# Universal Content Library System for AI Tutor

## Overview

Build a **deterministic content library system** covering **27 subjects** using CC-licensed OER (primarily OpenStax) as the truth layer. Each subject follows the same SKILLs pattern with subject-appropriate validation.

## Subject Coverage Matrix

| Category | Subject | OER Source | Validation | Skills |
|----------|---------|------------|------------|--------|
| **STEM Core** | Physics | OpenStax College Physics | Numeric solver (units) | 16 |
| | Chemistry | OpenStax Chemistry 2e | Numeric solver (stoich) | 14 |
| | Biology | OpenStax Biology 2e | MCQ + calculators | 18 |
| | Economics | OpenStax Principles of Economics 3e | Numeric + graphs | 12 |
| | Statistics | OpenStax Introductory Statistics 2e | Numeric solver | 10 |
| **Computer Science** | CS/Programming | Think Python, Eloquent JS | Code execution | 12 |
| | Data Structures | Think Data Structures | Trace validation | 8 |
| **Life Sciences** | Anatomy & Physiology | OpenStax Anatomy & Physiology 2e | MCQ + diagram labeling | 14 |
| | Human Biology/Health | OpenStax Human Biology OER | MCQ + lifestyle scenarios | 10 |
| | Nutrition | OER Nutrition texts | MCQ + meal analysis | 8 |
| **Earth/Environmental** | Earth Science | OER Earth Science texts | MCQ + diagram-based | 10 |
| | Environmental Science | OER Environmental Science | MCQ + case studies | 12 |
| | Sustainability/Policy | Environmental policy OER | Rubric + debate prompts | 8 |
| **Social Science** | History (US) | OpenStax U.S. History | Rubric + fact-check | 15 |
| | History (World) | OER World History | Rubric + fact-check | 15 |
| | Psychology | OpenStax Psychology 2e | MCQ + rubric | 14 |
| | Sociology | OpenStax Intro to Sociology 3e | Rubric grading | 12 |
| | Civics/Government | OpenStax American Government 3e | Fact-check + rubric | 10 |
| | Geography | OER Geography texts | MCQ + map-based | 10 |
| | Philosophy/Ethics | OER Intro Philosophy | Rubric grading | 8 |
| **Business/Law** | Intro Business | OER Business/Management texts | MCQ + case analysis | 10 |
| | Intro Law/Criminal Justice | OER Criminal Justice texts | Rubric + scenario-based | 10 |
| **Arts/Humanities** | Art History | OER Art History surveys | Rubric + comparison | 10 |
| | Music Theory | Open Music Theory (OMT2) | MCQ + notation exercises | 12 |
| | Music Appreciation | OER Music listening guides | Rubric + reflection | 8 |
| **Communication** | Academic Writing | OER Composition texts | Rubric + mechanics | 10 |
| | Public Speaking | OER Communication texts | Checklist + rubric | 8 |

**Additional Subjects (Phase 2 expansion)**:

| Category | Subject | OER Source | Validation | Skills |
|----------|---------|------------|------------|--------|
| **Academic/Theoretical** | Formal Logic | forall x, Concise Intro to Logic | Proof checker + MCQ | 8 |
| | Critical Thinking | OER Critical Thinking texts | Rubric + fallacy ID | 8 |
| | Media Studies | Media Studies 101 | Rubric + analysis | 8 |
| **Health/Nursing** | Nursing Fundamentals | TMU Nursing OER | Checklist + scenarios | 10 |
| | Public Health | Public Health OER | Numeric + epidemiology | 8 |
| **Vocational/Trades** | Electrical Trades | BCcampus Trades OER | Numeric + procedures | 10 |
| | Mechanical Trades | Trades OER collections | Procedures + diagrams | 8 |
| | Business/Workplace | OER Business Communication | Rubric + scenarios | 8 |
| **Meta/Cross-cutting** | Study Skills | College Success OER | Checklist + reflection | 6 |
| | Digital Literacy | Media Literacy OER | MCQ + source eval | 6 |

