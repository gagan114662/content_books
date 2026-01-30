---
id: waves
subject: physics
display_name: Wave Properties and Behavior
description: |
  Covers the fundamental properties of mechanical waves including transverse and longitudinal waves,
  wavelength, frequency, amplitude, wave speed, interference, and standing waves.
  Use when students need to understand wave behavior, solve wave speed problems, or analyze interference patterns.

grade_band: 9-12
khan_tags: [physics, waves, frequency, wavelength, interference, standing-waves, superposition]
standards:
  - NGSS.HS-PS4-1
  - NGSS.HS-PS4-5

objectives:
  - Distinguish between transverse and longitudinal waves
  - Calculate wave speed using v = f*lambda
  - Relate frequency, period, and wavelength
  - Apply the wave equation for waves on a string (v = sqrt(T/mu))
  - Analyze constructive and destructive interference
  - Solve standing wave and harmonic problems
  - Apply the superposition principle

prerequisites:
  - oscillations

estimated_time_minutes: 60

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 16
    url: https://openstax.org/books/college-physics/pages/16-introduction-to-oscillatory-motion-and-waves
    license: CC-BY-4.0
---

# Wave Properties and Behavior

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Waves transport matter from one place to another" | Waves transport energy, not matter; particles oscillate in place |
| "Wave speed depends on amplitude or frequency" | Wave speed depends only on the medium properties (e.g., tension and mass density for strings) |
| "Higher frequency means faster wave" | Frequency affects wavelength, not wave speed in a given medium |
| "In destructive interference, energy is destroyed" | Energy is conserved; it redistributes spatially |
| "All waves need a medium to travel" | Mechanical waves need a medium; electromagnetic waves do not |
| "Wavelength and amplitude are the same thing" | Wavelength is the spatial period; amplitude is the maximum displacement |

## Key Concepts

### Types of Waves

**Transverse Waves**:
- Particle motion is perpendicular to wave propagation
- Examples: waves on a string, water surface waves, light
- Can be polarized

**Longitudinal Waves**:
- Particle motion is parallel to wave propagation
- Consists of compressions and rarefactions
- Examples: sound waves, pressure waves in fluids
- Cannot be polarized

### Wave Parameters

**Wavelength (lambda)**:
- Distance between two consecutive identical points (e.g., crest to crest)
- Unit: meters (m)

**Frequency (f)**:
- Number of complete oscillations per second
- Unit: Hertz (Hz) = 1/s
- f = 1/T where T is the period

**Period (T)**:
- Time for one complete oscillation
- Unit: seconds (s)
- T = 1/f

**Amplitude (A)**:
- Maximum displacement from equilibrium
- Determines wave intensity/energy
- Unit: meters (m) for mechanical waves

**Wave Speed (v)**:
- Speed at which the wave pattern propagates
- Depends on medium properties, not on frequency or amplitude

### The Wave Equation

The fundamental relationship between wave speed, frequency, and wavelength:
- **v = f * lambda**
- Also: v = lambda / T

### Waves on a String

For a wave traveling on a stretched string:
- **v = sqrt(T / mu)**
- T = tension in the string (N)
- mu = linear mass density = mass/length (kg/m)

### Superposition Principle

When two or more waves overlap, the resultant displacement is the algebraic sum of individual displacements:
- **y_total = y_1 + y_2 + y_3 + ...**

### Interference

**Constructive Interference**:
- Occurs when waves are in phase
- Crests align with crests, troughs with troughs
- Resultant amplitude = sum of individual amplitudes
- Path difference = n * lambda (n = 0, 1, 2, ...)

**Destructive Interference**:
- Occurs when waves are out of phase by half a wavelength
- Crests align with troughs
- Resultant amplitude = difference of individual amplitudes
- Path difference = (n + 1/2) * lambda

### Standing Waves

Formed when two identical waves travel in opposite directions:
- **Nodes**: Points of zero displacement (destructive interference)
- **Antinodes**: Points of maximum displacement (constructive interference)

