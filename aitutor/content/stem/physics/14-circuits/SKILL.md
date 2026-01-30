---
id: circuits
subject: physics
display_name: Electric Circuits
description: |
  Analyzes electric circuits using Ohm's law, series/parallel resistor combinations, and Kirchhoff's laws.
  Use when students need to solve problems involving current, voltage, resistance, power, or circuit analysis.

grade_band: 9-12
khan_tags: [physics, circuits, ohms-law, resistors, power, kirchhoffs-laws]
standards:
  - NGSS.HS-PS3-3
  - NGSS.HS-PS3-5

objectives:
  - Define current as charge flow rate (I = Q/t)
  - Apply Ohm's law (V = IR) to circuit elements
  - Calculate equivalent resistance for series and parallel circuits
  - Apply Kirchhoff's voltage law (loop rule) and current law (junction rule)
  - Calculate electrical power using P = IV = I²R = V²/R
  - Analyze simple RC circuits and time constants

prerequisites:
  - electrostatics

estimated_time_minutes: 90

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 20-21
    url: https://openstax.org/books/college-physics/pages/20-introduction-to-electric-current-resistance-and-ohms-law
    license: CC-BY-4.0
---

# Electric Circuits

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Current gets used up in a circuit" | Current is conserved; it flows continuously around a closed loop. The same current enters and exits a resistor |
| "Batteries store charge" | Batteries store chemical energy and provide a voltage (potential difference), not charge |
| "Voltage flows through a wire" | Voltage is a potential difference between two points; current flows, voltage is measured across |
| "All resistors get the same current" | Only true in series; in parallel, current divides inversely proportional to resistance |
| "Adding resistors always increases total resistance" | True for series, but parallel combinations decrease total resistance |

## Key Concepts

### Electric Current
Current is the rate of charge flow through a conductor.

**Definition**:
- I = Q/t (charge per unit time)
- Unit: Ampere (A) = Coulomb/second (C/s)
- Conventional current flows from + to - (opposite to electron flow)

### Resistance
Resistance opposes the flow of current.

**Ohm's Law**:
- V = IR
- R = V/I
- Unit: Ohm (Ω) = V/A

**Factors affecting resistance**:
- R = ρL/A (resistivity × length / cross-sectional area)
- Temperature increases resistance in most conductors

### Resistors in Series
When resistors are connected end-to-end:
- Same current through all: I_total = I_1 = I_2 = I_3
- Voltages add: V_total = V_1 + V_2 + V_3
- Equivalent resistance: R_eq = R_1 + R_2 + R_3

### Resistors in Parallel
When resistors share the same two nodes:
- Same voltage across all: V_total = V_1 = V_2 = V_3
- Currents add: I_total = I_1 + I_2 + I_3
- Equivalent resistance: 1/R_eq = 1/R_1 + 1/R_2 + 1/R_3

**Special case for two resistors in parallel**:
- R_eq = (R_1 × R_2) / (R_1 + R_2)

### Kirchhoff's Laws

**Junction Rule (KCL - Kirchhoff's Current Law)**:
- Sum of currents entering a junction = sum of currents leaving
- ΣI_in = ΣI_out
- Based on conservation of charge

**Loop Rule (KVL - Kirchhoff's Voltage Law)**:
- Sum of voltage changes around any closed loop = 0
- ΣV = 0 (around a loop)
- Based on conservation of energy

**Sign conventions for loop rule**:
- EMF: + if traversing from - to + terminal
- Resistor: - if traversing in direction of current (voltage drop)

### Electrical Power
Power is the rate of energy transfer.

**Power formulas**:
- P = IV (general form)
- P = I²R (useful when current is known)
- P = V²/R (useful when voltage is known)
- Unit: Watt (W) = J/s = V·A

**Energy dissipated**:
- E = Pt (energy = power × time)
- Unit: Joule (J) or kilowatt-hour (kWh)

### RC Circuits (Basics)
A circuit with a resistor and capacitor in series.

**Charging a capacitor**:
- Q(t) = Q_max(1 - e^(-t/τ))
- τ = RC (time constant)
- After 5τ, capacitor is ~99% charged

**Discharging**:
- Q(t) = Q_0 × e^(-t/τ)
- Current and voltage decrease exponentially

## Equations

```
[1] I = Q/t (definition of current)
[2] V = IR (Ohm's law)
[3] R_series = R_1 + R_2 + R_3 + ... (series resistors)
[4] 1/R_parallel = 1/R_1 + 1/R_2 + 1/R_3 + ... (parallel resistors)
[5] P = IV = I²R = V²/R (electrical power)
[6] ΣI_in = ΣI_out (Kirchhoff's current law)
[7] ΣV_loop = 0 (Kirchhoff's voltage law)
[8] τ = RC (RC time constant)
```

## Worked Examples

### Example 1: Ohm's Law
**Problem**: A 12 V battery is connected to a 4 Ω resistor. What current flows through the resistor?

**Solution**:
1. Use Ohm's law: V = IR
2. Solve for I: I = V/R
3. I = 12/4 = **3 A**

### Example 2: Series Circuit
**Problem**: Three resistors (2 Ω, 3 Ω, and 5 Ω) are connected in series to a 20 V battery. Find the current and voltage across each resistor.

**Solution**:
1. Find equivalent resistance: R_eq = 2 + 3 + 5 = 10 Ω
2. Find total current: I = V/R_eq = 20/10 = 2 A
3. Voltage drops: V_1 = IR_1 = 2×2 = 4 V, V_2 = 2×3 = 6 V, V_3 = 2×5 = 10 V
4. Check: 4 + 6 + 10 = 20 V ✓

### Example 3: Parallel Circuit
**Problem**: Two resistors (6 Ω and 3 Ω) are connected in parallel to a 12 V source. Find the total current.

**Solution**:
1. Equivalent resistance: 1/R_eq = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2
2. R_eq = 2 Ω
3. Total current: I = V/R_eq = 12/2 = **6 A**

### Example 4: Power Calculation
**Problem**: A 60 W light bulb operates at 120 V. What is its resistance and the current through it?

**Solution**:
1. Find current: P = IV → I = P/V = 60/120 = 0.5 A
2. Find resistance: R = V/I = 120/0.5 = **240 Ω**
3. Or directly: P = V²/R → R = V²/P = 14400/60 = **240 Ω**

## Explanation Patterns

1. **Identify circuit type** - Is it series, parallel, or combination?
2. **Simplify the circuit** - Combine series and parallel sections step by step
3. **Find total current** - Use V_source / R_equivalent
4. **Work backward** - Find voltage and current in each branch
5. **Apply Kirchhoff's laws** for complex circuits
6. **Check your answer** - Verify KCL at junctions and KVL around loops

## Common Problem Types

1. **Ohm's law calculations**: Direct application of V = IR
2. **Series circuits**: Same current, voltages add
3. **Parallel circuits**: Same voltage, currents add
4. **Combined circuits**: Systematic simplification
5. **Power calculations**: Using P = IV, I²R, or V²/R
6. **Kirchhoff's laws**: Multi-loop circuit analysis
7. **RC circuits**: Time constant and exponential behavior