**K-12 Math (Khan Academy aligned)**:

| Grade Band | Topics | Skills |
|------------|--------|--------|
| K-2 | Counting, addition, subtraction, shapes | 15 |
| 3-5 | Multiplication, division, fractions, decimals | 20 |
| 6-8 | Pre-algebra, ratios, geometry, stats | 25 |
| Algebra 1 | Linear equations, inequalities, functions | 15 |
| Geometry | Proofs, triangles, circles, transformations | 15 |
| Algebra 2 | Polynomials, exponentials, trig | 15 |
| Precalculus | Functions, trig, complex numbers | 12 |
| Calculus | Limits, derivatives, integrals | 15 |
| SAT/ACT Prep | Math, reading, writing sections | 20 |

**Total**: ~40+ subjects, ~500+ skills, ~10,000+ problems

---

## Guiding Principle

> **For every topic covered in Khan Academy, we build a SKILL folder grounded in CC-licensed OER with deterministic validation.**

---

## 1. SKILL.md Schema (Concrete Spec)

Every SKILL.md file MUST follow this exact schema:

```yaml
---
# === REQUIRED METADATA ===
id: kinematics-1d                      # Unique ID (kebab-case)
subject: physics                        # Subject key
display_name: One-Dimensional Kinematics
description: |
  Analyzes motion in one dimension using position, velocity, and acceleration.
  Use when students need to solve constant-acceleration problems or interpret motion graphs.

# === CATEGORIZATION ===
grade_band: 9-12                        # K-2, 3-5, 6-8, 9-12, college
khan_tags: [physics, kinematics, motion] # Align to Khan Academy taxonomy
standards:
  - NGSS.HS-PS2-1                       # Next Gen Science Standards
  - CC.HSN-Q.A.1                        # Common Core (where applicable)

# === LEARNING STRUCTURE ===
objectives:
  - Define position, displacement, velocity, and acceleration
  - Interpret position-time and velocity-time graphs
  - Apply kinematic equations to constant-acceleration problems
  - Solve free-fall problems using g = 9.8 m/s²

prerequisites:
  - algebra-linear-equations            # Must complete these first
  - scientific-notation

estimated_time_minutes: 45              # Time to teach + practice

# === VALIDATION CONFIG ===
validator:
  type: numeric_solver                  # numeric_solver | code_executor | mcq | rubric | fact_check | writing
  config:
    unit_library: physics               # Which unit definitions to load
    default_tolerance: 0.02             # 2% relative tolerance
    require_units: true                 # Student must include units

# === SOURCES ===
sources:
  - name: OpenStax College Physics
    chapter: 2
    url: https://openstax.org/books/college-physics/pages/2-introduction
    license: CC-BY-4.0
---

# One-Dimensional Kinematics

## Misconceptions
<!-- Common wrong mental models to address -->
| Misconception | Correction |
|--------------|------------|
| "Zero velocity means zero acceleration" | Object at peak of trajectory has v=0 but a=g downward |
| "Heavier objects fall faster" | All objects fall at same rate (g) without air resistance |
| "Acceleration means speeding up" | Acceleration is any change in velocity (can be slowing down) |

## Key Concepts
<!-- Core content chunks, each <200 words -->
### Position and Displacement
Position (x) is location relative to an origin. Displacement (Δx = x₂ - x₁) is change in position.
**Key distinction**: Distance is total path length (scalar), displacement is change in position (vector).

### Velocity
- Average velocity: v_avg = Δx / Δt
- Instantaneous velocity: slope of x-t graph at a point

### Acceleration
- Average acceleration: a_avg = Δv / Δt
- Instantaneous acceleration: slope of v-t graph at a point

## Equations
<!-- Numbered for reference in problems -->
```
[1] v = v₀ + at
[2] x = x₀ + v₀t + ½at²
[3] v² = v₀² + 2a(x - x₀)
[4] x = x₀ + ½(v₀ + v)t
```

## Worked Examples
<!-- 2-3 fully worked problems with reasoning -->
### Example 1: Basic Displacement
**Problem**: A car accelerates from rest at 3.0 m/s² for 8.0 s. How far does it travel?

**Solution**:
1. Identify: v₀ = 0, a = 3.0 m/s², t = 8.0 s, find x
2. Select equation [2] (has x, v₀, a, t, no v)
3. Simplify: x = 0 + 0 + ½(3.0)(8.0)² = ½(3.0)(64) = **96 m**
4. Check: Units are m, magnitude reasonable for 8s of acceleration

## Explanation Patterns
<!-- How the tutor should explain this topic -->
1. Start with physical intuition (real-world example)
2. Draw diagram with coordinate system and sign conventions
3. List knowns and unknowns explicitly
4. Select equation based on what's known/unknown
5. Solve algebraically BEFORE substituting numbers
6. Check units and reasonableness of answer
```

