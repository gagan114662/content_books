---
id: oscillations
subject: physics
display_name: Oscillations and Simple Harmonic Motion
description: |
  Analyzes periodic motion including simple harmonic motion, springs, and pendulums.
  Use when students need to solve problems involving oscillations, period, frequency, amplitude, or energy in harmonic systems.

grade_band: 9-12
khan_tags: [physics, oscillations, simple-harmonic-motion, springs, pendulums, waves]
standards:
  - NGSS.HS-PS4-1

objectives:
  - Define and calculate period, frequency, and angular frequency
  - Describe position, velocity, and acceleration in SHM
  - Calculate the period of a mass-spring system
  - Calculate the period of a simple pendulum
  - Apply energy conservation to oscillating systems
  - Understand the effects of damping on oscillations

prerequisites:
  - energy-work
  - circular-motion

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

# Oscillations and Simple Harmonic Motion

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Period depends on amplitude" | For ideal springs and small-angle pendulums, period is independent of amplitude |
| "Heavier pendulums swing slower" | Pendulum period depends only on length and g, not mass: T = 2pi*sqrt(L/g) |
| "At equilibrium, velocity is zero" | At equilibrium, velocity is maximum; acceleration is zero |
| "SHM acceleration is constant" | Acceleration varies sinusoidally, maximum at endpoints, zero at equilibrium |
| "Stiffer springs oscillate slower" | Stiffer springs (larger k) have shorter periods: T = 2pi*sqrt(m/k) |
| "Energy is lost in ideal oscillations" | Total mechanical energy is conserved; it transforms between KE and PE |

## Key Concepts

