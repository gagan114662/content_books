---
id: kinematics-2d
subject: physics
display_name: Two-Dimensional Kinematics
description: |
  Analyzes motion in two dimensions including projectile motion and relative velocity.
  Use when students need to decompose vectors, solve projectile problems, or work with relative motion.

grade_band: 9-12
khan_tags: [physics, kinematics, projectile-motion, vectors]
standards:
  - NGSS.HS-PS2-1
  - CC.HSN-VM.A.1
  - CC.HSN-VM.B.4

objectives:
  - Decompose vectors into x and y components
  - Apply kinematic equations independently to horizontal and vertical motion
  - Solve projectile motion problems for range, max height, and time of flight
  - Analyze relative velocity problems in two dimensions

prerequisites:
  - kinematics-1d
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
    chapter: 3
    url: https://openstax.org/books/college-physics/pages/3-introduction-to-two-dimensional-kinematics
    license: CC-BY-4.0
---

# Two-Dimensional Kinematics

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Horizontal and vertical motions affect each other" | Horizontal and vertical motions are independent; a bullet fired horizontally hits ground same time as one dropped |
| "Objects moving horizontally don't fall" | Gravity acts on all objects equally regardless of horizontal motion |
| "Projectiles slow down at the top of their arc" | Horizontal velocity is constant; only vertical velocity becomes zero at peak |
| "Thrown objects have a force pushing them forward" | After release, only gravity acts (ignoring air resistance) |
| "Range is maximum at 90°" | Maximum range occurs at 45° launch angle |

## Key Concepts

### Vector Components
Any vector **v** can be decomposed into perpendicular components:
- Horizontal: v_x = v × cos(θ)
- Vertical: v_y = v × sin(θ)
- Magnitude: v = √(v_x² + v_y²)
- Direction: θ = tan⁻¹(v_y / v_x)

### Independence of Motion
Projectile motion can be analyzed as two separate 1D problems:
- **Horizontal**: constant velocity (a_x = 0)
- **Vertical**: constant acceleration (a_y = -g = -9.8 m/s²)

The same time t applies to both directions.

### Projectile Motion Equations

**Horizontal motion** (a_x = 0):
```
x = x₀ + v₀ₓt
v_x = v₀ₓ = v₀ cos(θ)
```

**Vertical motion** (a_y = -g):
```
y = y₀ + v₀ᵧt - ½gt²
v_y = v₀ᵧ - gt
v_y² = v₀ᵧ² - 2g(y - y₀)
```

### Key Projectile Formulas (launched from ground level)

```
[1] Time of flight: T = 2v₀sin(θ)/g
[2] Maximum height: H = v₀²sin²(θ)/(2g)
[3] Range: R = v₀²sin(2θ)/g
[4] At any time t: x = v₀cos(θ)t, y = v₀sin(θ)t - ½gt²
```

### Relative Velocity
Velocity of object A relative to object B:
```
v_AB = v_A - v_B
```

For perpendicular velocities (boat crossing river):
- Resultant velocity: v = √(v_boat² + v_river²)
- Drift distance: d = v_river × t_crossing

## Worked Examples

### Example 1: Horizontal Projectile
**Problem**: A ball is thrown horizontally at 15 m/s from a cliff 45 m high. How far from the base does it land?

**Solution**:
1. Find time to fall (vertical motion):
   - y = y₀ - ½gt²
   - 0 = 45 - ½(9.8)t²
   - t = √(90/9.8) = 3.03 s

2. Find horizontal distance:
   - x = v₀ₓ × t = 15 × 3.03 = **45.5 m**

### Example 2: Angled Launch
**Problem**: A soccer ball is kicked at 20 m/s at 30° above horizontal. Find the range.

**Solution**:
1. Use range formula: R = v₀²sin(2θ)/g
2. R = (20)²sin(60°)/9.8
3. R = 400 × 0.866/9.8 = **35.3 m**

### Example 3: River Crossing
**Problem**: A boat travels at 4 m/s in still water. The river flows at 3 m/s. If the boat aims straight across a 100 m wide river, find the drift downstream.

**Solution**:
1. Time to cross: t = width/v_boat = 100/4 = 25 s
2. Drift: d = v_river × t = 3 × 25 = **75 m**

## Explanation Patterns

1. **Always start with a diagram** showing coordinate axes, initial velocity vector, and trajectory
2. **Decompose initial velocity** into v₀ₓ and v₀ᵧ immediately
3. **Write separate equations** for x and y motion
4. **Identify what connects them**: usually time t
5. **Solve for time** from whichever equation has enough information
6. **Substitute time** into the other equation to find the unknown
7. **Check units and reasonableness**: distances in meters, times in seconds

## Common Problem Types

1. **Horizontal launch**: v₀ᵧ = 0, find range or time
2. **Angled launch from ground**: find range, max height, or time of flight
3. **Angled launch from height**: combines both
4. **River/wind problems**: relative velocity with perpendicular components
5. **Find launch angle**: given range and initial speed