---

## 2. Skills Enumeration (v1 Backlog)

### Physics (16 skills)
```
physics/
├── 01-kinematics-1d           # Position, velocity, acceleration, free fall
├── 02-kinematics-2d           # Projectile motion, relative motion
├── 03-newtons-laws            # F=ma, free body diagrams, equilibrium
├── 04-forces-friction         # Static/kinetic friction, inclined planes
├── 05-circular-motion         # Centripetal acceleration, orbits
├── 06-energy-work             # Work, KE, PE, conservation of energy
├── 07-momentum                # Impulse, collisions, conservation
├── 08-rotational-motion       # Torque, angular velocity, moment of inertia
├── 09-oscillations            # Simple harmonic motion, pendulums, springs
├── 10-waves                   # Wave properties, interference, standing waves
├── 11-sound                   # Sound waves, Doppler effect, resonance
├── 12-thermodynamics          # Heat, temperature, gas laws, engines
├── 13-electrostatics          # Coulomb's law, electric field, potential
├── 14-circuits                # Ohm's law, series/parallel, RC circuits
├── 15-magnetism               # Magnetic force, induction, EM waves
└── 16-optics                  # Reflection, refraction, lenses, mirrors
```

### Chemistry (14 skills)
```
chemistry/
├── 01-atomic-structure        # Atoms, isotopes, electron configuration
├── 02-periodic-table          # Trends, groups, properties
├── 03-chemical-bonding        # Ionic, covalent, metallic, Lewis structures
├── 04-stoichiometry           # Mole conversions, limiting reagent, yield
├── 05-reactions-equations     # Balancing, types of reactions, predicting products
├── 06-gas-laws                # Ideal gas law, partial pressures, kinetic theory
├── 07-thermochemistry         # Enthalpy, Hess's law, calorimetry
├── 08-solutions               # Molarity, dilution, colligative properties
├── 09-kinetics                # Rate laws, activation energy, catalysts
├── 10-equilibrium             # Kc, Kp, Le Chatelier's principle, ICE tables
├── 11-acids-bases             # pH, pKa, buffers, titrations
├── 12-electrochemistry        # Redox, galvanic cells, electrolysis
├── 13-organic-intro           # Functional groups, naming, basic reactions
└── 14-nuclear-chemistry       # Radioactivity, half-life, fission/fusion
```

### K-8 Math (60 skills)
```
math-k2/
├── counting-to-100
├── addition-single-digit
├── subtraction-single-digit
├── place-value-tens-ones
├── basic-shapes
└── ... (15 total)

math-3-5/
├── multiplication-facts
├── division-facts
├── fractions-intro
├── fractions-operations
├── decimals-intro
├── area-perimeter
└── ... (20 total)

math-6-8/
├── ratios-proportions
├── percents
├── integers-operations
├── expressions-equations
├── linear-relationships
├── geometry-angles
├── statistics-intro
└── ... (25 total)
```