### Simple Harmonic Motion (SHM)
Motion where the restoring force is proportional to displacement from equilibrium:
- F = -kx (Hooke's Law for springs)
- Results in sinusoidal motion
- Acceleration always points toward equilibrium
- a = -omega^2 * x

**Key characteristics**:
- Motion repeats with constant period T
- Amplitude A is the maximum displacement from equilibrium
- Angular frequency omega = 2*pi/T = 2*pi*f

### Period and Frequency
- **Period (T)**: Time for one complete oscillation (seconds)
- **Frequency (f)**: Number of oscillations per second (Hz = 1/s)
- **Angular frequency (omega)**: omega = 2*pi*f = 2*pi/T (rad/s)

Relationships:
- f = 1/T
- omega = 2*pi*f = 2*pi/T

### Amplitude
- Maximum displacement from equilibrium position
- Does not affect period in ideal SHM
- Determines maximum velocity and acceleration

### Mass-Spring System
A mass m attached to a spring with spring constant k:
- **Period**: T = 2*pi*sqrt(m/k)
- **Frequency**: f = (1/2*pi)*sqrt(k/m)
- **Angular frequency**: omega = sqrt(k/m)

Key insights:
- Period increases with mass (heavier = slower)
- Period decreases with stiffer spring (larger k = faster)
- Period is independent of amplitude and gravity

### Simple Pendulum
A mass on a string of length L (for small angles < 15 degrees):
- **Period**: T = 2*pi*sqrt(L/g)
- **Frequency**: f = (1/2*pi)*sqrt(g/L)

Key insights:
- Period depends only on length and gravitational acceleration
- Period is independent of mass and amplitude (for small angles)
- Longer pendulum = longer period

### Position, Velocity, and Acceleration in SHM
Starting from maximum displacement (x = A at t = 0):
- **Position**: x(t) = A*cos(omega*t)
- **Velocity**: v(t) = -A*omega*sin(omega*t)
- **Acceleration**: a(t) = -A*omega^2*cos(omega*t) = -omega^2*x

Maximum values:
- Maximum displacement: |x_max| = A
- Maximum velocity: |v_max| = A*omega
- Maximum acceleration: |a_max| = A*omega^2

Phase relationships:
- Velocity leads position by 90 degrees (pi/2 radians)
- Acceleration leads velocity by 90 degrees
- Acceleration is 180 degrees out of phase with position

### Energy in Simple Harmonic Motion
Total mechanical energy is conserved:
- **Potential Energy**: PE = (1/2)*k*x^2
- **Kinetic Energy**: KE = (1/2)*m*v^2
- **Total Energy**: E = (1/2)*k*A^2 = (1/2)*m*v_max^2

At any position:
- E = KE + PE = (1/2)*m*v^2 + (1/2)*k*x^2 = (1/2)*k*A^2

Energy exchange:
- At x = 0 (equilibrium): KE = max, PE = 0
- At x = +/- A (endpoints): KE = 0, PE = max

### Damped Oscillations
Real oscillations lose energy due to friction or air resistance:
- Amplitude decreases over time
- Three regimes:
  - **Underdamped**: Oscillates with decreasing amplitude
  - **Critically damped**: Returns to equilibrium fastest without oscillating
  - **Overdamped**: Returns slowly without oscillating

For underdamped systems:
- x(t) = A*e^(-bt/(2m))*cos(omega't)
- omega' < omega_0 (damped frequency is less than natural frequency)

## Equations

```
[1] x = A*cos(omega*t) or x = A*sin(omega*t + phi) (position in SHM)
[2] v = -A*omega*sin(omega*t) (velocity in SHM)
[3] a = -A*omega^2*cos(omega*t) = -omega^2*x (acceleration in SHM)
[4] T = 2*pi*sqrt(m/k) (period of mass-spring system)
[5] T = 2*pi*sqrt(L/g) (period of simple pendulum)
[6] f = 1/T, omega = 2*pi*f = 2*pi/T (frequency relationships)
[7] v_max = A*omega (maximum velocity)
[8] a_max = A*omega^2 (maximum acceleration)
[9] E = (1/2)*k*A^2 = (1/2)*m*v_max^2 (total energy)
[10] (1/2)*m*v^2 + (1/2)*k*x^2 = (1/2)*k*A^2 (energy conservation)
```

## Worked Examples

### Example 1: Mass-Spring Period
**Problem**: A 0.5 kg mass is attached to a spring with k = 200 N/m. What is the period of oscillation?

**Solution**:
1. Use the mass-spring period formula: T = 2*pi*sqrt(m/k)
2. T = 2*pi*sqrt(0.5/200) = 2*pi*sqrt(0.0025)
3. T = 2*pi * 0.05 = **0.314 s**

### Example 2: Simple Pendulum
**Problem**: What length pendulum has a period of 2.0 s on Earth (g = 9.8 m/s^2)?

**Solution**:
1. Use T = 2*pi*sqrt(L/g), solve for L
2. T^2 = 4*pi^2 * L/g
3. L = g*T^2 / (4*pi^2) = 9.8 * 4 / (4*pi^2)
4. L = 39.2 / 39.48 = **0.993 m** (approximately 1 m)

### Example 3: Energy in SHM
**Problem**: A 2 kg mass on a spring (k = 50 N/m) oscillates with amplitude 0.1 m. What is the maximum speed?

**Solution**:
1. Total energy: E = (1/2)*k*A^2 = (1/2)(50)(0.1)^2 = 0.25 J
2. At equilibrium, all energy is kinetic: E = (1/2)*m*v_max^2
3. v_max = sqrt(2E/m) = sqrt(2*0.25/2) = sqrt(0.25) = **0.5 m/s**

Alternative: v_max = A*omega = A*sqrt(k/m) = 0.1*sqrt(50/2) = 0.1*5 = **0.5 m/s**

### Example 4: Position and Velocity
**Problem**: A spring system has omega = 4 rad/s and A = 0.2 m. If x = A at t = 0, what is the position and velocity at t = 0.5 s?

**Solution**:
1. Position: x = A*cos(omega*t) = 0.2*cos(4*0.5) = 0.2*cos(2) = 0.2*(-0.416) = **-0.083 m**
2. Velocity: v = -A*omega*sin(omega*t) = -0.2*4*sin(2) = -0.8*(0.909) = **-0.727 m/s**

## Explanation Patterns

1. **Identify the type of oscillator**: Is it a spring, pendulum, or other system?
2. **Determine given quantities**: What do you know (m, k, L, A, T, f)?
3. **Choose the appropriate period formula**:
   - Spring: T = 2*pi*sqrt(m/k)
   - Pendulum: T = 2*pi*sqrt(L/g)
4. **For kinematics problems**: Write x(t), then differentiate for v(t) and a(t)
5. **For energy problems**: Use E = (1/2)*k*A^2 and energy conservation
6. **Check your answer**: Does the period make sense? Are units correct?

## Common Problem Types

1. **Period/frequency calculations**: Find T or f given system parameters
2. **Mass-spring problems**: Apply T = 2*pi*sqrt(m/k) or solve for m or k
3. **Pendulum problems**: Apply T = 2*pi*sqrt(L/g) or solve for L; compare periods on different planets
4. **Maximum velocity/acceleration**: Use v_max = A*omega and a_max = A*omega^2
5. **Position at a given time**: Use x = A*cos(omega*t) with correct initial conditions
6. **Energy problems**: Apply conservation of energy between positions
7. **Velocity at a given position**: Use energy conservation: (1/2)*m*v^2 + (1/2)*k*x^2 = (1/2)*k*A^2
8. **Damping effects**: Qualitative understanding of amplitude decay
