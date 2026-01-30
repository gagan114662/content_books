---
id: circular-motion
subject: physics
display_name: Circular Motion
description: |
  Analyzes objects moving in circular paths including centripetal acceleration and force.
  Use when students need to solve problems involving circular motion, centripetal force, or orbital mechanics.

grade_band: 9-12
khan_tags: [physics, circular-motion, centripetal-force, orbits]
standards:
  - NGSS.HS-PS2-1

objectives:
  - Define centripetal acceleration and its direction
  - Calculate centripetal force using F = mv²/r
  - Solve problems involving horizontal and vertical circular motion
  - Apply circular motion concepts to orbital mechanics
  - Analyze banked curves and conical pendulums

prerequisites:
  - newtons-laws
  - kinematics-2d

estimated_time_minutes: 60

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 6
    url: https://openstax.org/books/college-physics/pages/6-introduction-to-uniform-circular-motion-and-gravitation
    license: CC-BY-4.0
---

# Circular Motion

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "There's a centrifugal force pushing objects outward" | Centrifugal force is fictitious; objects feel pushed outward due to inertia |
| "Centripetal force is a new type of force" | Centripetal force is any force that causes circular motion (tension, gravity, friction, normal force) |
| "Objects in circular motion are in equilibrium" | Objects in circular motion are accelerating toward the center |
| "Faster motion means larger radius" | For constant centripetal force, faster motion requires smaller radius (or more force) |
| "Satellites are not falling" | Satellites are continuously falling but moving forward fast enough to miss Earth |

## Key Concepts

### Uniform Circular Motion
Motion in a circle at constant speed. Even though speed is constant, velocity is changing (direction changes), so there is acceleration.

**Key insight**: The acceleration is always directed toward the center of the circle.

### Centripetal Acceleration
- Magnitude: a_c = v²/r = ω²r = 4π²r/T²
- Direction: Always toward the center of the circle
- v = linear (tangential) speed
- r = radius of circular path
- ω = angular velocity (rad/s)
- T = period (time for one revolution)

### Centripetal Force
- The net force required to keep an object moving in a circle
- F_c = ma_c = mv²/r
- This is NOT a new force—it's the name for whatever force provides the centripetal acceleration
- Examples: tension (ball on string), friction (car turning), gravity (orbits), normal force (loop)

### Period and Frequency
- Period (T): Time for one complete revolution
- Frequency (f): Number of revolutions per second, f = 1/T
- Angular velocity: ω = 2π/T = 2πf
- Linear speed: v = 2πr/T = ωr

## Equations

```
[1] a_c = v²/r (centripetal acceleration)
[2] a_c = ω²r (using angular velocity)
[3] F_c = mv²/r (centripetal force)
[4] v = 2πr/T (speed from period)
[5] ω = 2π/T = 2πf (angular velocity)
[6] v = ωr (relating linear and angular speed)
[7] F_gravity = GMm/r² (gravitational force)
[8] v_orbit = √(GM/r) (orbital velocity)
```

## Worked Examples

### Example 1: Car on a Curve
**Problem**: A 1500 kg car travels around a flat curve of radius 50 m at 15 m/s. What friction force is required?

**Solution**:
1. The friction force provides the centripetal force
2. F_c = mv²/r = 1500 × (15)² / 50
3. F_c = 1500 × 225 / 50 = **6750 N**
4. Check: This is the friction needed; compare to μmg to see if it's possible

### Example 2: Ball on a String (Vertical Circle)
**Problem**: A 0.5 kg ball on a 1.2 m string swings in a vertical circle. What minimum speed is needed at the top of the circle?

**Solution**:
1. At the top, both gravity and tension point toward center
2. At minimum speed, tension = 0, so gravity alone provides centripetal force
3. mg = mv²/r → v² = gr
4. v = √(gr) = √(9.8 × 1.2) = √11.76 = **3.43 m/s**

### Example 3: Orbital Speed
**Problem**: A satellite orbits Earth at altitude 400 km. Find its orbital speed. (Earth radius = 6.37 × 10⁶ m, Earth mass = 5.97 × 10²⁴ kg)

**Solution**:
1. Orbital radius: r = R_Earth + altitude = 6.37 × 10⁶ + 4 × 10⁵ = 6.77 × 10⁶ m
2. Gravity provides centripetal force: GMm/r² = mv²/r
3. v = √(GM/r) = √(6.67 × 10⁻¹¹ × 5.97 × 10²⁴ / 6.77 × 10⁶)
4. v = √(5.88 × 10⁷) = **7670 m/s** ≈ 7.67 km/s

## Explanation Patterns

1. **Identify the source of centripetal force** - What force (or forces) point toward the center?
2. **Draw a free body diagram** at the position of interest (top, bottom, side of circle)
3. **Set up F_net = ma_c** with forces toward center as positive
4. **Be careful at top vs. bottom of vertical circles** - weight and normal/tension may add or subtract
5. **For orbits, equate gravitational force to centripetal force**
6. **Check if the required friction is reasonable** - compare to μmg

## Common Problem Types

1. **Horizontal circles**: Friction or tension provides centripetal force
2. **Vertical circles**: Analyze at top and bottom separately
3. **Banked curves**: Normal force has a horizontal component
4. **Conical pendulum**: Horizontal component of tension provides centripetal force
5. **Satellites/orbits**: Gravity provides centripetal force
6. **Loop-the-loop**: Find minimum speed at top where normal force = 0
