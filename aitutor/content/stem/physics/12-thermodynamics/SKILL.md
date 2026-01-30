---
id: thermodynamics
subject: physics
display_name: Thermodynamics
description: |
  Analyzes heat transfer, temperature changes, and energy transformations in thermal systems.
  Use when students need to solve problems involving temperature, heat, specific heat, phase changes, gas laws, or heat engines.

grade_band: 9-12
khan_tags: [physics, thermodynamics, heat, temperature, ideal-gas-law, heat-engines]
standards:
  - NGSS.HS-PS3-4
  - NGSS.HS-PS3-2

objectives:
  - Convert between temperature scales (Celsius, Fahrenheit, Kelvin)
  - Calculate heat transfer using Q = mcDeltaT
  - Apply specific heat concepts to calorimetry problems
  - Calculate energy for phase changes using latent heat
  - Apply thermal expansion formulas
  - Use the ideal gas law (PV = nRT)
  - Apply the first law of thermodynamics
  - Calculate heat engine efficiency

prerequisites:
  - energy-work

estimated_time_minutes: 90

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 15
    url: https://openstax.org/books/college-physics/pages/15-introduction-to-thermodynamics
    license: CC-BY-4.0
---

# Thermodynamics

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Heat and temperature are the same thing" | Temperature measures average kinetic energy; heat is energy transferred due to temperature difference |
| "Cold flows into warm objects" | Heat always flows from hot to cold; cold is absence of heat energy |
| "Metals are naturally cold" | Metals feel cold because they conduct heat away from your hand quickly |
| "Boiling water gets hotter as it boils longer" | Temperature stays constant during phase change; energy goes into breaking bonds |
| "Larger objects always have more heat" | Heat capacity depends on mass AND specific heat; a small amount of water can store more heat than a large piece of metal |

## Key Concepts

### Temperature Scales
Temperature is a measure of the average kinetic energy of particles.

**Conversion formulas**:
- Celsius to Fahrenheit: T_F = (9/5)T_C + 32
- Fahrenheit to Celsius: T_C = (5/9)(T_F - 32)
- Celsius to Kelvin: T_K = T_C + 273.15
- Kelvin to Celsius: T_C = T_K - 273.15

**Absolute zero**: 0 K = -273.15 C (lowest possible temperature)

### Heat Transfer
Heat (Q) is energy transferred due to temperature difference.

**Heat equation**:
- Q = mcDeltaT
- Q = heat transferred (J)
- m = mass (kg)
- c = specific heat capacity (J/kg*K)
- DeltaT = temperature change (K or C)

**Sign convention**:
- Q > 0: heat absorbed by system
- Q < 0: heat released by system

### Specific Heat
The amount of heat required to raise 1 kg of a substance by 1 K.

**Common values**:
- Water: c = 4186 J/kg*K
- Ice: c = 2090 J/kg*K
- Steam: c = 2010 J/kg*K
- Aluminum: c = 900 J/kg*K
- Copper: c = 385 J/kg*K
- Iron: c = 450 J/kg*K

### Calorimetry
In an isolated system, heat lost = heat gained:
- Q_lost + Q_gained = 0
- m_1*c_1*DeltaT_1 + m_2*c_2*DeltaT_2 = 0

### Latent Heat
Energy required for phase change (no temperature change):
- Q = mL
- L_f = latent heat of fusion (solid <-> liquid)
- L_v = latent heat of vaporization (liquid <-> gas)

**For water**:
- L_f = 3.34 x 10^5 J/kg (melting/freezing)
- L_v = 2.26 x 10^6 J/kg (boiling/condensing)

### Thermal Expansion
Materials expand when heated:

**Linear expansion**:
- DeltaL = alpha*L_0*DeltaT
- alpha = coefficient of linear expansion

**Volume expansion**:
- DeltaV = beta*V_0*DeltaT
- beta approximately equals 3*alpha for solids

### Ideal Gas Law
Relates pressure, volume, temperature, and amount of gas:
- PV = nRT
- P = pressure (Pa)
- V = volume (m^3)
- n = number of moles
- R = 8.314 J/mol*K (gas constant)
- T = absolute temperature (K)

**Alternative form**: PV = NkT (N = number of molecules, k = Boltzmann constant)

**Combined gas law** (fixed amount of gas):
- P_1*V_1/T_1 = P_2*V_2/T_2

### First Law of Thermodynamics
Conservation of energy for thermal systems:
- DeltaU = Q - W
- DeltaU = change in internal energy
- Q = heat added to system
- W = work done BY system