### Algebra 1 (15 skills)
```
algebra-1/
├── 01-variables-expressions
├── 02-solving-linear-equations
├── 03-linear-inequalities
├── 04-graphing-linear-functions
├── 05-slope-intercept
├── 06-systems-of-equations
├── 07-exponents-rules
├── 08-polynomials-operations
├── 09-factoring-polynomials
├── 10-quadratic-equations
├── 11-quadratic-formula
├── 12-functions-intro
├── 13-radical-expressions
├── 14-rational-expressions
└── 15-data-analysis
```

---

## 3. Validator I/O Specifications

### NumericSolver (Physics, Chemistry, Economics, Statistics)

**Input Schema**:
```json
{
  "validator_type": "numeric_solver",
  "problem_id": "kin1d_001",
  "student_answer": "96 m",
  "expected": {
    "value": 96,
    "unit": "m",
    "tolerance": 0.02,
    "tolerance_type": "relative"
  },
  "config": {
    "unit_library": "physics",
    "allow_equivalent_units": true
  }
}
```

**Output Schema**:
```json
{
  "correct": true,
  "score": 1.0,
  "student_parsed": {
    "value": 96.0,
    "unit": "meter"
  },
  "expected_parsed": {
    "value": 96.0,
    "unit": "meter"
  },
  "feedback": null,
  "error_code": null
}
```

**Error Codes**:
| Code | Meaning | TeachingAssistant Action |
|------|---------|--------------------------|
| `CORRECT` | Within tolerance | Praise, move to next |
| `WRONG_VALUE` | Value outside tolerance | Show hint, ask to retry |
| `WRONG_UNIT` | Correct value, wrong unit | "Check your units" |
| `UNIT_MISMATCH` | Incompatible dimensions | "Your answer has wrong dimensions" |
| `PARSE_ERROR` | Can't parse input | "Please enter a number with units" |
| `SIGN_ERROR` | Correct magnitude, wrong sign | "Check the sign of your answer" |

---

### CodeExecutor (CS, Data Structures)

**Input Schema**:
```json
{
  "validator_type": "code_executor",
  "problem_id": "cs_func_001",
  "student_code": "def factorial(n):\n    if n <= 1: return 1\n    return n * factorial(n-1)",
  "language": "python",
  "test_cases": [
    {"input": [0], "expected": 1},
    {"input": [5], "expected": 120}
  ],
  "config": {
    "timeout_seconds": 5,
    "memory_limit_mb": 128
  }
}
```

**Output Schema**:
```json
{
  "correct": true,
  "score": 1.0,
  "tests_passed": 4,
  "tests_total": 4,
  "test_results": [
    {"input": [0], "expected": 1, "actual": 1, "passed": true},
    {"input": [5], "expected": 120, "actual": 120, "passed": true}
  ],
  "execution_time_ms": 12,
  "feedback": null,
  "error_code": null
}
```

**Error Codes**:
| Code | Meaning | TeachingAssistant Action |
|------|---------|--------------------------|
| `ALL_PASSED` | All tests pass | Move to next problem |
| `PARTIAL_PASS` | Some tests fail | Show failing case, hint at edge case |
| `RUNTIME_ERROR` | Code crashes | Show error message, suggest debugging |
| `TIMEOUT` | Exceeded time limit | "Your code is too slow" |
| `SYNTAX_ERROR` | Won't compile/parse | Show syntax error location |

---

### MCQGrader (All Subjects)

**Input Schema**:
```json
{
  "validator_type": "mcq",
  "problem_id": "bio_cell_001",
  "student_answer": 1,
  "correct_answer": 1,
  "options": [
    "Nucleus",
    "Mitochondria",
    "Ribosome",
    "Golgi apparatus"
  ]
}
```

**Output Schema**:
```json
{
  "correct": true,
  "score": 1.0,
  "selected_option": "Mitochondria",
  "correct_option": "Mitochondria",
  "explanation": "Mitochondria produce most of the cell's ATP through cellular respiration.",
  "feedback": null
}
```

---

