---
id: electrostatics
subject: physics
display_name: Electrostatics
description: |
  Analyzes electric charges, forces, fields, and potentials using Coulomb's law and field theory.
  Use when students need to solve problems involving electric charge interactions, electric fields, and electric potential.

grade_band: 9-12
khan_tags: [physics, electricity, coulombs-law, electric-field, electric-potential]
standards:
  - NGSS.HS-PS2-4
  - NGSS.HS-PS3-5

objectives:
  - Apply Coulomb's law to calculate electric forces between point charges
  - Calculate electric fields from point charges and charge distributions
  - Determine electric potential from point charges
  - Calculate electric potential energy of charge configurations
  - Calculate work done by electric fields on moving charges
  - Distinguish between conductors and insulators

prerequisites:
  - newtons-laws

estimated_time_minutes: 90

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 18-19
    url: https://openstax.org/books/college-physics/pages/18-introduction-to-electric-charge-and-electric-field
    license: CC-BY-4.0
---

# Electrostatics

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Positive charges are heavier than negative charges" | Protons and electrons have nearly the same magnitude of charge; mass is unrelated to charge sign |
| "Electric field is the same as electric force" | Electric field (E) is force per unit charge; E = F/q. Field exists even without a test charge |
| "Doubling the distance halves the force" | Coulomb's law has inverse-square dependence: F ~ 1/r². Doubling distance reduces force to 1/4 |
| "Electric potential is the same as potential energy" | Potential (V) is energy per unit charge; PE = qV. Potential is a property of position, PE depends on the charge placed there |
| "Insulators cannot have any charge" | Insulators can hold charge; they just don't allow charge to flow freely through them |

## Key Concepts

### Electric Charge
The fundamental property of matter that causes electromagnetic interactions.

**Properties**:
- Two types: positive (+) and negative (-)
- Like charges repel, opposite charges attract
- Charge is quantized: q = ne, where e = 1.602 × 10⁻¹⁹ C
- Charge is conserved in all processes
- Unit: Coulomb (C)

### Coulomb's Law
The electric force between two point charges:

$$F = k\frac{q_1 q_2}{r^2}$$

Where:
- k = 8.99 × 10⁹ N·m²/C² (Coulomb's constant)
- q₁, q₂ = charges (in Coulombs)
- r = distance between charges (in meters)
- F = force (in Newtons)

**Direction**:
- Positive F: repulsive (like charges)
- Negative F: attractive (opposite charges)
- Force acts along the line connecting the charges

### Electric Field
A vector field that describes the electric force per unit positive test charge:

$$E = \frac{F}{q} = k\frac{Q}{r^2}$$

Where:
- E = electric field strength (N/C or V/m)
- Q = source charge creating the field
- r = distance from the source charge

**Direction**:
- Points away from positive charges
- Points toward negative charges
- At any point, E indicates the direction a positive test charge would accelerate

### Electric Potential
The electric potential energy per unit charge (scalar quantity):

$$V = k\frac{Q}{r}$$

Where:
- V = electric potential (Volts, V = J/C)
- Q = source charge
- r = distance from the source charge

**Key points**:
- Positive charges create positive potential
- Negative charges create negative potential
- Potential is a scalar (no direction)
- Potential difference (voltage) drives current

### Electric Potential Energy
The energy stored in a system of charges:

$$PE = k\frac{q_1 q_2}{r} = qV$$

Where:
- PE = potential energy (Joules)
- q₁, q₂ = the two charges
- r = separation distance
- V = potential at the location of charge q

**Sign convention**:
- Positive PE: like charges (repulsive, energy required to bring together)
- Negative PE: opposite charges (attractive, energy released when brought together)

### Work Done by Electric Field
Work done by the electric field when moving a charge:

$$W = q(V_i - V_f) = -\Delta PE$$

Where:
- W = work done by the field (Joules)
- q = charge being moved
- Vᵢ, Vf = initial and final potentials

**Key points**:
- Field does positive work when moving + charge to lower potential
- Field does positive work when moving - charge to higher potential
- Work by field = negative of change in PE

### Conductors vs Insulators

**Conductors**:
- Allow charges to move freely
- Excess charge resides on the surface
- Electric field inside is zero (electrostatic equilibrium)
- Examples: metals, ionic solutions

**Insulators**:
- Charges cannot move freely
- Charge remains where placed
- Can be polarized (induced dipoles)
- Examples: rubber, glass, plastic

## Equations

```
[1] F = kq₁q₂/r² (Coulomb's law)
[2] E = F/q = kQ/r² (electric field from point charge)
[3] V = kQ/r (electric potential from point charge)
[4] PE = kq₁q₂/r = qV (electric potential energy)
[5] W = q(Vᵢ - Vf) = -ΔPE (work by electric field)
[6] k = 8.99 × 10⁹ N·m²/C² (Coulomb's constant)
[7] e = 1.602 × 10⁻¹⁹ C (elementary charge)
```

## Worked Examples

### Example 1: Coulomb's Law
**Problem**: Two charges, q₁ = +3 μC and q₂ = -5 μC, are separated by 0.2 m. What is the magnitude of the electric force between them?

**Solution**:
1. Convert units: q₁ = 3 × 10⁻⁶ C, q₂ = 5 × 10⁻⁶ C
2. Apply Coulomb's law: F = k|q₁q₂|/r²
3. F = (8.99 × 10⁹)(3 × 10⁻⁶)(5 × 10⁻⁶)/(0.2)²
4. F = (8.99 × 10⁹)(15 × 10⁻¹²)/(0.04)
5. F = **3.37 N** (attractive)

### Example 2: Electric Field
**Problem**: What is the electric field 0.5 m from a +8 μC point charge?

**Solution**:
1. E = kQ/r²
2. E = (8.99 × 10⁹)(8 × 10⁻⁶)/(0.5)²
3. E = (8.99 × 10⁹)(8 × 10⁻⁶)/0.25
4. E = **2.88 × 10⁵ N/C** (pointing away from the charge)

### Example 3: Electric Potential Energy
**Problem**: How much work is required to bring a +2 μC charge from infinity to a point 0.3 m from a +6 μC charge?

**Solution**:
1. Work required = ΔPE = PEf - PEi
2. PEi = 0 (at infinity)
3. PEf = kq₁q₂/r = (8.99 × 10⁹)(2 × 10⁻⁶)(6 × 10⁻⁶)/0.3
4. PEf = (8.99 × 10⁹)(12 × 10⁻¹²)/0.3
5. Work = **0.36 J**

## Explanation Patterns

1. **Identify the charges** - What are their signs and magnitudes?
2. **Determine what's asked** - Force, field, potential, or energy?
3. **Draw a diagram** - Show charges, distances, and direction of fields/forces
4. **Choose the appropriate equation**:
   - Force between charges: Coulomb's law
   - Field from a charge: E = kQ/r²
   - Potential from a charge: V = kQ/r
   - Energy of configuration: PE = kq₁q₂/r
5. **Watch units** - Convert μC to C, cm to m
6. **Check signs** - Like charges repel, opposite attract

## Common Problem Types

1. **Coulomb force calculations**: Find force magnitude and direction between point charges
2. **Electric field from point charges**: Calculate field strength and direction
3. **Superposition of fields**: Add vector fields from multiple charges
4. **Electric potential calculations**: Find potential at a point from one or more charges
5. **Potential energy of charge systems**: Calculate energy stored in charge configurations
6. **Work-energy problems**: Find work to move charges between points
7. **Conductor/insulator concepts**: Qualitative questions about charge distribution
