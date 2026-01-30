---
id: rotational-motion
subject: physics
display_name: Rotational Motion
description: |
  Analyzes rotational kinematics, torque, moment of inertia, and rotational energy.
  Use when students need to solve problems involving rotating objects, torque, angular momentum, or rolling motion.

grade_band: 9-12
khan_tags: [physics, rotational-motion, torque, moment-of-inertia, angular-momentum]
standards:
  - NGSS.HS-PS2-1

objectives:
  - Relate angular displacement, velocity, and acceleration
  - Apply rotational kinematic equations
  - Calculate torque using τ = rF sin(θ)
  - Determine moment of inertia for common shapes
  - Calculate rotational kinetic energy using KE = ½Iω²
  - Apply conservation of angular momentum
  - Analyze rolling motion combining translation and rotation

prerequisites:
  - circular-motion
  - energy-work

estimated_time_minutes: 60

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 10
    url: https://openstax.org/books/college-physics/pages/10-introduction-to-rotational-motion-and-angular-momentum
    license: CC-BY-4.0
---

# Rotational Motion

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Angular velocity and linear velocity are the same" | Angular velocity (ω) is rotation rate in rad/s; linear velocity (v = ωr) depends on distance from axis |
| "Torque is the same as force" | Torque is the rotational effect of a force; it depends on force, distance from axis, and angle |
| "All objects with the same mass have the same moment of inertia" | Moment of inertia depends on mass distribution; mass farther from axis increases I |
| "A rolling object only has translational KE" | Rolling objects have both translational KE (½mv²) and rotational KE (½Iω²) |
| "Angular momentum is always conserved" | Angular momentum is conserved only when net external torque is zero |
| "Heavier objects are harder to rotate" | Moment of inertia, not mass alone, determines rotational resistance |

## Key Concepts

### Angular Kinematics
Rotational motion uses angular quantities analogous to linear motion:

| Linear | Angular | Relationship |
|--------|---------|--------------|
| Displacement (x) | Angular displacement (θ) | θ in radians |
| Velocity (v) | Angular velocity (ω) | v = ωr |
| Acceleration (a) | Angular acceleration (α) | a_tangential = αr |

**Key conversions**:
- 1 revolution = 2π radians = 360°
- ω (rad/s) = 2π × frequency (Hz) = 2π/T

### Angular Velocity
- Average: ω_avg = Δθ/Δt
- Instantaneous: ω = dθ/dt
- Direction: Right-hand rule (curl fingers in rotation direction, thumb points along ω)
- Unit: rad/s

### Angular Acceleration
- Average: α_avg = Δω/Δt
- Instantaneous: α = dω/dt
- Positive α means speeding up (if ω positive) or slowing down (if ω negative)
- Unit: rad/s²

### Rotational Kinematic Equations
For constant angular acceleration (analogous to linear kinematics):

| Linear | Rotational |
|--------|-----------|
| v = v₀ + at | ω = ω₀ + αt |
| x = x₀ + v₀t + ½at² | θ = θ₀ + ω₀t + ½αt² |
| v² = v₀² + 2a(x - x₀) | ω² = ω₀² + 2α(θ - θ₀) |
| x = x₀ + ½(v₀ + v)t | θ = θ₀ + ½(ω₀ + ω)t |

### Torque
Torque is the rotational equivalent of force:
- **τ = rF sin(θ)** where θ is the angle between r and F
- Equivalently: τ = r × F (cross product)
- τ = r_⊥ × F = r × F_⊥ (lever arm form)
- Unit: N·m (not Joules, though same dimensions)
- Sign: positive for counterclockwise, negative for clockwise

**Key insight**: Torque = (lever arm) × (force) where lever arm is perpendicular distance from axis to line of action of force.

### Moment of Inertia
Moment of inertia (I) is the rotational analog of mass:
- Measures resistance to angular acceleration
- **I = Σmᵢrᵢ²** (discrete masses)
- Depends on axis of rotation
- Unit: kg·m²

**Common moments of inertia** (about central axis unless noted):

| Shape | Moment of Inertia |
|-------|------------------|
| Point mass at radius r | I = mr² |
| Solid cylinder/disk | I = ½MR² |
| Hollow cylinder/ring | I = MR² |
| Solid sphere | I = ⅖MR² |
| Hollow sphere | I = ⅔MR² |
| Thin rod (center) | I = (1/12)ML² |
| Thin rod (end) | I = ⅓ML² |

**Parallel Axis Theorem**: I = I_cm + Md² (d = distance from center of mass to new axis)

### Newton's Second Law for Rotation
- **τ_net = Iα**
- Analogous to F_net = ma

### Rotational Kinetic Energy
- **KE_rot = ½Iω²**
- Analogous to KE_trans = ½mv²
- For rolling without slipping: KE_total = ½mv² + ½Iω² with v = ωR