### RubricGrader (History, Psychology, Sociology, Philosophy)

**Input Schema**:
```json
{
  "validator_type": "rubric",
  "problem_id": "hist_cw_001",
  "student_answer": "The Civil War was caused by slavery...",
  "rubric": {
    "full_credit": "Identifies slavery as primary cause with specific evidence",
    "partial_credit": "Mentions slavery but lacks supporting evidence",
    "no_credit": "Incorrect or off-topic"
  },
  "must_mention": ["slavery", "expansion", "secession"],
  "exemplar": "The primary cause of the Civil War was slavery..."
}
```

**Output Schema**:
```json
{
  "correct": true,
  "score": 0.5,
  "facts_mentioned": ["slavery", "secession"],
  "facts_missing": ["expansion"],
  "rubric_level": "partial_credit",
  "justification": "Student correctly identifies slavery but doesn't discuss expansion into territories.",
  "feedback": "Good start! Consider how the debate over slavery's expansion into new territories contributed to tensions.",
  "confidence": 0.85
}
```

---

### FactChecker (History, Civics)

**Input Schema**:
```json
{
  "validator_type": "fact_check",
  "problem_id": "civics_fed_001",
  "student_answer": "The Supreme Court can declare laws unconstitutional...",
  "required_facts": [
    {"fact": "judicial review", "weight": 0.4},
    {"fact": "Marbury v. Madison", "weight": 0.3},
    {"fact": "checks and balances", "weight": 0.3}
  ]
}
```

**Output Schema**:
```json
{
  "correct": true,
  "score": 0.7,
  "facts_found": [
    {"fact": "judicial review", "found": true, "quote": "...can declare laws unconstitutional..."},
    {"fact": "Marbury v. Madison", "found": false, "quote": null},
    {"fact": "checks and balances", "found": true, "quote": "...balance of power..."}
  ],
  "feedback": "Good explanation! Mentioning Marbury v. Madison (1803) would strengthen your answer."
}
```

---

### WritingRubric (Academic Writing, Public Speaking)

**Input Schema**:
```json
{
  "validator_type": "writing",
  "problem_id": "write_thesis_001",
  "student_text": "Social media has changed communication...",
  "dimensions": ["thesis_clarity", "arguability", "scope"],
  "exemplar": "While social media has expanded reach..."
}
```

**Output Schema**:
```json
{
  "correct": false,
  "score": 0.5,
  "overall_score": 0.5,
  "dimension_scores": {
    "thesis_clarity": 0.6,
    "arguability": 0.4,
    "scope": 0.5
  },
  "dimension_feedback": {
    "thesis_clarity": "Your thesis is somewhat clear but could be more specific.",
    "arguability": "This reads more like a fact than an arguable claim. Take a stronger stance.",
    "scope": "Good scope for a short essay."
  },
  "revision_suggestions": [
    "Add 'has improved' or 'has harmed' to make it arguable",
    "Specify which aspect of communication you're addressing"
  ]
}
```

---

## 4. Integration Contract with Tutor

### Flow: Student Starts a Topic

```
┌─────────────┐     ┌─────────────────┐     ┌──────────────┐
│   Frontend  │────▶│ TeachingAssist. │────▶│ DASH System  │
│  (React)    │     │   (FastAPI)     │     │  (FastAPI)   │
└─────────────┘     └─────────────────┘     └──────────────┘
       │                    │                      │
       │ 1. Start topic     │                      │
       │    (physics,       │ 2. Get user state    │
       │     kinematics)    │    & select SKILL    │
       │                    │◀─────────────────────│
       │                    │                      │
       │                    │ 3. Load SKILL.md     │
       │                    │    from content/     │
       │                    │                      │
       │                    │ 4. Build tutor       │
       │                    │    prompt with       │
       │                    │    SKILL context     │
       │                    │                      │
       │◀───────────────────│ 5. Return lesson     │
       │   Lesson content   │    + first problem   │
       │   + problem        │                      │
       │                    │                      │
       │ 6. Student submits │                      │
       │    answer          │                      │
       │────────────────────▶                      │
       │                    │ 7. Call validator    │
       │                    │    (NumericSolver)   │
       │                    │                      │
       │                    │ 8. Get result        │
       │                    │    {correct, score,  │
       │                    │     feedback}        │
       │                    │                      │
       │                    │ 9. Update user       │
       │                    │    skill_states      │
       │                    │────────────────────▶ │
       │                    │                      │
       │◀───────────────────│ 10. Return feedback  │
       │   Feedback +       │     + next action    │
       │   next problem     │                      │
       └────────────────────┴──────────────────────┘
```