**Special processes**:
- Isothermal (constant T): DeltaU = 0, so Q = W
- Isochoric (constant V): W = 0, so DeltaU = Q
- Isobaric (constant P): W = P*DeltaV
- Adiabatic (no heat transfer): Q = 0, so DeltaU = -W

### Heat Engines
Convert heat to work using temperature difference.

**Efficiency**:
- e = W/Q_H = (Q_H - Q_C)/Q_H = 1 - Q_C/Q_H
- Q_H = heat absorbed from hot reservoir
- Q_C = heat expelled to cold reservoir
- W = useful work output

**Carnot efficiency** (maximum possible):
- e_Carnot = 1 - T_C/T_H
- T must be in Kelvin

## Equations

```
[1] T_F = (9/5)T_C + 32 (Celsius to Fahrenheit)
[2] T_K = T_C + 273.15 (Celsius to Kelvin)
[3] Q = mcDeltaT (heat transfer)
[4] Q = mL (latent heat)
[5] DeltaL = alpha*L_0*DeltaT (linear expansion)
[6] PV = nRT (ideal gas law)
[7] P_1*V_1/T_1 = P_2*V_2/T_2 (combined gas law)
[8] DeltaU = Q - W (first law of thermodynamics)
[9] e = W/Q_H = 1 - Q_C/Q_H (heat engine efficiency)
[10] e_Carnot = 1 - T_C/T_H (Carnot efficiency)
```

## Worked Examples

### Example 1: Temperature Conversion
**Problem**: Convert 77 F to Celsius and Kelvin.

**Solution**:
1. T_C = (5/9)(T_F - 32) = (5/9)(77 - 32) = (5/9)(45) = **25 C**
2. T_K = T_C + 273.15 = 25 + 273.15 = **298.15 K**

### Example 2: Heat Transfer
**Problem**: How much heat is needed to raise the temperature of 2 kg of water from 20 C to 80 C?

**Solution**:
1. Q = mcDeltaT
2. Q = 2 x 4186 x (80 - 20) = 2 x 4186 x 60 = **502,320 J** (or 502.3 kJ)

### Example 3: Calorimetry
**Problem**: A 0.5 kg piece of iron at 200 C is dropped into 2 kg of water at 20 C. Find the final temperature.

**Solution**:
1. Heat lost by iron = Heat gained by water
2. m_Fe*c_Fe*(T_i,Fe - T_f) = m_w*c_w*(T_f - T_i,w)
3. 0.5 x 450 x (200 - T_f) = 2 x 4186 x (T_f - 20)
4. 225(200 - T_f) = 8372(T_f - 20)
5. 45000 - 225*T_f = 8372*T_f - 167440
6. 212440 = 8597*T_f
7. T_f = **24.7 C**

### Example 4: Ideal Gas Law
**Problem**: A gas at 300 K and 100 kPa occupies 2 L. What is its pressure if compressed to 0.5 L at 400 K?

**Solution**:
1. P_1*V_1/T_1 = P_2*V_2/T_2
2. P_2 = P_1*V_1*T_2/(V_2*T_1)
3. P_2 = 100 x 2 x 400/(0.5 x 300) = 80000/150 = **533 kPa**

### Example 5: Heat Engine Efficiency
**Problem**: A heat engine absorbs 1000 J from a hot reservoir at 500 K and expels heat to a cold reservoir at 300 K. What is the maximum work output?

**Solution**:
1. Carnot efficiency: e = 1 - T_C/T_H = 1 - 300/500 = 0.4
2. Maximum work: W = e*Q_H = 0.4 x 1000 = **400 J**

## Explanation Patterns

1. **Identify the thermal process** - Is it heating/cooling, phase change, or gas behavior?
2. **List known quantities** - temperatures, masses, pressures, volumes
3. **Choose the appropriate equation** - Q = mcDeltaT, PV = nRT, etc.
4. **Check units** - especially temperature (K vs C) for gas law and efficiency
5. **Apply conservation** - energy in = energy out for calorimetry
6. **Check reasonableness** - heat flows hot to cold, efficiency < 100%

## Common Problem Types

1. **Temperature conversion**: Converting between C, F, and K
2. **Heat transfer**: Finding Q, m, c, or DeltaT using Q = mcDeltaT
3. **Calorimetry**: Finding final temperature when objects exchange heat
4. **Phase changes**: Calculating energy for melting, freezing, boiling, condensing
5. **Ideal gas law**: Finding P, V, n, or T for a gas
6. **Combined gas law**: Comparing initial and final states of a gas
7. **First law problems**: Energy balance with heat and work
8. **Heat engine efficiency**: Calculating efficiency and work output
