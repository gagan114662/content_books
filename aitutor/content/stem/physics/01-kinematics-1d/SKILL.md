---
# === REQUIRED METADATA ===
id: kinematics-1d
subject: physics
display_name: One-Dimensional Kinematics
description: |
  Analyzes motion in one dimension using position, velocity, and acceleration.
  Use when students need to solve constant-acceleration problems, interpret motion
  graphs, or analyze free-fall scenarios.

# === CATEGORIZATION ===
grade_band: 9-12
khan_tags: [physics, kinematics, motion, ap-physics-1]
standards:
  - NGSS.HS-PS2-1
  - CC.HSN-Q.A.1

# === LEARNING STRUCTURE ===
objectives:
  - Define and distinguish position, displacement, velocity, and acceleration
  - Interpret position-time and velocity-time graphs
  - Apply kinematic equations to constant-acceleration problems
  - Solve free-fall problems using g = 9.8 m/s²
  - Identify when to use each kinematic equation based on known quantities

prerequisites:
  - algebra-linear-equations
  - scientific-notation

estimated_time_minutes: 45

# === VALIDATION CONFIG ===
validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

# === SOURCES ===
sources:
  - name: OpenStax College Physics
    chapter: 2
    sections: [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7]
    url: https://openstax.org/books/college-physics/pages/2-introduction
    license: CC-BY-4.0
---

# One-Dimensional Kinematics

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Zero velocity means zero acceleration" | An object at the peak of its trajectory has v=0 but a=g downward. Acceleration is the rate of change of velocity, not velocity itself. |
| "Heavier objects fall faster" | In the absence of air resistance, all objects fall at the same rate (g ≈ 9.8 m/s²). Galileo demonstrated this at the Leaning Tower of Pisa. |
| "Acceleration means speeding up" | Acceleration is any change in velocity—it can mean speeding up, slowing down, or changing direction. Deceleration is just acceleration in the opposite direction of motion. |
| "Distance and displacement are the same" | Distance is the total path length (always positive), while displacement is the change in position (can be positive, negative, or zero). |
| "Average velocity equals average speed" | Average speed is total distance / time, while average velocity is displacement / time. They're equal only for motion in one direction. |

## Key Concepts

### Position and Displacement

**Position** (x) describes where an object is located relative to a chosen origin point.

**Displacement** (Δx) is the change in position:
```
Δx = x_final - x_initial = x₂ - x₁
```

**Key distinction**:
- **Distance** is the total path length traveled (scalar, always ≥ 0)
- **Displacement** is the straight-line change in position (vector, can be +, -, or 0)

*Example*: If you walk 3 m east then 3 m west, your distance is 6 m but your displacement is 0 m.

### Velocity

**Average velocity** is displacement divided by time:
```
v_avg = Δx / Δt = (x₂ - x₁) / (t₂ - t₁)
```

**Instantaneous velocity** is the slope of the position-time graph at a specific moment:
```
v = lim(Δt→0) Δx/Δt = dx/dt
```

**Key insight**: On an x-t graph:
- Steep slope = fast motion
- Positive slope = moving in positive direction
- Negative slope = moving in negative direction
- Zero slope = at rest

### Acceleration

**Average acceleration** is the rate of change of velocity:
```
a_avg = Δv / Δt = (v₂ - v₁) / (t₂ - t₁)
```

**Instantaneous acceleration** is the slope of the velocity-time graph:
```
a = lim(Δt→0) Δv/Δt = dv/dt
```

**Key insight**: On a v-t graph:
- Area under the curve = displacement
- Slope = acceleration
- Horizontal line = constant velocity (zero acceleration)

## Equations

The four kinematic equations for constant acceleration:

```
[1] v = v₀ + at                    (no x)
[2] x = x₀ + v₀t + ½at²            (no v)
[3] v² = v₀² + 2a(x - x₀)          (no t)
[4] x = x₀ + ½(v₀ + v)t            (no a)
```

**Equation Selection Strategy**:
| If you don't have... | Use equation... |
|---------------------|-----------------|
| x (displacement) | [1] |
| v (final velocity) | [2] |
| t (time) | [3] |
| a (acceleration) | [4] |

### Free Fall

Objects in free fall near Earth's surface experience constant acceleration:
```
g = 9.8 m/s² ≈ 10 m/s² (downward)
```

**Sign convention** (standard):
- Upward = positive
- Downward = negative
- Therefore: a = -g = -9.8 m/s²

## Worked Examples

### Example 1: Basic Constant Acceleration