**Standing Waves on a String Fixed at Both Ends**:
- Fundamental (1st harmonic): L = lambda_1 / 2
- nth harmonic: L = n * lambda_n / 2
- lambda_n = 2L / n
- f_n = n * f_1 = n * v / (2L)

**Standing Waves on a String Fixed at One End (Open at Other)**:
- Only odd harmonics present
- L = (2n - 1) * lambda_n / 4 for n = 1, 2, 3, ...
- lambda_n = 4L / (2n - 1)
- f_n = (2n - 1) * f_1

## Equations

```
[1] v = f * lambda (wave equation)
[2] f = 1/T (frequency and period)
[3] v = sqrt(T / mu) (wave speed on a string)
[4] lambda_n = 2L / n (standing wave, both ends fixed)
[5] f_n = n * v / (2L) (harmonics, both ends fixed)
[6] f_n = n * f_1 (harmonic frequencies)
[7] Path difference = n * lambda (constructive interference)
[8] Path difference = (n + 0.5) * lambda (destructive interference)
```

## Worked Examples

### Example 1: Wave Speed Calculation
**Problem**: A wave has a frequency of 440 Hz and a wavelength of 0.78 m. What is the wave speed?

**Solution**:
1. Use the wave equation: v = f * lambda
2. v = 440 Hz * 0.78 m
3. v = **343.2 m/s**

### Example 2: Wavelength from Frequency
**Problem**: A radio station broadcasts at 98.5 MHz. Radio waves travel at 3.0 x 10^8 m/s. What is the wavelength?

**Solution**:
1. Convert frequency: f = 98.5 MHz = 98.5 x 10^6 Hz
2. Rearrange v = f * lambda to get lambda = v / f
3. lambda = (3.0 x 10^8) / (98.5 x 10^6)
4. lambda = **3.05 m**

### Example 3: Wave Speed on a String
**Problem**: A guitar string has a tension of 120 N and a linear mass density of 0.003 kg/m. What is the wave speed?

**Solution**:
1. Use v = sqrt(T / mu)
2. v = sqrt(120 / 0.003) = sqrt(40000)
3. v = **200 m/s**

### Example 4: Standing Wave Harmonics
**Problem**: A string of length 0.65 m is fixed at both ends. If the wave speed is 260 m/s, what are the frequencies of the first three harmonics?

**Solution**:
1. Fundamental frequency: f_1 = v / (2L) = 260 / (2 * 0.65) = 260 / 1.3 = **200 Hz**
2. Second harmonic: f_2 = 2 * f_1 = **400 Hz**
3. Third harmonic: f_3 = 3 * f_1 = **600 Hz**

### Example 5: Interference
**Problem**: Two speakers emit sound waves of wavelength 0.5 m in phase. A listener is 4 m from one speaker and 5.5 m from the other. Is the interference constructive or destructive?

**Solution**:
1. Path difference = |5.5 - 4| = 1.5 m
2. Check: path difference / lambda = 1.5 / 0.5 = 3
3. Since 3 is a whole number, the path difference is 3*lambda
4. **Constructive interference** (waves arrive in phase)

## Explanation Patterns

1. **Identify wave type** - Is it transverse or longitudinal?
2. **List known quantities** - What are the given values (f, lambda, v, T, mu)?
3. **Choose the appropriate equation** - v = f*lambda for basic problems, v = sqrt(T/mu) for strings
4. **For standing waves**, draw the pattern and count nodes/antinodes
5. **For interference**, calculate path difference and compare to wavelength
6. **Check units** - Frequency in Hz, wavelength in m, speed in m/s
7. **Verify reasonableness** - Does the answer make physical sense?

## Common Problem Types

1. **Wave speed calculation**: Using v = f*lambda
2. **Finding wavelength or frequency**: Rearranging v = f*lambda
3. **Waves on a string**: Using v = sqrt(T/mu)
4. **Standing wave frequencies**: Finding harmonics using f_n = nv/(2L)
5. **Standing wave wavelengths**: Finding lambda_n = 2L/n
6. **Interference determination**: Calculating path difference and determining type
7. **Superposition problems**: Adding wave displacements algebraically
