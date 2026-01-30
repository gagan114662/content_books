---
id: newtons-laws
subject: physics
display_name: Newton's Laws of Motion
description: |
  Applies Newton's three laws to analyze forces and motion.
  Use when students need to draw free body diagrams, calculate net force, or solve equilibrium problems.

grade_band: 9-12
khan_tags: [physics, forces, newtons-laws, dynamics]
standards:
  - NGSS.HS-PS2-1
  - NGSS.HS-PS2-3

objectives:
  - State and apply Newton's three laws of motion
  - Draw and interpret free body diagrams
  - Calculate net force and resulting acceleration
  - Solve equilibrium problems (ΣF = 0)
  - Apply Newton's third law to identify action-reaction pairs

prerequisites:
  - kinematics-1d
  - kinematics-2d
  - algebra-linear-equations

estimated_time_minutes: 60

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 4
    url: https://openstax.org/books/college-physics/pages/4-introduction-to-dynamics-newtons-laws-of-motion
    license: CC-BY-4.0
---

# Newton's Laws of Motion

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Objects need force to keep moving" | Objects in motion stay in motion without force (1st Law) |
| "Heavier objects need more force to start moving" | Mass determines acceleration for a given force: a = F/m |
| "Action-reaction forces cancel out" | Action-reaction pairs act on DIFFERENT objects, so they don't cancel |
| "No motion means no forces" | Objects at rest can have many forces that sum to zero (equilibrium) |
| "Force causes velocity" | Force causes acceleration (change in velocity), not velocity itself |

## Key Concepts

### Newton's First Law (Law of Inertia)
An object at rest stays at rest, and an object in motion stays in motion at constant velocity, unless acted upon by a net external force.

**Key insight**: Inertia is the tendency to resist changes in motion. Mass is a measure of inertia.

### Newton's Second Law
The acceleration of an object is directly proportional to the net force and inversely proportional to its mass.

```
ΣF = ma    or    a = ΣF/m
```

- **ΣF** = net force (vector sum of all forces)
- **m** = mass (scalar, in kg)
- **a** = acceleration (vector, in m/s²)

### Newton's Third Law
For every action, there is an equal and opposite reaction.

**Key insight**: Forces always come in pairs acting on different objects.
- If A pushes B with force F, then B pushes A with force -F
- These forces are equal in magnitude, opposite in direction

### Free Body Diagrams (FBD)
A diagram showing ALL forces acting on a SINGLE object:
1. Draw the object as a point or simple shape
2. Draw arrows for each force, starting from the object
3. Label each force (W, N, T, f, F_applied, etc.)
4. Arrow length should indicate relative magnitude

### Common Forces
- **Weight (W or Fg)**: W = mg, always points down
- **Normal force (N)**: Perpendicular to surface, pushes away from surface
- **Tension (T)**: Along rope/string, pulls away from object
- **Friction (f)**: Parallel to surface, opposes motion or tendency to move
- **Applied force (F)**: Any external push or pull

## Equations

```
[1] ΣF = ma (Newton's Second Law)
[2] W = mg (Weight)
[3] ΣFx = max (x-component)
[4] ΣFy = may (y-component)
[5] For equilibrium: ΣF = 0 (or ΣFx = 0 and ΣFy = 0)
```

## Worked Examples

### Example 1: Horizontal Push
**Problem**: A 10 kg box is pushed with a force of 50 N on a frictionless surface. What is its acceleration?

**Solution**:
1. Draw FBD: Weight (W) down, Normal (N) up, Applied force (F) horizontal
2. Apply Newton's 2nd Law in x-direction:
   - ΣFx = ma
   - 50 = 10 × a
   - a = 5.0 m/s²

### Example 2: Elevator Problem
**Problem**: A 70 kg person stands on a scale in an elevator accelerating upward at 2 m/s². What does the scale read?

**Solution**:
1. Draw FBD: Weight (W = mg) down, Normal force (N = scale reading) up
2. Choose up as positive
3. Apply Newton's 2nd Law:
   - ΣF = ma
   - N - mg = ma
   - N = m(g + a) = 70(9.8 + 2) = 70 × 11.8 = **826 N**

### Example 3: Two Blocks
**Problem**: Two blocks (3 kg and 5 kg) are pushed across a frictionless surface by a 24 N force applied to the 3 kg block. Find the force between the blocks.

**Solution**:
1. Find total acceleration: a = F/(m₁ + m₂) = 24/8 = 3 m/s²
2. For the 5 kg block alone, the only horizontal force is from the 3 kg block:
   - F_contact = m₂ × a = 5 × 3 = **15 N**

## Explanation Patterns

1. **Always draw a Free Body Diagram first** - identify all forces on the object
2. **Choose a coordinate system** - typically x horizontal, y vertical
3. **Break forces into components** if they're at angles
4. **Write ΣF = ma for each direction** (x and y separately)
5. **Solve the resulting equations** - often simultaneous equations
6. **Check your answer**: units should be N or m/s², sign should make physical sense

## Common Problem Types

1. **Single object, horizontal forces**: Direct application of F = ma
2. **Inclined plane (without friction)**: Break weight into components
3. **Connected objects**: Use same acceleration, different forces
4. **Elevator/vertical acceleration**: Scale reads N, not mg
5. **Equilibrium**: ΣF = 0, solve for unknown force
6. **Action-reaction identification**: Forces on different objects
