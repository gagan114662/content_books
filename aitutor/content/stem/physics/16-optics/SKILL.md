---
id: optics
subject: physics
display_name: Optics
description: |
  Covers the behavior of light including reflection, refraction, and image formation by mirrors and lenses.
  Use when students need to understand how light interacts with surfaces, apply Snell's law, calculate critical angles,
  or solve mirror and lens problems using the thin lens/mirror equation.

grade_band: 9-12
khan_tags: [physics, optics, reflection, refraction, snells-law, mirrors, lenses, magnification, total-internal-reflection]
standards:
  - NGSS.HS-PS4-3
  - NGSS.HS-PS4-5

objectives:
  - Apply the law of reflection (angle of incidence = angle of reflection)
  - Use Snell's law to calculate refraction angles (n1*sin(theta1) = n2*sin(theta2))
  - Calculate critical angle and predict total internal reflection
  - Distinguish between plane, concave, and convex mirrors
  - Distinguish between converging (convex) and diverging (concave) lenses
  - Apply the mirror/lens equation (1/f = 1/do + 1/di)
  - Calculate magnification using m = -di/do
  - Determine image characteristics (real/virtual, upright/inverted, magnified/diminished)

prerequisites:
  - waves

estimated_time_minutes: 75

validator:
  type: numeric_solver
  config:
    unit_library: physics
    default_tolerance: 0.02
    require_units: true

sources:
  - name: OpenStax College Physics
    chapter: 25-27
    url: https://openstax.org/books/college-physics/pages/25-introduction-to-geometric-optics
    license: CC-BY-4.0
---

# Optics

## Misconceptions

| Misconception | Correction |
|--------------|------------|
| "Light bends toward the normal when entering a less dense medium" | Light bends away from the normal when entering a less dense (lower n) medium |
| "Total internal reflection can occur when light goes from air to glass" | TIR only occurs when light travels from higher to lower refractive index |
| "Concave mirrors always produce smaller images" | Concave mirrors can produce magnified images when object is inside focal point |
| "Virtual images cannot be seen" | Virtual images can be seen; they just cannot be projected onto a screen |
| "The focal length of a mirror depends on the object distance" | Focal length is a property of the mirror/lens geometry only |
| "Magnification is always positive" | Magnification sign indicates orientation: negative = inverted, positive = upright |

## Key Concepts

### Reflection

**Law of Reflection**:
- Angle of incidence = Angle of reflection
- theta_i = theta_r
- Angles measured from the normal (perpendicular to surface)

**Types of Reflection**:
- Specular reflection: Smooth surfaces, parallel rays remain parallel
- Diffuse reflection: Rough surfaces, parallel rays scatter in many directions

### Refraction

**Snell's Law**:
- n_1 * sin(theta_1) = n_2 * sin(theta_2)
- n = refractive index (n = c/v where c is speed of light in vacuum)
- Light bends toward the normal when entering a denser medium (higher n)
- Light bends away from the normal when entering a less dense medium (lower n)

**Common Refractive Indices**:
- Vacuum: n = 1.00
- Air: n = 1.00 (approximately)
- Water: n = 1.33
- Glass: n = 1.50 (typical)
- Diamond: n = 2.42

### Total Internal Reflection

**Critical Angle**:
- Occurs when light travels from higher n to lower n medium
- At critical angle, refracted ray travels along the boundary (theta_2 = 90 degrees)
- sin(theta_c) = n_2 / n_1 (where n_1 > n_2)
- For angles greater than critical angle: total internal reflection

**Applications**:
- Fiber optics
- Diamond brilliance
- Prisms in binoculars

### Mirrors

**Plane Mirrors**:
- Image is virtual, upright, same size
- Image distance = object distance (behind mirror)
- Magnification = +1

**Concave Mirrors (Converging)**:
- Center of curvature (C) at distance R from mirror
- Focal point (F) at distance f = R/2 from mirror
- Real, inverted images when object beyond F
- Virtual, upright, magnified images when object inside F

**Convex Mirrors (Diverging)**:
- Focal point behind mirror (virtual focus)
- Always produce virtual, upright, diminished images
- Used for wide field of view (car side mirrors)

### Lenses

**Converging (Convex) Lenses**:
- Thicker in middle than at edges
- Real focus on opposite side from object
- Similar behavior to concave mirrors

**Diverging (Concave) Lenses**:
- Thinner in middle than at edges
- Virtual focus on same side as object
- Always produce virtual, upright, diminished images

### Mirror and Lens Equation

**The Thin Lens/Mirror Equation**:
- 1/f = 1/d_o + 1/d_i
- f = focal length
- d_o = object distance (always positive for real objects)
- d_i = image distance

