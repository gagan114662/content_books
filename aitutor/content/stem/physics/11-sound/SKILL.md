---
id: sound
subject: physics
display_name: Sound Waves
description: |
  Analyzes sound wave properties, propagation, and phenomena including Doppler effect and resonance.
  Use when students need to solve problems involving sound speed, intensity, decibels, beats, or standing waves in pipes.

grade_band: 9-12
khan_tags: [physics, sound, waves, doppler-effect, resonance, decibels]
standards:
  - NGSS.HS-PS4-1
  - NGSS.HS-PS4-3

objectives:
  - Describe sound as a longitudinal mechanical wave
  - Calculate the speed of sound in different media
  - Apply the decibel scale for sound intensity
  - Solve Doppler effect problems for moving sources and observers
  - Calculate beat frequency from two sound sources
  - Analyze standing waves and resonance in open and closed pipes

prerequisites:
  - waves

estimated_time_minutes: 60

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 17
    url: https://openstax.org/books/college-physics/pages/17-introduction-to-the-physics-of-hearing
    license: CC-BY-4.0
---

# Sound Waves

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Sound can travel through a vacuum" | Sound requires a medium; it cannot travel through a vacuum (unlike light) |
| "Louder sounds travel faster" | Sound speed depends on the medium, not amplitude or loudness |
| "The Doppler effect changes the actual frequency emitted" | Doppler effect only changes the observed frequency; the source frequency is unchanged |
| "Decibels are a linear scale" | Decibels are logarithmic; +10 dB means 10x the intensity |
| "Resonance creates energy" | Resonance transfers energy efficiently at natural frequencies; it doesn't create energy |
| "Sound travels faster in denser materials" | Sound speed depends on stiffness AND density; it's often faster in stiffer materials despite higher density |

## Key Concepts

### Sound as a Longitudinal Wave
Sound is a mechanical longitudinal wave that propagates through compression and rarefaction of a medium.

**Characteristics**:
- Requires a medium (solid, liquid, or gas)
- Particles oscillate parallel to wave direction
- Creates alternating high-pressure (compression) and low-pressure (rarefaction) regions
- Human hearing range: 20 Hz to 20,000 Hz

### Speed of Sound
The speed of sound depends on the medium's properties:

**In air** (approximate):
- v = 343 m/s at 20C (68F)
- Temperature dependence: v = 331 + 0.6T (where T is in Celsius)