### Angular Momentum
- **L = Iω** (for rigid body rotating about fixed axis)
- Unit: kg·m²/s
- Vector quantity (direction from right-hand rule)

### Conservation of Angular Momentum
When net external torque is zero:
- **L_initial = L_final**
- I₁ω₁ = I₂ω₂
- Examples: ice skater spin, collapsing star, diver's tuck

### Rolling Motion
For rolling without slipping:
- **v_cm = ωR** (constraint condition)
- **a_cm = αR**
- Friction provides torque but does no work (contact point instantaneously at rest)
- Total KE = ½mv² + ½Iω² = ½mv²(1 + I/(mR²))

## Equations

```
[1] ω = ω₀ + αt (angular velocity)
[2] θ = θ₀ + ω₀t + ½αt² (angular displacement)
[3] ω² = ω₀² + 2α(θ - θ₀) (angular velocity-displacement)
[4] τ = rF sin(θ) (torque)
[5] τ_net = Iα (Newton's 2nd law for rotation)
[6] I = Σmᵢrᵢ² (moment of inertia)
[7] KE_rot = ½Iω² (rotational kinetic energy)
[8] L = Iω (angular momentum)
[9] I₁ω₁ = I₂ω₂ (conservation of angular momentum)
[10] v = ωR (rolling constraint)
```

## Worked Examples

### Example 1: Angular Kinematics
**Problem**: A wheel accelerates uniformly from rest to 150 rad/s in 5 seconds. (a) What is the angular acceleration? (b) How many revolutions does it make?

**Solution**:
1. Given: ω₀ = 0, ω = 150 rad/s, t = 5 s
2. (a) α = (ω - ω₀)/t = (150 - 0)/5 = **30 rad/s²**
3. (b) θ = ω₀t + ½αt² = 0 + ½(30)(5)² = 375 rad
4. Revolutions = 375/(2π) = **59.7 revolutions**

### Example 2: Torque Calculation
**Problem**: A 40 N force is applied at the end of a 0.5 m wrench at 60° to the handle. What torque is produced?

**Solution**:
1. τ = rF sin(θ)
2. τ = 0.5 × 40 × sin(60°) = 0.5 × 40 × 0.866
3. τ = **17.3 N·m**

### Example 3: Rotational Dynamics
**Problem**: A solid disk of mass 4 kg and radius 0.2 m has a cord wrapped around it. If 10 N tension is applied, what is the angular acceleration?

**Solution**:
1. Moment of inertia: I = ½MR² = ½(4)(0.2)² = 0.08 kg·m²
2. Torque: τ = TR = 10 × 0.2 = 2 N·m
3. τ = Iα → α = τ/I = 2/0.08 = **25 rad/s²**

### Example 4: Rolling Down an Incline
**Problem**: A solid sphere of mass 2 kg and radius 0.1 m rolls without slipping down a 3 m high incline. What is its speed at the bottom?

**Solution**:
1. For solid sphere: I = ⅖MR², so I/(MR²) = 2/5
2. Energy conservation: Mgh = ½Mv² + ½Iω²
3. With v = ωR: Mgh = ½Mv² + ½(⅖MR²)(v/R)² = ½Mv² + ⅕Mv² = (7/10)Mv²
4. v² = (10/7)gh = (10/7)(9.8)(3) = 42
5. v = **6.48 m/s**

### Example 5: Conservation of Angular Momentum
**Problem**: An ice skater with arms extended has I = 4.5 kg·m² and spins at 2 rev/s. When she pulls in her arms, I = 1.5 kg·m². What is her new spin rate?

**Solution**:
1. Conservation: I₁ω₁ = I₂ω₂
2. ω₁ = 2 rev/s = 4π rad/s
3. ω₂ = I₁ω₁/I₂ = (4.5 × 4π)/1.5 = 12π rad/s
4. ω₂ = 12π/(2π) = **6 rev/s**

## Explanation Patterns

1. **Identify the axis of rotation** - All angular quantities are defined relative to this axis
2. **Draw an extended free body diagram** - Show where forces act, not just at center of mass
3. **Calculate torques** - Use τ = rF sin(θ) or lever arm method; include signs
4. **Apply τ_net = Iα** for rotational dynamics
5. **For rolling problems**, use both F = ma and τ = Iα with the constraint v = ωR
6. **For energy problems**, include both translational and rotational KE
7. **Check for angular momentum conservation** - Is external torque zero?

## Common Problem Types

1. **Angular kinematics**: Use rotational equations analogous to linear kinematics
2. **Torque calculation**: Find τ = rF sin(θ) for individual forces
3. **Rotational dynamics**: Apply τ_net = Iα with correct I for the shape
4. **Rotational energy**: Include KE_rot = ½Iω² in energy conservation
5. **Rolling motion**: Combine translation and rotation with v = ωR
6. **Angular momentum conservation**: I₁ω₁ = I₂ω₂ when τ_external = 0
7. **Atwood machine with pulley**: Include pulley's I in the analysis