### API Contracts

**1. Start Topic Session**
```
POST /api/session/start-topic
Request:
{
  "user_id": "user_xxx",
  "subject": "physics",
  "skill_id": "kinematics-1d"  // Optional, auto-select if null
}

Response:
{
  "session_id": "sess_xxx",
  "skill": {
    "id": "kinematics-1d",
    "display_name": "One-Dimensional Kinematics",
    "objectives": [...],
    "estimated_time_minutes": 45
  },
  "user_state": {
    "memory_strength": 0.3,
    "problems_attempted": 5,
    "problems_correct": 2
  },
  "first_problem": {
    "problem_id": "kin1d_003",
    "question": "A ball is dropped from 45 m. How long until it hits the ground?",
    "difficulty": 0.4,
    "hints_available": 2
  },
  "tutor_context_loaded": true
}
```

**2. Get SKILL Context (Internal)**
```
GET /api/skills/{skill_id}/context
Response:
{
  "skill_id": "kinematics-1d",
  "content_md": "# One-Dimensional Kinematics\n\n## Misconceptions...",
  "objectives": [...],
  "misconceptions": [...],
  "equations": [...],
  "explanation_patterns": [...],
  "validator_config": {
    "type": "numeric_solver",
    "unit_library": "physics"
  }
}
```

**3. Submit Answer**
```
POST /api/problems/submit
Request:
{
  "session_id": "sess_xxx",
  "problem_id": "kin1d_003",
  "student_answer": "3.0 s"
}

Response:
{
  "validation_result": {
    "correct": true,
    "score": 1.0,
    "feedback": null,
    "error_code": "CORRECT"
  },
  "updated_skill_state": {
    "memory_strength": 0.45,
    "problems_attempted": 6,
    "problems_correct": 3
  },
  "next_action": "next_problem",  // next_problem | show_hint | review_concept | topic_complete
  "next_problem": {
    "problem_id": "kin1d_007",
    "question": "...",
    "difficulty": 0.5
  }
}
```