**Sign Conventions**:
- Mirrors: d_i positive = in front of mirror (real), d_i negative = behind mirror (virtual)
- Lenses: d_i positive = opposite side from object (real), d_i negative = same side as object (virtual)
- Converging: f positive
- Diverging: f negative

### Magnification

**Magnification Equation**:
- m = -d_i / d_o = h_i / h_o
- h_i = image height, h_o = object height
- |m| > 1: magnified
- |m| < 1: diminished
- m > 0: upright (virtual image)
- m < 0: inverted (real image)

### Image Characteristics

**Real Images**:
- Form where light rays actually converge
- Can be projected onto a screen
- Always inverted (for single lens/mirror)
- d_i is positive

**Virtual Images**:
- Form where light rays appear to diverge from
- Cannot be projected onto a screen
- Always upright (for single lens/mirror)
- d_i is negative

## Equations

```
[1] theta_i = theta_r (law of reflection)
[2] n_1 * sin(theta_1) = n_2 * sin(theta_2) (Snell's law)
[3] sin(theta_c) = n_2 / n_1 (critical angle, n_1 > n_2)
[4] 1/f = 1/d_o + 1/d_i (mirror/lens equation)
[5] m = -d_i / d_o (magnification)
[6] m = h_i / h_o (magnification from heights)
[7] f = R/2 (focal length of spherical mirror)
[8] n = c/v (refractive index definition)
```

## Worked Examples

### Example 1: Snell's Law
**Problem**: Light travels from air (n=1.00) into glass (n=1.50) at an angle of 30 degrees from the normal. What is the angle of refraction?

**Solution**:
1. Use Snell's law: n_1 * sin(theta_1) = n_2 * sin(theta_2)
2. 1.00 * sin(30) = 1.50 * sin(theta_2)
3. 0.50 = 1.50 * sin(theta_2)
4. sin(theta_2) = 0.333
5. theta_2 = **19.5 degrees**

### Example 2: Critical Angle
**Problem**: What is the critical angle for light traveling from water (n=1.33) to air (n=1.00)?

**Solution**:
1. Use: sin(theta_c) = n_2 / n_1
2. sin(theta_c) = 1.00 / 1.33 = 0.752
3. theta_c = **48.8 degrees**

### Example 3: Concave Mirror
**Problem**: An object is placed 30 cm from a concave mirror with focal length 20 cm. Find the image distance and magnification.

**Solution**:
1. Use mirror equation: 1/f = 1/d_o + 1/d_i
2. 1/20 = 1/30 + 1/d_i
3. 1/d_i = 1/20 - 1/30 = 3/60 - 2/60 = 1/60
4. d_i = **60 cm** (positive, so real image)
5. m = -d_i/d_o = -60/30 = **-2** (inverted, magnified)

### Example 4: Converging Lens
**Problem**: A converging lens has a focal length of 15 cm. An object is placed 10 cm from the lens. Where is the image and what are its characteristics?

**Solution**:
1. Use lens equation: 1/f = 1/d_o + 1/d_i
2. 1/15 = 1/10 + 1/d_i
3. 1/d_i = 1/15 - 1/10 = 2/30 - 3/30 = -1/30
4. d_i = **-30 cm** (negative, so virtual image on same side as object)
5. m = -d_i/d_o = -(-30)/10 = **+3** (upright, magnified)
6. Image is virtual, upright, and magnified

### Example 5: Magnification
**Problem**: An object 5 cm tall is placed 25 cm from a lens. The image forms 50 cm from the lens on the opposite side. What is the image height?

**Solution**:
1. Calculate magnification: m = -d_i/d_o = -50/25 = -2
2. Use m = h_i/h_o: h_i = m * h_o = -2 * 5 = **-10 cm**
3. The negative sign indicates the image is inverted
4. The image is 10 cm tall and inverted

## Explanation Patterns

1. **Draw a ray diagram** - Always start with a sketch showing object, optical element, and principal rays
2. **Identify the type** - Is it a mirror or lens? Converging or diverging?
3. **Apply sign conventions** - Be careful with positive/negative for f, d_o, d_i
4. **Use appropriate equations** - Mirror/lens equation for distances, magnification for size/orientation
5. **Interpret the results** - Positive/negative d_i tells you real/virtual, sign of m tells you orientation
6. **Check reasonableness** - Does the image location and type match the ray diagram?

## Common Problem Types

1. **Snell's law calculations**: Finding refraction angles
2. **Critical angle problems**: Calculating when TIR occurs
3. **Mirror problems**: Finding image distance and magnification
4. **Lens problems**: Finding image distance and magnification
5. **Image characterization**: Determining if real/virtual, upright/inverted, magnified/diminished
6. **Combined problems**: Multi-step problems involving both equations
7. **Ray diagram interpretation**: Understanding image formation from diagrams
