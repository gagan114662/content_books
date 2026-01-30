---
id: energy-work
subject: physics
display_name: Work and Energy
description: |
  Analyzes energy transformations and applies work-energy theorem to solve mechanics problems.
  Use when students need to solve problems involving kinetic energy, potential energy, work, or power.

grade_band: 9-12
khan_tags: [physics, energy, work, conservation-of-energy, power]
standards:
  - NGSS.HS-PS3-1
  - NGSS.HS-PS3-2

objectives:
  - Calculate work done by constant and variable forces
  - Apply the work-energy theorem
  - Calculate kinetic and potential energy
  - Apply conservation of mechanical energy
  - Solve problems involving non-conservative forces
  - Calculate power and efficiency

prerequisites:
  - newtons-laws
  - forces-friction
  - kinematics-1d

estimated_time_minutes: 75

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 7
    url: https://openstax.org/books/college-physics/pages/7-introduction-to-work-energy-and-energy-resources
    license: CC-BY-4.0
---

# Work and Energy

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "If I push hard but nothing moves, I did work" | Work requires displacement; W = Fd cos(θ). No displacement = no work |
| "Energy is a force" | Energy is a scalar quantity representing capacity to do work; force is a vector |
| "Heavier objects have more kinetic energy" | KE depends on both mass AND velocity: KE = ½mv². A fast light object can have more KE |
| "Potential energy is energy that might be used" | PE is stored energy due to position or configuration; it's real energy, not hypothetical |
| "Conservation of energy means energy never changes" | Total energy is conserved, but it transforms between types (KE ↔ PE ↔ thermal) |

## Key Concepts

### Work
Work is energy transferred by a force acting through a displacement.

**For constant force**:
- W = F · d = Fd cos(θ)
- θ is the angle between force and displacement
- Work can be positive (force in direction of motion) or negative (opposite)
- Unit: Joule (J) = N·m = kg·m²/s²

**Special cases**:
- Force parallel to motion: W = Fd
- Force perpendicular to motion: W = 0
- Force opposite to motion: W = -Fd

### Kinetic Energy
Energy of motion:
- KE = ½mv²
- Always positive (mass and v² are both positive)
- Depends on reference frame

### Work-Energy Theorem
The net work done on an object equals its change in kinetic energy:
- W_net = ΔKE = ½mv_f² - ½mv_i²

### Potential Energy
Energy stored due to position or configuration:

**Gravitational PE**:
- PE_g = mgh (near Earth's surface)
- PE_g = -GMm/r (general formula)
- Reference point is arbitrary but must be consistent

**Elastic PE** (spring):
- PE_s = ½kx²
- k = spring constant (N/m)
- x = displacement from equilibrium

### Conservation of Mechanical Energy
If only conservative forces do work:
- E_total = KE + PE = constant
- KE_i + PE_i = KE_f + PE_f

**Conservative forces**: gravity, spring force, electric force
**Non-conservative forces**: friction, air resistance, applied forces

### Work by Non-Conservative Forces
When friction or other non-conservative forces are present:
- W_nc = ΔKE + ΔPE = ΔE_mechanical
- Energy "lost" to friction becomes thermal energy

### Power
Rate of doing work or energy transfer:
- P = W/t = ΔE/t
- P = Fv (instantaneous power)
- Unit: Watt (W) = J/s

## Equations

```
[1] W = Fd cos(θ) (work by constant force)
[2] KE = ½mv² (kinetic energy)
[3] W_net = ΔKE = ½mv_f² - ½mv_i² (work-energy theorem)
[4] PE_g = mgh (gravitational potential energy)
[5] PE_s = ½kx² (elastic potential energy)
[6] KE_i + PE_i = KE_f + PE_f (conservation of energy)
[7] W_nc = ΔKE + ΔPE (work by non-conservative forces)
[8] P = W/t = Fv (power)
```

## Worked Examples

### Example 1: Work-Energy Theorem
**Problem**: A 5 kg box initially at rest is pushed with 40 N for 3 m on a frictionless surface. What is its final speed?

**Solution**:
1. Work done: W = Fd = 40 × 3 = 120 J
2. Work-energy theorem: W = ½mv_f² - ½mv_i²
3. 120 = ½(5)v_f² - 0
4. v_f² = 240/5 = 48
5. v_f = **6.93 m/s**

### Example 2: Conservation of Energy
**Problem**: A 2 kg ball is dropped from 10 m. What is its speed just before hitting the ground?

**Solution**:
1. Initial: KE_i = 0, PE_i = mgh = 2 × 9.8 × 10 = 196 J
2. Final: KE_f = ½mv_f², PE_f = 0
3. Conservation: KE_i + PE_i = KE_f + PE_f
4. 0 + 196 = ½(2)v_f² + 0
5. v_f = √(196) = **14 m/s**

### Example 3: Spring Energy
**Problem**: A spring (k = 500 N/m) compressed 0.2 m launches a 0.5 kg ball. How high does it rise?

**Solution**:
1. Initial PE_spring = ½kx² = ½(500)(0.2)² = 10 J
2. All spring PE converts to gravitational PE
3. mgh = 10 J
4. h = 10/(0.5 × 9.8) = **2.04 m**

## Explanation Patterns

1. **Identify the system** and determine if energy is conserved (are there non-conservative forces?)
2. **Choose a reference point** for potential energy (usually ground level or lowest point)
3. **Identify initial and final states** - what types of energy exist at each?
4. **Apply the appropriate energy equation**:
   - No friction: KE_i + PE_i = KE_f + PE_f
   - With friction: KE_i + PE_i + W_nc = KE_f + PE_f
5. **Check your answer**: Does the energy accounting make sense?

## Common Problem Types

1. **Free fall**: PE converts to KE (or vice versa for upward motion)
2. **Inclined plane**: Component of gravity does work, PE changes with height
3. **Spring problems**: Elastic PE converts to KE or gravitational PE
4. **Friction problems**: Mechanical energy decreases by work done against friction
5. **Power problems**: Calculate rate of energy transfer or work done
6. **Pendulum**: PE and KE exchange at different positions