**4. Tutor LLM System Prompt Template**
```python
TUTOR_SYSTEM_PROMPT = """
You are a {subject} tutor helping a student master {skill_display_name}.

## Learning Objectives
{objectives_list}

## Key Concepts
{concepts_from_skill_md}

## Misconceptions to Watch For
{misconceptions_table}

## How to Explain This Topic
{explanation_patterns}

## Current Problem
{current_problem}

## Student State
- Problems attempted: {problems_attempted}
- Accuracy: {accuracy_percent}%
- Common errors: {common_errors}

Guidelines:
1. If student is wrong, identify which misconception might be at play
2. Use the explanation patterns above
3. Give hints progressively, don't reveal answer immediately
4. When student is correct, briefly reinforce the concept then move on
"""
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        AI Tutor App                             │
├─────────────────────────────────────────────────────────────────┤
│  Frontend (React)                                               │
│  ├── SubjectBrowser → All 17 subjects                          │
│  ├── TopicBrowser → Skills within subject                       │
│  ├── ProblemSolver → Work problems with validation              │
│  └── SkillViewer → SKILL.md content + references                │
├─────────────────────────────────────────────────────────────────┤
│  Validation Services                                            │
│  ├── NumericSolver → Physics, Chemistry, Econ, Stats            │
│  ├── CodeExecutor → CS, Data Structures                         │
│  ├── MCQGrader → All subjects                                   │
│  ├── RubricGrader → History, Psych, Soc, Writing, Philosophy    │
│  └── FactChecker → History, Civics (must-mention lists)         │
├─────────────────────────────────────────────────────────────────┤
│  Content Storage                                                │
│  └── content/{subject}/{skill}/SKILL.md + problems/             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Content Directory Structure

```
content/
├── stem/
│   ├── physics/           # OpenStax College Physics
│   │   ├── 01-kinematics-1d/
│   │   ├── 02-kinematics-2d/
│   │   ├── 03-newtons-laws/
│   │   ├── 04-forces-friction/
│   │   ├── 05-circular-motion/
│   │   ├── 06-energy-work/
│   │   ├── 07-momentum/
│   │   ├── 08-rotational-motion/
│   │   ├── 09-oscillations/
│   │   ├── 10-waves/
│   │   ├── 11-sound/
│   │   ├── 12-thermodynamics/
│   │   ├── 13-electrostatics/
│   │   ├── 14-circuits/
│   │   ├── 15-magnetism/
│   │   └── 16-optics/
│   │
│   ├── chemistry/         # OpenStax Chemistry 2e
│   │   ├── 01-atomic-structure/
│   │   ├── 02-periodic-table/
│   │   ├── 03-chemical-bonding/
│   │   ├── 04-stoichiometry/
│   │   └── ...
│   │
│   ├── biology/           # OpenStax Biology 2e
│   │   ├── 01-scientific-method/
│   │   ├── 02-chemistry-of-life/
│   │   └── ...
│   │
│   └── math-algebra1/     # Khan Academy aligned
│       ├── 01-variables-expressions/
│       ├── 02-solving-linear-equations/
│       └── ...
│
├── social-science/
│   ├── history-us/
│   ├── psychology/
│   └── ...
│
└── communication/
    ├── academic-writing/
    └── public-speaking/
```

---

## Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
- [x] Create full content directory structure
- [x] Build ValidationService skeleton with router
- [x] Set up MongoDB collections
- [x] Create base validators (MCQ, Numeric)

### Phase 2: STEM Core (Week 3-4)
- [ ] Physics: 6 skills + NumericSolver
- [ ] Chemistry: 4 skills + ChemistrySolver
- [ ] 20 problems per skill
- [ ] Integration tests

### Phase 3: More STEM (Week 5-6)
- [ ] Biology: 8 skills + MCQ + Hardy-Weinberg
- [ ] Economics: 4 skills + equilibrium solver
- [ ] Statistics: 4 skills + distribution calculations

### Phase 4: Social Science (Week 7-8)
- [ ] History (US): 8 skills + RubricGrader + FactChecker
- [ ] Psychology: 6 skills
- [ ] Civics: 4 skills

### Phase 5: Communication (Week 9)
- [ ] Academic Writing: 5 skills + WritingRubric
- [ ] Public Speaking: 4 skills

### Phase 6: CS (Week 10)
- [ ] CS Programming: 6 skills + CodeExecutor
- [ ] Data Structures: 4 skills

### Phase 7: Remaining Subjects (Week 11-12)
- [ ] World History, Sociology, Geography
- [ ] Philosophy, Art History

### Phase 8: Evaluation & Polish (Week 13+)
- [ ] Offline eval for all subjects
- [ ] 90%+ accuracy threshold
- [ ] A/B testing with/without SKILL context
- [ ] Expand problem banks

---

## Current Progress

### Completed
- ValidationService with NumericSolver and MCQGrader
- MongoDB migration script
- Physics skill 01-kinematics-1d (SKILL.md + 20 problems)
- Physics skill 02-kinematics-2d (SKILL.md + 20 problems)

### In Progress
- Physics skills 03-06 (SKILL.md + problems.json)

### Next Up
- Chemistry skills 01-04
- Biology skills 01-05
- Algebra 1 skills 01-05