**Problem**: A car accelerates from rest at 3.0 m/s² for 8.0 seconds. How far does it travel?

**Solution**:
1. **Identify knowns and unknowns**:
   - v₀ = 0 m/s (starts from rest)
   - a = 3.0 m/s²
   - t = 8.0 s
   - x₀ = 0 m (choose starting position as origin)
   - Find: x = ?

2. **Select equation**: Need x, have v₀, a, t, don't need v → Use equation [2]

3. **Solve**:
   ```
   x = x₀ + v₀t + ½at²
   x = 0 + (0)(8.0) + ½(3.0)(8.0)²
   x = ½(3.0)(64)
   x = 96 m
   ```

4. **Check**: Units are meters ✓, positive displacement for positive acceleration ✓, reasonable magnitude ✓

**Answer**: 96 m

---

### Example 2: Free Fall - Time to Fall

**Problem**: A ball is dropped from a height of 45 m. How long does it take to hit the ground?

**Solution**:
1. **Identify knowns and unknowns**:
   - y₀ = 45 m (using y for vertical)
   - y = 0 m (ground level)
   - v₀ = 0 m/s (dropped, not thrown)
   - a = -9.8 m/s² (downward)
   - Find: t = ?

2. **Select equation**: Need t, have y, y₀, v₀, a → Use equation [2]

3. **Solve**:
   ```
   y = y₀ + v₀t + ½at²
   0 = 45 + (0)t + ½(-9.8)t²
   -45 = -4.9t²
   t² = 45/4.9 = 9.18
   t = 3.0 s
   ```

4. **Check**: Units are seconds ✓, positive time ✓, reasonable for ~45 m drop ✓

**Answer**: 3.0 s

---

### Example 3: Finding Initial Velocity

**Problem**: A car traveling at unknown speed brakes with deceleration 5.0 m/s² and stops in 40 m. What was its initial speed?

**Solution**:
1. **Identify knowns and unknowns**:
   - v = 0 m/s (stops)
   - a = -5.0 m/s² (deceleration = negative acceleration)
   - Δx = 40 m
   - Find: v₀ = ?

2. **Select equation**: Need v₀, have v, a, Δx, don't need t → Use equation [3]

3. **Solve**:
   ```
   v² = v₀² + 2aΔx
   0² = v₀² + 2(-5.0)(40)
   0 = v₀² - 400
   v₀² = 400
   v₀ = 20 m/s
   ```

4. **Check**: Positive initial velocity ✓, reasonable car speed (~45 mph) ✓

**Answer**: 20 m/s

## Explanation Patterns

When teaching kinematics, follow this sequence:

### For Conceptual Questions
1. Start with physical intuition (real-world example)
2. Connect to the mathematical representation
3. Verify with limiting cases (what happens when v→0, t→∞, etc.)
4. Address common misconceptions explicitly

### For Problem Solving
1. **Draw a diagram** with coordinate system and sign conventions
2. **List knowns and unknowns** explicitly (including units)
3. **Identify which kinematic equation** to use based on what's missing
4. **Solve algebraically first** - keep symbols until the last step
5. **Substitute numbers** with units
6. **Check**:
   - Are units correct?
   - Is the sign reasonable?
   - Is the magnitude physically sensible?

### For Graph Interpretation
1. Identify what's on each axis (x-t, v-t, or a-t)
2. For x-t: slope = velocity, curvature = acceleration
3. For v-t: slope = acceleration, area = displacement
4. For a-t: area = change in velocity

## When to Use This Skill

Use kinematics when:
- Motion is in **one dimension** (straight line)
- Acceleration is **constant** (or zero)
- You need to find **position, velocity, time, or acceleration**
- Problems involve **free fall** or **projectile motion** (vertical component)

Do NOT use kinematics when:
- Acceleration changes over time (need calculus or numerical methods)
- Forces are the focus (use Newton's laws first, then kinematics)
- Motion is circular (use circular motion equations)

## Advanced Topics

For deeper exploration:
- [references/calculus-kinematics.md] - Calculus-based derivations of kinematic equations
- [references/relative-motion.md] - Reference frames and relative velocity
- [references/motion-graphs.md] - Detailed graph interpretation strategies

## Resources

- **Textbook**: OpenStax College Physics, Chapter 2
- **Video**: Khan Academy - One-dimensional motion
- **Simulation**: PhET "The Moving Man" - https://phet.colorado.edu/en/simulation/moving-man
- **Practice**: OpenStax Chapter 2 end-of-chapter problems
