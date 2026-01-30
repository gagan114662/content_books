#!/usr/bin/env python3
"""
MongoDB Migration Script for AI Tutor Content Library

This script imports SKILL content and problems from the content directory
into a local MongoDB instance.

Usage:
    python migrate_to_mongo.py --mongo-uri mongodb://localhost:27017 --db aitutor_db

Collections created:
    - courses: Course metadata
    - units: Units within courses
    - exercises: Exercise sets
    - questions: Individual questions (Perseus format)
    - skills: SKILL.md content (parsed)
    - user_progress: Student mastery tracking (schema only)
"""

import argparse
import json
import os
import re
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False
    print("Warning: PyYAML not installed. SKILL.md parsing will be limited.")

try:
    from pymongo import MongoClient, ASCENDING, DESCENDING
    from pymongo.errors import DuplicateKeyError
    MONGO_AVAILABLE = True
except ImportError:
    MONGO_AVAILABLE = False
    print("Error: pymongo not installed. Run: pip install pymongo")


# Default paths
CONTENT_ROOT = Path(__file__).parent.parent.parent.parent / "content"
DEFAULT_MONGO_URI = "mongodb://localhost:27017"
DEFAULT_DB_NAME = "aitutor_db"


def parse_skill_md(file_path: Path) -> dict:
    """
    Parse a SKILL.md file into structured data.

    Returns:
        dict with 'metadata' (from YAML frontmatter) and 'content' (markdown body)
    """
    content = file_path.read_text(encoding="utf-8")

    # Extract YAML frontmatter between --- markers
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)

    if not frontmatter_match:
        return {
            "metadata": {},
            "content": content,
            "raw": content
        }

    yaml_content = frontmatter_match.group(1)
    markdown_content = frontmatter_match.group(2)

    metadata = {}
    if YAML_AVAILABLE:
        try:
            metadata = yaml.safe_load(yaml_content) or {}
        except yaml.YAMLError as e:
            print(f"Warning: Could not parse YAML in {file_path}: {e}")

    return {
        "metadata": metadata,
        "content": markdown_content,
        "raw": content
    }


