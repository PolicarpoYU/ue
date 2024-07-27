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

## Example of use 01:
### Drawing a standard ellipse using the sin(alpha) and cos(aplha) functions and the Ulianov ellipse using the sinuell(alpha,Ue) and cosell(alpha,Ue) functions
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

## Example of use 02:
### Drawing a Poliana Elliptic Flower

The `Poliana_Flower` function creates a beautiful, flower-like pattern using a combination of standard and Ulianov ellipses. The function accepts various parameters to customize the size, number of petals, colors, and rotation of the flower.

```python
import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def Poliana_Flower(a0, b0, a1, b1, ptn=24, gp=0, cla1="green", cla2="red", clb1="yellow", clb2="blue", num_flor_user=0):
    # Ensure a0 >= b0 and a1 >= b1 for the ellipses
    if b0 > a0:
        a0, b0 = b0, a0  
    if b1 > a1:
        a1, b1 = b1, a1  

    # Set up the plot
    plt.figure(figsize=(10, 6))
    for j in range(4):
        giroEL = 0 
        if j == 1:
            giroEL = gp / 180 * np.pi / ptn  # Calculate the rotation for the petals
        if j == 0 or j == 2:
            a = a0
            b = b0
            cl1 = cla1 
            cl2 = cla2
        else:     
            cl1 = clb1
            cl2 = clb2
            a = a1
            b = b1 

        for i in range(ptn):
            ang_ellipse = (giroEL + (2 * np.pi / ptn * i)) * 180 / np.pi  # Calculate angle for each petal
            SE_x, SE_y = eu.ellipse_ab(a, b, ang_ellipse_degrees=ang_ellipse)  # Standard ellipse coordinates
            UE_x, UE_y = eu.ulianov_ellipse_ab(a, b, ang_ellipse_degrees=ang_ellipse)  # Ulianov ellipse coordinates
            if j > 1:  
                if cl1 != "none":
                    plt.plot(np.array(SE_x), SE_y, color=cl1)  # Plot standard ellipse
            else:
                if cl2 != "none":   
                    plt.plot(np.array(UE_x), UE_y, color=cl2)  # Plot Ulianov ellipse

    # Finalize plot settings
    plt.ylabel("y")
    plt.xlabel("x")
    plt.axis('off')
    plt.axis('equal')
    plt.title(f"PoliFlower N$^0${num_flor_user}: a0={a0}, b0={b0}, a1={a1}, b1={b1}, ptn={ptn}, G={gp}$^o$, C1={cla1}, C2={cla2}, C3={clb1}, C4={clb2}")
    plt.savefig(f"PolianaFlower{num_flor_user}.jpg")  # Save the plot as an image
    plt.show()

# Example usage with different parameters for each flower
Poliana_Flower(a0=80, b0=60, a1=30, b1=4, ptn=36, gp=0, cla1="green", cla2="red", clb1="black", clb2="blue", num_flor_user=24)
Poliana_Flower(a0=240, b0=30, a1=90, b1=20, ptn=24, gp=180, cla1="none", cla2="none", clb1="black", clb2="blue", num_flor_user=2)
Poliana_Flower(a0=80, b0=30, a1=60, b1=40, ptn=24, gp=0, cla1="green", cla2="red", clb1="black", clb2="blue", num_flor_user=3)
Poliana_Flower(a0=50, b0=40, a1=55, b1=45, ptn=24, gp=0, cla1="green", cla2="red", clb1="black", clb2="blue", num_flor_user=4)
Poliana_Flower(a0=80, b0=30, a1=60, b1=40, ptn=24, gp=0, cla1="green", cla2="red", clb1="black", clb2="blue", num_flor_user=5)
Poliana_Flower(a0=240, b0=20, a1=80, b1=10, ptn=36, gp=180, cla1="green", cla2="red", clb1="black", clb2="blue", num_flor_user=77)
Poliana_Flower(a0=240, b0=30, a1=90, b1=20, ptn=24, gp=180, cla1="green", cla2="red", clb1="black", clb2="blue", num_flor_user=7)
Poliana_Flower(a0=80, b0=30, a1=60, b1=40, ptn=24, gp=180, cla1="green", cla2="red", clb1="black", clb2="blue", num_flor_user=8)
Poliana_Flower(a0=50, b0=40, a1=55, b1=45, ptn=24, gp=180, cla1="green", cla2="red", clb1="black", clb2="blue", num_flor_user=9)
Poliana_Flower(a0=80, b0=30, a1=60, b1=40, ptn=24, gp=180, cla1="green", cla2="red", clb1="black", clb2="blue", num_flor_user=33)

```

### Explanation of the Code

**Imports:**

- `numpy` and `matplotlib.pyplot` are standard libraries for numerical calculations and plotting in Python.
- `eu` is imported from the `ulianovellipse` package, providing functions to compute parameters for the Ulianov ellipse.

**Function `Poliana_Flower`:**

- **Parameters:**
  - `a0`, `b0`: Semi-major and semi-minor axes of the outer ellipses.
  - `a1`, `b1`: Semi-major and semi-minor axes of the inner ellipses.
  - `ptn`: Number of petals.
  - `gp`: Rotation angle for the petals.
  - `cla1`, `cla2`, `clb1`, `clb2`: Colors for the outer and inner ellipses.

- **Calculations:**
  - `ang_ellipse`: Calculated angle for rotating each ellipse.

- **Plotting:**
  - Ellipses are plotted with specified colors, creating a flower-like pattern.
  - The plot includes the title with parameters used to create the flower.

This example demonstrates how to create a complex, visually appealing pattern using both standard and Ulianov ellipses, highlighting the versatility of the `ulianovellipse` package.

**Visual Examples:**

1. ![PoliFlower N°24](https://github.com/PolicarpoYU/ue/blob/main/polianaflower1.png)
2. ![PoliFlower N°77](https://github.com/PolicarpoYU/ue/blob/main/polianaflower2.png)
3. ![PoliFlower N°5](https://github.com/PolicarpoYU/ue/blob/main/polianaflower.png)







