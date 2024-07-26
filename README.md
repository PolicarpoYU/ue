# UlianovEllipse

## Overview

The **UlianovEllipse** library provides a comprehensive set of functions and classes for working with Ulianov elliptical functions. These functions are utilized in the Ulianov Orbital Model (UOM) to analyze and model elliptical orbits. The library also includes general utilities for handling and transforming elliptical shapes in various applications.

## Key Features

- **Ulianov Elliptical Cosine and Sine Functions:** These functions (`cosuell`, `sinuell`) are used to calculate the cosine and sine of an angle for Ulianov ellipses, which differ from standard trigonometric functions.
- **Parameter Conversion:** Methods like `calc_Ue` and `calc_ab` convert between different sets of parameters (e.g., semi-major and semi-minor axes, Ulianov parameters).
- **Axis Rotation:** The `rotate_axis` function allows for the rotation of coordinates, useful in transforming elliptical data.
- **Elliptical Path Calculations:** Functions such as `ulianov_ellipse_ue` and `ulianov_ellipse_ab` provide tools for calculating points along an ellipse using various parameterizations.

## Getting Started

To use the `UlianovEllipse` library, first ensure you have `numpy` installed, as it is a required dependency. You can install it using pip:

```bash
pip install numpy
pip install ulianovellipse
```

## Example of use:

```python
import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def two_ellipses(a, b, ang_ini_degrees=0, ang_fim_degrees=360, npassos=1000):
    # Calculate the focal distance R0 and the parameter Ue for the Ulianov ellipse
    R0, Ue = eu.calc_Ue(a, b)

    # Generate angles from ang_ini_degrees to ang_fim_degrees
    alpha = np.linspace(ang_ini_degrees * np.pi / 180, ang_fim_degrees * np.pi / 180, npassos)

    # Calculate the coordinates of the Ulianov ellipse
    UE_x = R0 * eu.cosuell(alpha, Ue)
    UE_y = R0 * eu.sinuell(alpha, Ue)

    # Calculate the coordinates of the standard ellipse
    SE_x = a * np.cos(alpha)
    SE_y = b * np.sin(alpha)

    # Plot the ellipses
    plt.figure(figsize=(10, 6))
    plt.plot(np.array(SE_x), SE_y, color="red", label='Standard')
    plt.plot(np.array(UE_x), UE_y, color="blue", label='Ulianov')

    # Add labels and title
    plt.legend()
    plt.ylabel("y")
    plt.xlabel("x")
    plt.axis('equal')
    plt.title(f"Ellipses a={a}, b={b}, R0={R0}, Ue={Ue}")
    plt.grid()
    plt.show()

# Example usage: plotting two ellipses with semi-major axis a=5 and semi-minor axis b=3
two_ellipses(5, 3)
```

![Result of this example](https://github.com/PolicarpoYU/ue/blob/main/ExampleTwoEll.png)

### Explanation of the Code

**Imports:**

- `numpy` and `matplotlib.pyplot` are standard libraries used for numerical calculations and plotting in Python.
- `eu` is imported from the `ulianovellipse` package, providing functions to compute parameters for the Ulianov ellipse.

**Function `two_ellipses`:**

- **Parameters:**
  - `a`, `b`: Semi-major and semi-minor axes of the standard ellipse.
  - `ang_ini_degrees`, `ang_fim_degrees`: The starting and ending angles for generating the ellipses, in degrees.
  - `npassos`: Number of steps for the angle, providing smoothness to the ellipse.

- **Calculations:**
  - `R0`, `Ue`: Parameters for the Ulianov ellipse calculated using the function `calc_Ue`.
  - `alpha`: Array of angles in radians from `ang_ini_degrees` to `ang_fim_degrees`.
  - `UE_x`, `UE_y`: X and Y coordinates for the Ulianov ellipse, calculated using functions `cosuell` and `sinuell`.
  - `SE_x`, `SE_y`: X and Y coordinates for the standard ellipse, calculated using standard trigonometric functions.

- **Plotting:**
  - Two ellipses are plotted on the same figure: the standard ellipse in red and the Ulianov ellipse in blue.
  - The plot includes labels for the axes, a legend, and a title displaying the parameters of the ellipses.

This example demonstrates how to use the `ulianovellipse` package to compare a standard ellipse with an Ulianov ellipse, providing a visual representation of the differences.


