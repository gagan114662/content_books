---
id: magnetism
subject: physics
display_name: Magnetism
description: |
  Covers magnetic fields, magnetic forces on moving charges and current-carrying wires, and electromagnetic induction.
  Use when students need to solve problems involving magnetic forces, field calculations, or Faraday's law.

grade_band: 9-12
khan_tags: [physics, magnetism, magnetic-force, electromagnetic-induction, faraday-law]
standards:
  - NGSS.HS-PS2-5
  - NGSS.HS-PS3-5

objectives:
  - Calculate magnetic force on a moving charge using F = qvB sin(theta)
  - Apply the right-hand rule to determine force direction
  - Calculate force on a current-carrying wire using F = BIL
  - Determine magnetic field from a long straight wire using B = mu_0 I / (2 pi r)
  - Understand magnetic field in solenoids
  - Apply Faraday's law to calculate induced EMF
  - Use Lenz's law to determine direction of induced current

prerequisites:
  - circuits
  - circular-motion

estimated_time_minutes: 75

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 22-23
    url: https://openstax.org/books/college-physics/pages/22-introduction-to-magnetism
    license: CC-BY-4.0
---

# Magnetism

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Magnetic force does work on charged particles" | Magnetic force is always perpendicular to velocity, so it does zero work |
| "Magnetic poles can be isolated" | Magnetic poles always come in north-south pairs; no magnetic monopoles exist |
| "Current flows through a magnetic field to create force" | Force arises from the interaction of moving charges with the magnetic field |
| "Induced EMF depends on the magnetic flux" | Induced EMF depends on the rate of change of flux, not the flux itself |
| "Lenz's law creates energy" | Lenz's law opposes change and is consistent with energy conservation |

## Key Concepts

### Magnetic Field
A magnetic field **B** is a vector field that exerts forces on moving charges. Magnetic field lines point from north to south poles outside the magnet and form closed loops.

**Units**: Tesla (T) = kg/(A·s²) = Wb/m²

### Magnetic Force on a Moving Charge
A charge q moving with velocity v in a magnetic field B experiences a force:

**F = qvB sin(θ)**

Where θ is the angle between v and B.

**Key properties**:
- Force is perpendicular to both v and B
- Force is zero when v is parallel to B
- Use the right-hand rule: fingers point in v direction, curl toward B, thumb points in F direction (for positive charges)
- For negative charges, force is opposite to right-hand rule

### Magnetic Force on a Current-Carrying Wire
A wire of length L carrying current I in a magnetic field B experiences a force:

**F = BIL sin(θ)**

Where θ is the angle between the wire and B.

### Circular Motion in a Magnetic Field
Since magnetic force is always perpendicular to velocity, a charged particle in a uniform magnetic field moves in a circle (or helix if there's a component parallel to B).

**Radius of circular path**: r = mv/(qB)

**Period**: T = 2πm/(qB) (independent of speed!)

### Magnetic Field from a Long Straight Wire
A long straight wire carrying current I produces a magnetic field at distance r:

**B = μ₀I/(2πr)**

Where μ₀ = 4π × 10⁻⁷ T·m/A is the permeability of free space.

**Direction**: Use right-hand rule - thumb in current direction, fingers curl in direction of B.

### Magnetic Field in a Solenoid
A solenoid with n turns per unit length carrying current I produces a uniform field inside:

**B = μ₀nI**

The field is nearly uniform inside and approximately zero outside.

### Faraday's Law of Induction
The induced EMF in a loop equals the negative rate of change of magnetic flux:

**EMF = -N × (ΔΦ/Δt)**

Where Φ = BA cos(θ) is the magnetic flux, N is the number of turns.

### Lenz's Law
The direction of induced current creates a magnetic field that opposes the change in flux that produced it.

## Equations

```
[1] F = qvB sin(θ) (magnetic force on moving charge)
[2] F = BIL sin(θ) (force on current-carrying wire)
[3] r = mv/(qB) (radius of circular motion)
[4] T = 2πm/(qB) (period of circular motion)
[5] B = μ₀I/(2πr) (field from long wire)
[6] B = μ₀nI (field in solenoid)
[7] Φ = BA cos(θ) (magnetic flux)
[8] EMF = -N(ΔΦ/Δt) (Faraday's law)
[9] μ₀ = 4π × 10⁻⁷ T·m/A (permeability of free space)
```

## Worked Examples

### Example 1: Force on a Moving Proton
**Problem**: A proton (q = 1.6 × 10⁻¹⁹ C) moves at 3 × 10⁶ m/s perpendicular to a 0.5 T magnetic field. What is the magnetic force?

**Solution**:
1. Use F = qvB sin(θ) with θ = 90°
2. F = (1.6 × 10⁻¹⁹)(3 × 10⁶)(0.5)(1)
3. F = **2.4 × 10⁻¹³ N**

### Example 2: Circular Motion of an Electron
**Problem**: An electron (m = 9.11 × 10⁻³¹ kg, q = 1.6 × 10⁻¹⁹ C) moves at 2 × 10⁷ m/s in a 0.01 T field. Find the radius of its circular path.

**Solution**:
1. Use r = mv/(qB)
2. r = (9.11 × 10⁻³¹)(2 × 10⁷) / [(1.6 × 10⁻¹⁹)(0.01)]
3. r = 1.82 × 10⁻²³ / 1.6 × 10⁻²¹
4. r = **0.0114 m = 1.14 cm**

### Example 3: Induced EMF
**Problem**: A 50-turn coil with area 0.02 m² is in a magnetic field that decreases from 0.8 T to 0.2 T in 0.1 s. What is the induced EMF?

**Solution**:
1. ΔΦ = A × ΔB = 0.02 × (0.2 - 0.8) = -0.012 Wb
2. EMF = -N × ΔΦ/Δt = -50 × (-0.012)/0.1
3. EMF = **6 V**

## Explanation Patterns

1. **Identify the physical situation** - Is it force on a charge, force on a wire, or induction?
2. **Draw the geometry** - Show B field, velocity/current direction, and use right-hand rule
3. **Identify the angle** - Carefully determine θ between the relevant vectors
4. **Apply the appropriate formula** - F = qvB, F = BIL, or Faraday's law
5. **Check direction using right-hand rule** - Especially important for force problems
6. **Verify units** - Tesla = kg/(A·s²), Weber = T·m²

## Common Problem Types

1. **Force on moving charges**: Calculate force magnitude and direction
2. **Circular motion in B field**: Find radius, period, or frequency
3. **Force on current-carrying wires**: Calculate force on straight or curved wires
4. **Magnetic field calculations**: Find B from wires or solenoids
5. **Faraday's law problems**: Calculate induced EMF from changing flux
6. **Lenz's law**: Determine direction of induced current
