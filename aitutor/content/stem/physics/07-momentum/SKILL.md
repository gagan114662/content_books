---
id: momentum
subject: physics
display_name: Momentum and Collisions
description: |
  Analyzes momentum, impulse, and collision problems using conservation principles.
  Use when students need to solve problems involving momentum conservation, impulse, or elastic/inelastic collisions.

grade_band: 9-12
khan_tags: [physics, momentum, impulse, collisions, conservation]
standards:
  - NGSS.HS-PS2-2
  - NGSS.HS-PS2-3

objectives:
  - Calculate momentum and impulse
  - Apply the impulse-momentum theorem
  - Apply conservation of momentum to collision problems
  - Distinguish between elastic and inelastic collisions
  - Solve 2D collision problems
  - Analyze explosions and recoil

prerequisites:
  - newtons-laws
  - energy-work
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
    chapter: 8
    url: https://openstax.org/books/college-physics/pages/8-introduction-to-linear-momentum-and-collisions
    license: CC-BY-4.0
---

# Momentum and Collisions

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Heavier objects have more momentum" | Momentum depends on both mass AND velocity: p = mv |
| "Momentum is the same as kinetic energy" | Momentum is a vector (p = mv), KE is a scalar (½mv²); they're conserved differently |
| "In a collision, the heavier object always wins" | Momentum is always conserved; the lighter object changes velocity more |
| "Momentum is always conserved" | Momentum is conserved only when external forces are negligible |
| "Elastic collisions conserve energy, inelastic don't" | Both conserve momentum; elastic also conserves KE, inelastic doesn't |

## Key Concepts

### Momentum
Momentum is mass times velocity:
- **p = mv**
- Vector quantity (has direction)
- Unit: kg·m/s (no special name)
- Total momentum of a system: **p_total = Σmᵢvᵢ**

### Impulse
Impulse is the change in momentum caused by a force:
- **J = FΔt = Δp = p_f - p_i**
- Vector quantity
- Unit: N·s = kg·m/s
- Area under F-t graph equals impulse

### Impulse-Momentum Theorem
The impulse equals the change in momentum:
- **FΔt = mΔv = mv_f - mv_i**
- Derived from Newton's second law: F = ma = m(Δv/Δt)

### Conservation of Momentum
In an isolated system (no external forces), total momentum is conserved:
- **Σp_before = Σp_after**
- m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f

### Types of Collisions

**Elastic Collision**:
- Momentum is conserved
- Kinetic energy is conserved
- Objects bounce off each other
- Examples: billiard balls, atomic collisions

**Inelastic Collision**:
- Momentum is conserved
- Kinetic energy is NOT conserved (some converts to heat, sound, deformation)
- Most real collisions are inelastic

**Perfectly Inelastic Collision**:
- Objects stick together after collision
- Maximum KE loss (consistent with momentum conservation)
- m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)v_f

### Center of Mass
The point where total mass can be considered concentrated:
- x_cm = (m₁x₁ + m₂x₂)/(m₁ + m₂)
- Velocity of center of mass: v_cm = (m₁v₁ + m₂v₂)/(m₁ + m₂)
- In isolated system, v_cm is constant

## Equations

```
[1] p = mv (momentum)
[2] J = FΔt = Δp (impulse)
[3] m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f (conservation of momentum)
[4] (m₁ + m₂)v_f = m₁v₁ᵢ + m₂v₂ᵢ (perfectly inelastic)
[5] ½m₁v₁ᵢ² + ½m₂v₂ᵢ² = ½m₁v₁f² + ½m₂v₂f² (elastic collision, KE conserved)
[6] v₁f = ((m₁-m₂)/(m₁+m₂))v₁ᵢ + (2m₂/(m₁+m₂))v₂ᵢ (elastic collision formula)
[7] v_cm = (m₁v₁ + m₂v₂)/(m₁ + m₂) (center of mass velocity)
```

## Worked Examples

### Example 1: Impulse
**Problem**: A 0.15 kg baseball moving at 40 m/s is hit by a bat and leaves at 50 m/s in the opposite direction. What impulse did the bat deliver?

**Solution**:
1. Define positive direction as initial ball direction
2. Initial momentum: p_i = 0.15 × 40 = 6 kg·m/s
3. Final momentum: p_f = 0.15 × (-50) = -7.5 kg·m/s
4. Impulse: J = p_f - p_i = -7.5 - 6 = **-13.5 kg·m/s** (or 13.5 kg·m/s toward the pitcher)

### Example 2: Perfectly Inelastic Collision
**Problem**: A 1000 kg car moving at 20 m/s collides with a 2000 kg truck at rest. They stick together. Find the final velocity.

**Solution**:
1. Conservation of momentum: m₁v₁ + m₂v₂ = (m₁ + m₂)v_f
2. 1000(20) + 2000(0) = (1000 + 2000)v_f
3. 20000 = 3000v_f
4. v_f = **6.67 m/s**

### Example 3: Elastic Collision (1D)
**Problem**: A 2 kg ball moving at 5 m/s collides elastically with a 3 kg ball at rest. Find both final velocities.

**Solution**:
1. Using elastic collision formulas:
2. v₁f = ((m₁-m₂)/(m₁+m₂))v₁ᵢ = ((2-3)/(2+3)) × 5 = (-1/5) × 5 = **-1 m/s**
3. v₂f = (2m₁/(m₁+m₂))v₁ᵢ = (2×2/(2+3)) × 5 = (4/5) × 5 = **4 m/s**
4. Check: momentum and KE should be conserved

## Explanation Patterns

1. **Define a coordinate system** and positive direction
2. **Identify the system** - what objects are involved?
3. **Check for external forces** - if negligible, momentum is conserved
4. **Determine collision type**: elastic (both p and KE conserved) or inelastic (only p conserved)
5. **Write conservation equations** for each direction
6. **For 2D problems**, use vector components
7. **Check your answer**: total momentum before = total momentum after

## Common Problem Types

1. **Impulse**: FΔt = Δp, finding force from momentum change
2. **Inelastic collision**: Objects stick together, find final velocity
3. **Elastic collision**: Both momentum and KE conserved
4. **Recoil/explosion**: Initially at rest, objects separate
5. **2D collision**: Use vector components, conserve p_x and p_y separately
6. **Ballistic pendulum**: Collision + energy conservation