**In general**:
- v = sqrt(B/rho) for fluids (B = bulk modulus, rho = density)
- v = sqrt(Y/rho) for solids (Y = Young's modulus)

**Typical values**:
- Air (20C): 343 m/s
- Water (25C): 1493 m/s
- Steel: 5960 m/s
- Human tissue: ~1540 m/s

### Intensity and Decibels
Sound intensity is power per unit area: I = P/A (W/m^2)

**Inverse square law**: Intensity decreases with distance squared
- I = P/(4*pi*r^2) for a point source

**Decibel scale** (logarithmic):
- beta = 10 * log10(I/I_0)
- I_0 = 10^(-12) W/m^2 (threshold of hearing)
- Each +10 dB = 10x intensity
- Each +3 dB = 2x intensity (approximately)

**Reference levels**:
- 0 dB: Threshold of hearing
- 60 dB: Normal conversation
- 85 dB: Prolonged exposure may cause damage
- 120 dB: Threshold of pain

### Doppler Effect
The apparent change in frequency when source and/or observer are moving.

**General formula**:
- f' = f * (v +/- v_o) / (v -/+ v_s)

**Convention**:
- Use + in numerator when observer moves toward source
- Use - in numerator when observer moves away from source
- Use - in denominator when source moves toward observer
- Use + in denominator when source moves away from observer

**Special cases**:
- Moving observer only: f' = f * (v + v_o) / v (approaching)
- Moving source only: f' = f * v / (v - v_s) (approaching)

### Beat Frequency
When two sound waves of slightly different frequencies interfere:
- f_beat = |f_1 - f_2|
- Creates periodic variation in loudness
- Used for tuning instruments

### Standing Waves in Pipes

**Open pipe** (open at both ends):
- Antinodes at both ends
- Harmonics: f_n = n * v / (2L), where n = 1, 2, 3, ...
- All harmonics present
- Wavelengths: lambda_n = 2L/n

**Closed pipe** (closed at one end):
- Node at closed end, antinode at open end
- Harmonics: f_n = n * v / (4L), where n = 1, 3, 5, ... (odd only)
- Only odd harmonics present
- Fundamental wavelength: lambda_1 = 4L

### Resonance
A system oscillates with maximum amplitude when driven at its natural frequency.

**Examples**:
- Musical instruments (strings, air columns)
- Tuning forks
- Breaking glass with voice

## Equations

```
[1] v = 343 m/s (speed of sound in air at 20C)
[2] v = 331 + 0.6T (speed of sound in air, T in Celsius)
[3] beta = 10 * log10(I/I_0), where I_0 = 10^(-12) W/m^2 (decibel level)
[4] I = P/(4*pi*r^2) (intensity from point source)
[5] f' = f * (v +/- v_o) / (v -/+ v_s) (Doppler effect)
[6] f_beat = |f_1 - f_2| (beat frequency)
[7] f_n = n * v / (2L), n = 1, 2, 3, ... (open pipe harmonics)
[8] f_n = n * v / (4L), n = 1, 3, 5, ... (closed pipe harmonics)
```

## Worked Examples

### Example 1: Speed of Sound
**Problem**: What is the speed of sound in air at 35C?

**Solution**:
1. Use the temperature formula: v = 331 + 0.6T
2. v = 331 + 0.6(35) = 331 + 21 = **352 m/s**

### Example 2: Decibel Calculation
**Problem**: A sound has intensity 5.0 x 10^(-6) W/m^2. What is its decibel level?

**Solution**:
1. Use decibel formula: beta = 10 * log10(I/I_0)
2. beta = 10 * log10(5.0 x 10^(-6) / 10^(-12))
3. beta = 10 * log10(5.0 x 10^6)
4. beta = 10 * 6.7 = **67 dB**

### Example 3: Doppler Effect
**Problem**: A car horn emits 400 Hz. If the car approaches at 30 m/s, what frequency does a stationary observer hear? (v_sound = 343 m/s)

**Solution**:
1. Source approaching, observer stationary
2. f' = f * v / (v - v_s)
3. f' = 400 * 343 / (343 - 30)
4. f' = 400 * 343 / 313 = **438 Hz**

### Example 4: Standing Waves in Closed Pipe
**Problem**: A closed pipe is 0.5 m long. What are the first two resonant frequencies? (v = 343 m/s)

**Solution**:
1. Closed pipe: only odd harmonics, f_n = n * v / (4L)
2. First harmonic (n=1): f_1 = 1 * 343 / (4 * 0.5) = 343/2 = **171.5 Hz**
3. Third harmonic (n=3): f_3 = 3 * 343 / (4 * 0.5) = 3 * 171.5 = **514.5 Hz**

## Explanation Patterns

1. **Identify the type of problem**: speed, intensity, Doppler, beats, or resonance
2. **Draw a diagram** showing wave direction, motion of source/observer, or pipe configuration
3. **Establish the reference frame** and sign conventions for Doppler problems
4. **Check if pipe is open or closed** - this determines which harmonics exist
5. **Use appropriate formula** and substitute values carefully
6. **Verify units** and check if answer is physically reasonable

## Common Problem Types

1. **Speed of sound**: Calculate v at different temperatures or in different media
2. **Intensity/decibels**: Convert between intensity (W/m^2) and decibel level, or use inverse square law
3. **Doppler effect**: Find observed frequency with moving source and/or observer
4. **Beat frequency**: Find the beat frequency or one of the original frequencies
5. **Open pipe resonance**: Find harmonics with antinodes at both ends
6. **Closed pipe resonance**: Find odd harmonics with node at closed end
7. **Wavelength in pipes**: Relate wavelength to pipe length for standing waves