def load_problems_json(file_path: Path) -> dict:
    """Load and parse a problems.json file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing {file_path}: {e}")
        return {"questions": []}


def generate_id(prefix: str, *parts: str) -> str:
    """Generate a deterministic hex ID from parts."""
    combined = "_".join(str(p) for p in parts)
    hash_hex = hashlib.md5(combined.encode()).hexdigest()[:16]
    return f"x{prefix}{hash_hex[:15]}"


def create_indexes(db) -> None:
    """Create MongoDB indexes for efficient queries."""

    # Questions collection indexes
    db.questions.create_index([("question_id", ASCENDING)], unique=True)
    db.questions.create_index([("skill_id", ASCENDING)])
    db.questions.create_index([("exercise_id", ASCENDING)])
    db.questions.create_index([("difficulty", ASCENDING)])
    db.questions.create_index([("course_id", ASCENDING), ("unit_id", ASCENDING)])
    db.questions.create_index([("tags", ASCENDING)])

    # Skills collection indexes
    db.skills.create_index([("skill_id", ASCENDING)], unique=True)
    db.skills.create_index([("folder_key", ASCENDING)])
    db.skills.create_index([("subject", ASCENDING)])
    db.skills.create_index([("grade_band", ASCENDING)])

    # Courses collection indexes
    db.courses.create_index([("course_id", ASCENDING)], unique=True)
    db.courses.create_index([("subject", ASCENDING)])

    # Units collection indexes
    db.units.create_index([("unit_id", ASCENDING)], unique=True)
    db.units.create_index([("course_id", ASCENDING)])

    # Exercises collection indexes
    db.exercises.create_index([("exercise_id", ASCENDING)], unique=True)
    db.exercises.create_index([("skill_id", ASCENDING)])

    # User progress indexes
    db.user_progress.create_index([("user_id", ASCENDING)])
    db.user_progress.create_index([("user_id", ASCENDING), ("skill_id", ASCENDING)], unique=True)

    print("Created indexes on all collections")


def migrate_skill_folder(
    skill_path: Path,
    db,
    subject: str,
    course_id: str,
    unit_id: str,
    dry_run: bool = False
) -> dict:
    """
    Migrate a single skill folder to MongoDB.

    Returns:
        dict with migration stats including:
        - folder_key: The folder name (e.g., "01-kinematics-1d")
        - skill_id: The id from SKILL.md frontmatter (may differ from folder_key)
    """
    folder_key = skill_path.name

    stats = {
        "skill_inserted": False,
        "folder_key": folder_key,
        "skill_id": None,
        "questions_inserted": 0,
        "exercises_created": set(),
        "errors": [],
        "warnings": []
    }

    skill_md_path = skill_path / "SKILL.md"
    problems_json_path = skill_path / "problems" / "problems.json"

    # Parse SKILL.md
    if skill_md_path.exists():
        skill_data = parse_skill_md(skill_md_path)
        metadata = skill_data["metadata"]

        # Validate skill_id presence
        skill_id = metadata.get("id")
        if not skill_id:
            stats["warnings"].append(f"Missing 'id' in SKILL.md frontmatter, using folder name: {folder_key}")
            skill_id = folder_key
        elif skill_id != folder_key:
            # Log when they differ (not an error, but worth noting)
            stats["warnings"].append(f"skill_id '{skill_id}' differs from folder '{folder_key}'")

        stats["skill_id"] = skill_id

        skill_doc = {
            "skill_id": skill_id,
            "folder_key": folder_key,  # Store both for reference
            "subject": subject,
            "course_id": course_id,
            "unit_id": unit_id,
            "display_name": metadata.get("display_name", skill_path.name),
            "description": metadata.get("description", ""),
            "grade_band": metadata.get("grade_band", "9-12"),
            "objectives": metadata.get("objectives", []),
            "prerequisites": metadata.get("prerequisites", []),
            "khan_tags": metadata.get("khan_tags", []),
            "standards": metadata.get("standards", []),
            "validator": metadata.get("validator", {}),
            "sources": metadata.get("sources", []),
            "content_md": skill_data["content"],
            "estimated_time_minutes": metadata.get("estimated_time_minutes", 30),
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc)
        }

        if not dry_run:
            try:
                db.skills.replace_one(
                    {"skill_id": skill_doc["skill_id"]},
                    skill_doc,
                    upsert=True
                )
                stats["skill_inserted"] = True
            except Exception as e:
                stats["errors"].append(f"Skill insert error: {e}")
        else:
            print(f"  [DRY RUN] Would insert skill: {skill_doc['skill_id']}")
            stats["skill_inserted"] = True

    # Load and migrate problems
    if problems_json_path.exists():
        problems_data = load_problems_json(problems_json_path)
        questions = problems_data.get("questions", [])

        for question in questions:
            # Add metadata
            question["subject"] = subject
            question["imported_at"] = datetime.now(timezone.utc)

            # Track exercises
            exercise_id = question.get("exercise_id")
            if exercise_id:
                stats["exercises_created"].add(exercise_id)

            if not dry_run:
                try:
                    db.questions.replace_one(
                        {"question_id": question["question_id"]},
                        question,
                        upsert=True
                    )
                    stats["questions_inserted"] += 1
                except Exception as e:
                    stats["errors"].append(f"Question insert error: {e}")
            else:
                stats["questions_inserted"] += 1

        # Create exercise documents
        for exercise_id in stats["exercises_created"]:
            exercise_questions = [q for q in questions if q.get("exercise_id") == exercise_id]
            exercise_doc = {
                "exercise_id": exercise_id,
                "skill_id": skill_doc.get("skill_id") if skill_md_path.exists() else skill_path.name,
                "subject": subject,
                "course_id": course_id,
                "unit_id": unit_id,
                "question_count": len(exercise_questions),
                "question_ids": [q["question_id"] for q in exercise_questions],
                "created_at": datetime.now(timezone.utc)
            }

            if not dry_run:
                try:
                    db.exercises.replace_one(
                        {"exercise_id": exercise_id},
                        exercise_doc,
                        upsert=True
                    )
                except Exception as e:
                    stats["errors"].append(f"Exercise insert error: {e}")

    return stats


def migrate_subject(
    subject_path: Path,
    db,
    dry_run: bool = False
) -> dict:
    """
    Migrate an entire subject directory to MongoDB.

    Returns:
        dict with migration stats
    """
    subject_name = subject_path.name
    category = subject_path.parent.name

    print(f"\nMigrating subject: {category}/{subject_name}")

    # Generate course ID
    course_id = generate_id("course", category, subject_name)

    # Read subject CLAUDE.md if exists
    claude_md_path = subject_path / "CLAUDE.md"
    subject_metadata = {}
    if claude_md_path.exists():
        subject_data = parse_skill_md(claude_md_path)
        subject_metadata = subject_data.get("metadata", {})

    # Create course document
    course_doc = {
        "course_id": course_id,
        "subject": subject_name,
        "category": category,
        "display_name": subject_metadata.get("display_name", subject_name.replace("-", " ").title()),
        "description": subject_metadata.get("description", ""),
        "grade_band": subject_metadata.get("grade_band", "9-12"),
        "unit_ids": [],
        "created_at": datetime.now(timezone.utc)
    }

    stats = {
        "course_id": course_id,
        "skills_migrated": 0,
        "questions_migrated": 0,
        "exercises_created": 0,
        "errors": [],
        "warnings": []
    }

    # Find all skill folders (directories starting with numbers)
    skill_folders = sorted([
        d for d in subject_path.iterdir()
        if d.is_dir() and re.match(r'^\d{2}-', d.name)
    ])

    # Generate unit ID for this subject (single unit per subject for now)
    unit_id = generate_id("unit", course_id, "main")
    course_doc["unit_ids"].append(unit_id)

    # Create unit document
    unit_doc = {
        "unit_id": unit_id,
        "course_id": course_id,
        "display_name": f"{subject_name.replace('-', ' ').title()} - Main Unit",
        "skills": [],  # Array of {folder_key, skill_id} for mapping
        "order": 0,
        "created_at": datetime.now(timezone.utc)
    }

    for skill_folder in skill_folders:
        print(f"  Processing: {skill_folder.name}")

        folder_stats = migrate_skill_folder(
            skill_folder,
            db,
            subject_name,
            course_id,
            unit_id,
            dry_run=dry_run
        )

        # Print any warnings
        for warning in folder_stats.get("warnings", []):
            print(f"    Warning: {warning}")

        if folder_stats["skill_inserted"]:
            stats["skills_migrated"] += 1
            # Store both folder_key and skill_id to avoid mismatches
            unit_doc["skills"].append({
                "folder_key": folder_stats["folder_key"],
                "skill_id": folder_stats["skill_id"]
            })

        stats["questions_migrated"] += folder_stats["questions_inserted"]
        stats["exercises_created"] += len(folder_stats["exercises_created"])
        stats["errors"].extend(folder_stats["errors"])
        stats["warnings"].extend(folder_stats.get("warnings", []))

    # Insert course and unit documents
    if not dry_run:
        try:
            db.courses.replace_one({"course_id": course_id}, course_doc, upsert=True)
            db.units.replace_one({"unit_id": unit_id}, unit_doc, upsert=True)
        except Exception as e:
            stats["errors"].append(f"Course/Unit insert error: {e}")

    return stats


def migrate_all(
    content_root: Path,
    db,
    dry_run: bool = False,
    subjects_filter: Optional[list] = None
) -> dict:
    """
    Migrate all content from the content directory to MongoDB.

    Args:
        content_root: Path to content directory
        db: MongoDB database instance
        dry_run: If True, don't actually insert anything
        subjects_filter: If provided, only migrate these subjects

    Returns:
        dict with overall migration stats
    """
    print(f"Starting migration from: {content_root}")
    print(f"Dry run: {dry_run}")

    if not dry_run:
        create_indexes(db)

    overall_stats = {
        "courses_migrated": 0,
        "skills_migrated": 0,
        "questions_migrated": 0,
        "exercises_created": 0,
        "errors": [],
        "warnings": []
    }

    # Find all category directories
    categories = [d for d in content_root.iterdir() if d.is_dir()]

    for category_path in categories:
        # Find all subject directories within category
        subject_dirs = [d for d in category_path.iterdir() if d.is_dir()]

        for subject_path in subject_dirs:
            # Apply filter if specified
            if subjects_filter and subject_path.name not in subjects_filter:
                continue

            subject_stats = migrate_subject(subject_path, db, dry_run=dry_run)

            overall_stats["courses_migrated"] += 1
            overall_stats["skills_migrated"] += subject_stats["skills_migrated"]
            overall_stats["questions_migrated"] += subject_stats["questions_migrated"]
            overall_stats["exercises_created"] += subject_stats["exercises_created"]
            overall_stats["errors"].extend(subject_stats["errors"])
            overall_stats["warnings"].extend(subject_stats.get("warnings", []))

    return overall_stats


def main():
    parser = argparse.ArgumentParser(
        description="Migrate AI Tutor content to MongoDB"
    )
    parser.add_argument(
        "--mongo-uri",
        default=DEFAULT_MONGO_URI,
        help=f"MongoDB connection URI (default: {DEFAULT_MONGO_URI})"
    )
    parser.add_argument(
        "--db",
        default=DEFAULT_DB_NAME,
        help=f"Database name (default: {DEFAULT_DB_NAME})"
    )
    parser.add_argument(
        "--content-root",
        type=Path,
        default=CONTENT_ROOT,
        help=f"Content directory root (default: {CONTENT_ROOT})"
    )
    parser.add_argument(
        "--subjects",
        nargs="*",
        help="Specific subjects to migrate (default: all)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't actually insert, just show what would happen"
    )
    parser.add_argument(
        "--drop-existing",
        action="store_true",
        help="Drop existing collections before migrating"
    )

    args = parser.parse_args()

    if not MONGO_AVAILABLE:
        print("Error: pymongo is required. Install with: pip install pymongo")
        return 1

    # Connect to MongoDB
    print(f"Connecting to MongoDB at {args.mongo_uri}...")
    client = MongoClient(args.mongo_uri)
    db = client[args.db]

    # Test connection
    try:
        client.admin.command("ping")
        print("Connected successfully!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return 1

    # Drop existing collections if requested
    if args.drop_existing and not args.dry_run:
        print("Dropping existing collections...")
        for collection in ["courses", "units", "exercises", "questions", "skills"]:
            db[collection].drop()
        print("Collections dropped.")

    # Run migration
    stats = migrate_all(
        args.content_root,
        db,
        dry_run=args.dry_run,
        subjects_filter=args.subjects
    )

    # Print summary
    print("\n" + "=" * 50)
    print("MIGRATION SUMMARY")
    print("=" * 50)
    print(f"Courses migrated:   {stats['courses_migrated']}")
    print(f"Skills migrated:    {stats['skills_migrated']}")
    print(f"Questions migrated: {stats['questions_migrated']}")
    print(f"Exercises created:  {stats['exercises_created']}")

    if stats["warnings"]:
        print(f"\nWarnings ({len(stats['warnings'])}):")
        for warning in stats["warnings"][:10]:
            print(f"  - {warning}")
        if len(stats["warnings"]) > 10:
            print(f"  ... and {len(stats['warnings']) - 10} more")

    if stats["errors"]:
        print(f"\nErrors ({len(stats['errors'])}):")
        for error in stats["errors"][:10]:
            print(f"  - {error}")
        if len(stats["errors"]) > 10:
            print(f"  ... and {len(stats['errors']) - 10} more")
    else:
        print("\nNo errors!")

    return 0


if __name__ == "__main__":
    exit(main())
