# Physics Content Library

## Overview
This content library covers high school physics topics aligned with OpenStax College Physics and Khan Academy curriculum. Each skill folder contains structured learning content with deterministic validation.

## Subject Information
- **Subject**: Physics
- **Grade Level**: 9-12 (High School)
- **Primary Source**: OpenStax College Physics (CC-BY 4.0)
- **Validator Type**: `numeric_solver` (unit-aware with tolerances)

## Skills Index

| # | Skill ID | Display Name | Source Chapter |
|---|----------|--------------|----------------|
| 01 | kinematics-1d | One-Dimensional Kinematics | Ch 2 |
| 02 | kinematics-2d | Two-Dimensional Kinematics | Ch 3 |
| 03 | newtons-laws | Newton's Laws of Motion | Ch 4 |
| 04 | forces-friction | Forces and Friction | Ch 5 |
| 05 | circular-motion | Circular Motion | Ch 6 |
| 06 | energy-work | Work and Energy | Ch 7 |
| 07 | momentum | Momentum and Collisions | Ch 8 |
| 08 | rotational-motion | Rotational Motion | Ch 10 |
| 09 | oscillations | Oscillations | Ch 16 |
| 10 | waves | Waves | Ch 16 |
| 11 | sound | Sound | Ch 17 |
| 12 | thermodynamics | Thermodynamics | Ch 15 |
| 13 | electrostatics | Electrostatics | Ch 18-19 |
| 14 | circuits | Electric Circuits | Ch 20-21 |
| 15 | magnetism | Magnetism | Ch 22-23 |
| 16 | optics | Optics | Ch 25-27 |

## Tutor Guidelines

When tutoring physics:

### Explanation Approach
1. **Start with physical intuition** - Use real-world examples before math
2. **Draw diagrams** - Always encourage sketching with coordinate systems
3. **Identify knowns/unknowns** - List them explicitly before solving
4. **Solve symbolically first** - Algebra before numbers
5. **Check units** - Dimensional analysis as verification
6. **Check reasonableness** - Does the answer make physical sense?

### Common Student Struggles
- Confusing scalars and vectors
- Sign conventions (especially in 1D kinematics)
- When to use which kinematic equation
- Free body diagrams and force identification
- Energy conservation vs. momentum conservation

### Validator Configuration
All physics problems use the `numeric_solver` validator with:
- Unit library: `physics` (SI units)
- Default tolerance: 2% relative
- Require units: true (students must include units in answers)
