---
id: forces-friction
subject: physics
display_name: Forces and Friction
description: |
  Analyzes static and kinetic friction forces in various situations.
  Use when students need to solve problems involving friction on horizontal surfaces or inclined planes.

grade_band: 9-12
khan_tags: [physics, forces, friction, inclined-planes]
standards:
  - NGSS.HS-PS2-1

objectives:
  - Distinguish between static and kinetic friction
  - Calculate friction force using f = μN
  - Solve problems involving friction on horizontal surfaces
  - Analyze forces on inclined planes
  - Determine conditions for objects to slide or remain stationary

prerequisites:
  - newtons-laws
  - kinematics-1d

estimated_time_minutes: 60

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 5
    url: https://openstax.org/books/college-physics/pages/5-introduction-to-friction-drag-and-elasticity
    license: CC-BY-4.0
---

# Forces and Friction

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Friction always opposes motion" | Friction opposes relative motion or tendency to move; static friction can cause motion (walking, driving) |
| "Heavier objects have more friction because they're harder to push" | Heavier objects have more friction because N is larger (f = μN), not because of the weight directly |
| "Friction depends on surface area" | Friction is independent of surface area; it depends only on N and μ |
| "Static friction is always at maximum" | Static friction adjusts from 0 to fs,max; it equals the force trying to cause sliding |
| "Objects on inclines always slide" | Objects stay stationary if friction is sufficient to balance the component of weight along the surface |

## Key Concepts

### Types of Friction
1. **Static friction (fs)**: Acts when surfaces are not sliding relative to each other
   - Adjusts from 0 up to a maximum value
   - Maximum: fs,max = μs N

2. **Kinetic friction (fk)**: Acts when surfaces ARE sliding relative to each other
   - Constant for given surfaces: fk = μk N
   - Always less than or equal to fs,max (μk ≤ μs)

### Coefficient of Friction (μ)
- Dimensionless number depending on both surfaces
- μs = coefficient of static friction
- μk = coefficient of kinetic friction
- Typical values: wood on wood ~0.4, rubber on concrete ~0.8, ice on ice ~0.03

### Inclined Plane Analysis
For an object on an incline of angle θ:
- Weight components:
  - Parallel to surface: mg sin(θ)
  - Perpendicular to surface: mg cos(θ)
- Normal force: N = mg cos(θ)
- Critical angle: tan(θ) = μs

## Equations

```
[1] fs ≤ μs N (static friction)
[2] fk = μk N (kinetic friction)
[3] N = mg cos(θ) (normal force on incline)
[4] W_parallel = mg sin(θ) (weight component down incline)
[5] tan(θ_critical) = μs (angle at which sliding begins)
```

## Worked Examples

### Example 1: Horizontal Surface
**Problem**: A 20 kg box is pushed across a floor with μk = 0.3. What force is needed to keep it moving at constant velocity?

**Solution**:
1. At constant velocity, ΣF = 0
2. Normal force: N = mg = 20 × 9.8 = 196 N
3. Kinetic friction: fk = μk N = 0.3 × 196 = 58.8 N
4. Applied force must equal friction: F = **58.8 N**

### Example 2: Will It Slide?
**Problem**: A 5 kg block sits on a plane inclined at 25°. If μs = 0.5, will it slide?

**Solution**:
1. Weight component down the incline: mg sin(25°) = 5 × 9.8 × 0.423 = 20.7 N
2. Normal force: N = mg cos(25°) = 5 × 9.8 × 0.906 = 44.4 N
3. Maximum static friction: fs,max = 0.5 × 44.4 = 22.2 N
4. Since 20.7 N < 22.2 N, friction is sufficient. **No sliding.**

### Example 3: Acceleration on Incline
**Problem**: A 10 kg block slides down a 30° incline with μk = 0.2. Find the acceleration.

**Solution**:
1. Weight parallel: mg sin(30°) = 10 × 9.8 × 0.5 = 49 N
2. Normal force: N = mg cos(30°) = 10 × 9.8 × 0.866 = 84.9 N
3. Kinetic friction: fk = 0.2 × 84.9 = 17.0 N
4. Net force: 49 - 17 = 32 N
5. Acceleration: a = 32/10 = **3.2 m/s²**

## Explanation Patterns

1. **Always draw a Free Body Diagram** showing all forces including friction
2. **Determine if the object is sliding or stationary** to decide between fs and fk
3. **For inclines, rotate your coordinate system** so x is parallel and y is perpendicular to the surface
4. **Calculate the normal force first** - it's needed for friction calculations
5. **For static friction problems**, first check if the object would slide without friction
6. **Remember**: μ is just a ratio - friction force depends on BOTH μ and N
