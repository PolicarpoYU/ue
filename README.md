# UlianovEllipse

## Overview

The **UlianovEllipse** library provides a comprehensive set of functions and classes for working with Ulianov elliptical functions. These functions are utilized in the Ulianov Orbital Model (UOM) to analyze and model elliptical orbits. The library also includes general utilities for handling and transforming elliptical shapes in various applications.

## Key Features

- **Ulianov Elliptical Cosine and Sine Functions:** These functions (`cosuell`, `sinuell`) are used to calculate the cosine and sine of an angle for Ulianov ellipses, which differ from standard trigonometric functions.
- **Parameter Conversion:** Methods like `calc_ue` and `calc_ab` convert between different sets of parameters (e.g., semi-major and semi-minor axes, Ulianov parameters).
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
    R0, Ue = eu.calc_ue(a, b)

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

![Result of this example](images//ExampleTwoEll.png)

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
  - `R0`, `Ue`: Parameters for the Ulianov ellipse calculated using the function `calc_ue`.
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

1. ![PoliFlower N°24](images//polianaflower1.png)
2. ![PoliFlower N°77](images//polianaflower2.png)
3. ![PoliFlower N°5](images//polianaflower.png)


## Example of Use 03:
### Drawing Ellipses, Parabolas, and Hyperboles

This example demonstrates how to use the `ulianovellipse` library to plot a series of Ulianov ellipses, along with parabolic and hyperbolic paths, by varying the Ulianov Ellipse Parameter (\( U_e \)).

```python
import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def all_ellipses(Ue_min=0, Ue_max=3, passo=0.1, esc=50, R0=1000):
    """
    Plots a series of Ulianov ellipses for a range of Ue values.

    Parameters:
    Ue_min (float): Minimum value of Ulianov Ellipse Parameter (default is 0).
    Ue_max (float): Maximum value of Ulianov Ellipse Parameter (default is 3).
    passo (float): Step size for incrementing Ue (default is 0.1).
    esc (float): Scale factor for the plot limits (default is 50).
    R0 (float): Minimum orbital distance, a fixed parameter for all ellipses (default is 1000).

    The function generates a plot with ellipses corresponding to different Ue values, each having a unique color.
    """
    # Initialize the plot
    plt.figure(figsize=(10, 6))
    
    # Generate Ue values from Ue_min to Ue_max with the given step size
    Ue_values = np.arange(Ue_min, Ue_max + passo, passo)
    
    for Ue in Ue_values:
        print(f"Drawing Ellipse Ue={Ue:.02}")
        # Calculate the x and y coordinates of the Ulianov ellipse for the given Ue
        UE_x, UE_y = eu.ulianov_ellipse_ue(R0, Ue, ang_ini_degrees=-1800, ang_fim_degrees=1800)
        
        # Choose colors and labels based on specific Ue values
        if abs(Ue - 1) < 0.01:
            plt.plot(UE_x, UE_y, color="red", label="Ue=1")
        elif abs(Ue - 2) < 0.01:
            plt.plot(UE_x, UE_y, color="red", label="Ue=2")
        elif Ue > 2:
            plt.plot(UE_x, UE_y, color="black", label="")
        elif Ue > 1:
            plt.plot(UE_x, UE_y, color="blue", label="")
        else:        
            plt.plot(UE_x, UE_y, color="green", label="")

    # Adjust the plot's axis limits and scale
    plt.axis('equal')
    plt.xlim(-esc * R0, 2 * R0)
    plt.ylim(-esc * R0, esc * R0)
    
    # Set plot labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Ulianov Ellipse for different Ue values')
    plt.grid(True)
    plt.show()

# Call the function to generate the plot with default parameters
all_ellipses()
```

### Explanation of the Code

**Imports:**

- `numpy` and `matplotlib.pyplot` are standard libraries for numerical calculations and plotting in Python.
- `eu` is imported from the `ulianovellipse` package, providing functions to compute parameters for the Ulianov ellipse.

**Function `all_ellipses`:**

- **Parameters:**
  - `Ue_min`, `Ue_max`: Define the range of Ulianov Ellipse Parameter values to plot.
  - `passo`: Step size for the increment of \( U_e \) values.
  - `esc`: Scale factor to adjust the plot limits.
  - `R0`: Fixed parameter representing the minimum orbital distance for all ellipses.

- **Calculations:**
  - `Ue_values`: Array of \( U_e \) values ranging from `Ue_min` to `Ue_max` with step size `passo`.
  - For each \( U_e \) value, the function calculates the coordinates of the Ulianov ellipse using `ulianov_ellipse_ue`.

- **Plotting:**
  - The ellipses are plotted with different colors:
    - Green for \( U_e < 1 \)
    - Blue for \( 1 < U_e < 2 \)
    - Black for \( U_e > 2 \)
    - Red highlights are added for specific \( U_e \) values, such as 1 and 2.
  - The plot includes labels for the axes, a title, and a grid for better visualization.

**Visual Example:**

The plot shows various conic sections (ellipses, parabolas, hyperbolas) depending on the value of \( U_e \). These curves are essential in orbital mechanics and physics, representing different types of orbital paths.

![Result of this example](images//allellipses.png)

This example showcases the versatility of the `ulianovellipse` library in visualizing different conic sections, demonstrating the unique properties of the Ulianov Ellipse Parameter.

## Example of Use 04:  
### Drawing Incomplete, Bicolor, and Rotated Ellipses

This example illustrates how to use the `ulianovellipse` library to draw incomplete, bicolor, and rotated ellipses. The functions provided allow for the visualization of various sections of ellipses with different rotations and color schemes.

```python
import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def Plot_Two_Ellipses_rotate_degrees_ab(a, b, ang_ellipse=0):
    """
    Plots two ellipses (standard and Ulianov) with given semi-major (a) and semi-minor (b) axes,
    rotated by a specified angle in degrees.

    Parameters:
    a (float): Semi-major axis length.
    b (float): Semi-minor axis length.
    ang_ellipse (float): Rotation angle in degrees for the ellipses.

    The function generates a plot showing both the standard and Ulianov ellipses.
    """
    plt.figure(figsize=(10, 6))
    UE_x, UE_y = eu.ulianov_ellipse_ab(a, b, ang_ellipse_degrees=ang_ellipse)
    SE_x, SE_y = eu.ellipse_ab(a, b, ang_ellipse_degrees=ang_ellipse)
    plt.plot(np.array(SE_x), SE_y, color="red", label='Standard')
    plt.plot(np.array(UE_x), UE_y, color="blue", label='Ulianov')
    plt.legend()
    plt.ylabel("y")
    plt.xlabel("x")
    plt.axis('equal')
    plt.title(f"Ellipses a={a}, b={b}, angle rotate={ang_ellipse}°")
    plt.grid()
    plt.show()

def Plot_Two_Ellipses_rotate_rad_ue(R0, Ue, ang_ellipse=0):
```
### Explanation of the Code

**Function `Plot_Two_Ellipses_rotate_degrees_ab`:**

- **Description:** Plots two ellipses (standard and Ulianov) with given semi-major axis \( a \) and semi-minor axis \( b \), rotated by a specified angle in degrees. The ellipses are plotted in different colors to facilitate comparison.
- **Parameters:**
  - `a`: Length of the semi-major axis.
  - `b`: Length of the semi-minor axis.
  - `ang_ellipse`: Rotation angle in degrees.

**Function `Plot_Two_Ellipses_rotate_rad_ue`:**

- **Description:** Plots two ellipses (standard and Ulianov) using the parameters \( R_0 \) and \( U_e \), rotated by a specified angle in radians. This function is useful for visualizing ellipses with different Ulianov parameters.
- **Parameters:**
  - `R0`: Minimum orbital distance for the Ulianov ellipse.
  - `Ue`: Ulianov Ellipse Parameter.
  - `ang_ellipse`: Rotation angle in radians.

**Function `Plot_Two_Ellipses_incomplete`:**

- **Description:** Plots incomplete segments of two ellipses (standard and Ulianov) with semi-major axis \( a \) and semi-minor axis \( b \), rotated by a specified angle in degrees. The segments are drawn in different colors, highlighting various parts of the ellipses.
- **Parameters:**
  - `a`: Length of the semi-major axis.
  - `b`: Length of the semi-minor axis.
  - `ang_ellipse`: Rotation angle in degrees.

### Visualization

The following image demonstrates the output of the three functions with different parameters, highlighting the versatility of the Ulianov elliptical model for creating complex visualizations of ellipses with rotations and incomplete sections.

![Result of this example](images//incompleteroatateellipses.png)

This figure illustrates various elliptical shapes and transformations, showcasing the unique capabilities of the `ulianovellipse` package for detailed and customizable visualizations.


## Example of Use 05:
### Testing Resolution Errors in the Function `arctanuell`

The `arctanuell` function is a key component of the **UlianovEllipse** library, used to calculate the angle and distance for a given set of coordinates and Ulianov Ellipse parameter \( U_e \). This function is particularly useful in applications where precise calculations of elliptical parameters are required.

### Function Definition:
```python
def arctanuell(self, y, x, Ue, precision=1E-10):
    """
    Calculates the Ulianov Ellipse arctangent for a given x and y coordinate and Ue.

    Parameters:
    y (float): Y-coordinate.
    x (float): X-coordinate.
    Ue (float): Ellipse parameter Ue (ranges from 0.500000000000002 to 1.99999999999999).
    precision (float): Desired precision for the calculation.
    msg (int): Verbosity level for debugging messages.

    Returns:
    tuple: (angle, R0)
    angle (float): Calculated angle in radians.
    R0 (float): Calculated R0 value.
    """
    return ang_final, R0n
```

This function iteratively finds the angle and distance using the \( x \) and \( y \) coordinates and the Ulianov Ellipse parameter \( U_e \). Due to the iterative nature of the function, there is a rounding error of the order of \( 10^{-12} \% \). The accuracy and reliability of the `arctanuell` function can be tested using a specialized testing routine, as shown below:

### Testing Routine:
The `test_arctanuell` function assesses the accuracy of the `arctanuell` function by comparing the calculated and original angles and distances for various \( U_e \) values.

```python
import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def test_arctanuell(lim=0):
    Ue_values = [1.2, 1.5, 1.8, 1.9, 1.95, 1.99, 1.999, 1.9999, 1.99999, 1.999999, 1.99999999, eu.Lim_Ue]
    nump = 5000
    R0 = 10000
    all_alpha = []
    all_error_alpha = []
    all_error_R0 = []

    if lim == 0:
        lim = len(Ue_values)
    if lim > len(Ue_values):
        lim = len(Ue_values)
        
    for i in range(lim):
        Ue = Ue_values[i]
        print(f"Testing arctanuell for Ue={Ue}")
        alpha = []
        error_alpha = []
        error_R0 = []

        maxerro = 0
        maxerroR0 = 0
        maxct = 0
        mostra = 0
        
        for t in range(nump):
            ag = (t) * np.pi * 2 / nump
            aggr = ag * 180 / np.pi
            alpha.append(aggr)
            ex = R0 * eu.cosuell(ag, Ue)
            ey = R0 * eu.sinuell(ag, Ue)
            agn, R0n = eu.arctanuell(ey, ex, Ue)
            if eu.last_functon_steps() > maxct:
                maxct = eu.last_functon_steps()
            agngr = agn * 180 / np.pi
            errogr = (agngr - aggr)
            errorR0 = (R0 - R0n) / R0 * 100
            if abs(errogr) > abs(maxerro):
                maxerro = errogr
                angerromax = aggr
            if abs(errorR0) > abs(maxerroR0):
                maxerroR0 = errogr
                angerromaxR0 = aggr
            error_alpha.append(errogr)
            error_R0.append(errorR0)
            mostra += 1
            if mostra > 10:
                mostra = 0
                print(f"\rag gr={aggr:.4f}, agn gr={agngr:.4f}, errogr ={errogr:.6e} ", end="")
             
        all_alpha.append(alpha)
        all_error_alpha.append(error_alpha)
        all_error_R0.append(error_R0)
        print(f"\nUe={Ue}, Maxerro Alpha= {maxerro} in angle {angerromax}")
        print(f"\nMaxerro R0 = {errorR0} in angle {angerromaxR0}, Max Steps ={maxct}")

    plt.figure(figsize=(10, 6))
    for i in range(lim):
        plt.plot(all_alpha[i], all_error_alpha[i], label=f'Ue={Ue_values[i]}')
    plt.xlabel('Original Alpha')
    plt.ylabel('Error in Alpha (degrees)')
    plt.title(f'arctanuell Alpha Error for Different Ue Values')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    for i in range(lim):
        plt.plot(all_alpha[i], all_error_R0[i], label=f'Ue={Ue_values[i]}')
    plt.xlabel('Original Alpha')
    plt.ylabel('Error in R0 (%)')
    plt.title(f'arctanuell R0 Error for Different Ue Values')
    plt.legend()
    plt.grid(True)
    plt.show()

# Test the function with a specific number of Ue values
test_arctanuell(4)
```

### Explanation of the Code

The function `test_arctanuell` is designed to evaluate the accuracy of the `arctanuell` function from the `ulianovellipse` library. This function calculates the inverse of the elliptical functions (`cosuell` and `sinuell`) for given \( x \) and \( y \) coordinates, returning the angle (\( \alpha \)) and distance (\( R_0 \)).

**Parameters:**
- `lim`: Limits the number of different \( U_e \) values to be tested. If not specified, all values in the `Ue_values` list are used.

**Core Testing Process:**
1. **Setting up `Ue` values:** The function defines a range of \( U_e \) values, including values approaching the limiting value `eu.Lim_Ue`.
2. **Generating Test Data:** For each \( U_e \) value, the function generates several points on the ellipse:
   - `ex` and `ey` coordinates are calculated using the `cosuell` and `sinuell` functions for angles from 0 to 360 degrees.
   - These coordinates are then passed to the `arctanuell` function, which calculates the corresponding angle (\( \alpha \)) and distance (\( R_0 \)).
3. **Calculating Errors:** The differences between the original and calculated angles (`errogr`) and the original and calculated distances (`errorR0`) are computed.
4. **Tracking Maximum Errors:** The maximum errors for angle and distance, along with the corresponding angles, are recorded for each \( U_e \).

**Visualization:**
The function generates two plots:
1. **Error in Alpha:** Plots the error in the angle calculation (\( \alpha \)) against the original angle for different \( U_e \) values.
2. **Error in \( R_0 \):** Plots the percentage error in the calculated distance \( R_0 \) against the original angle for different \( U_e \) values.

These plots help visualize the accuracy and stability of the `arctanuell` function across a range of \( U_e \) values.

### Heart of the Test

The central part of the test involves generating multiple positions (`ex`, `ey`) for a wide range of angles (0 to 360 degrees) and several \( U_e \) values:

```python
ex = R0 * eu.cosuell(ag, Ue)
ey = R0 * eu.sinuell(ag, Ue)
```

The inverse function `arctanuell` is then used to recover the angle and distance:

```python
agn, R0n = eu.arctanuell(ey, ex, Ue)
```

Finally, two types of errors are calculated:
- **Error in Angle (degrees):** `errogr = (agngr - aggr)`
- **Error in \( R_0 \) (percentage):** `errorR0 = (R0 - R0n) / R0 * 100`
![Result of this example](images//errorarctanuell.png)


This figure illustrates that the errors in the `arctanuell` function are in the range of \(10^{-12}\%\). This level of accuracy is impressive and is consistent with the precision limits of the numpy library. To achieve even more precise results, it would be necessary to use libraries like `mpmath` which allow configurable precision with a large number of decimal places. The next version of the `ulianovellipse` library plans to include an object named `eump` that will use `mpmath` routines instead of numpy, offering precision up to 100 digits.

## Example of Use 06: Testing Resolution Errors in the Function `arctanuell_ue`

The `arctanuell_ue` function is a key component of the **UlianovEllipse** library. It calculates the angle and the Ulianov Ellipse parameter \( U_e \) from given \( x \) and \( y \) coordinates and a reference distance \( R_0 \). This function is essential for accurately determining the properties of an ellipse based on its geometric parameters.

#### Function Definition:
```python
def arctanuell_ue(self, y, x, R0):
    """
    Calculates the Ulianov Ellipse arctangent and Ue value from R0 value.

    Parameters:
    y (float): Y-coordinate.
    x (float): X-coordinate.
    R0 (float): Ellipse parameter R0.
    Ndig (int): Number of digits for refinement (default is 10).

    Returns:
    tuple: (angle, Ue)
    angle (float): Calculated angle in radians.
    Ue (float): Calculated Ue value (ranges from 0.500000000000002 to 1.99999999999999).
    """
    return angulo, Ue
```

This function iteratively finds the angle and \( U_e \) value using the provided \( x \) and \( y \) coordinates, along with the reference distance \( R_0 \). Due to the iterative nature of the function, there may be rounding errors. The accuracy and reliability of the `arctanuell_ue` function can be tested using the following routine:

#### Testing Routine:
The `test_arctanuell_ue` function evaluates the accuracy of the `arctanuell_ue` function by comparing the calculated and original angles and \( U_e \) values for various \( \alpha \) values.

```python
import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def test_arctanuell_ue():
    """
    Tests the accuracy of the arctanuell_ue function across a range of alpha values.

    This function checks the precision of converting between coordinates (x, y) and (alpha, Ue) on the Ulianov ellipse.
    """
    # List of alpha values (in degrees) to test
    alpha_values = [5.12345, 30.1234, 45.12345, 60.12345, 90.12345, 125.12345, 180.12345, 270.12345, 399.12345, 355.12345]
    nump = 100  # Number of points for generating the ellipse
    R0 = 10000  # Reference radius

    all_ue = []  # Store all Ue values tested
    all_error_alpha = []  # Store errors in calculated alpha
    all_error_r0 = []  # Store errors in calculated Ue

    for i in range(len(alpha_values)):
        alpha = alpha_values[i]
        print(f"Testing arctanuell_Ue for alpha={alpha}", end="")
        error_alpha = []  # List to store the angle errors
        error_r0 = []  # List to store the Ue errors
        mat_ue = []  # List to store Ue values for plotting

        maxerro = 0
        maxct = 0
        for j in range(nump):
            Ue = 1 + j * 0.9999999 / nump  # Generate Ue values from 1 to nearly 2
            alpha_rad = alpha * np.pi / 180  # Convert alpha to radians
            print(f"\rTesting arctanuell_Ue for alpha={alpha}, Ue={Ue}", end="")
            mat_ue.append(Ue)
            
            # Compute the x and y coordinates on the Ulianov ellipse for the given angle and Ue
            xi = R0 * eu.cosuell(alpha_rad, Ue)
            yi = R0 * eu.sinuell(alpha_rad, Ue)
            
            # Use the arctanuell_ue function to retrieve the angle and Ue from (yi, xi)
            alpha_med, Ue_med = eu.arctanuell_ue(yi, xi, R0)
            if eu.last_functon_steps() > maxct:
                maxct = eu.last_functon_steps()
            alpha_medgr = alpha_med * 180 / np.pi  # Convert the calculated angle to degrees
            
            # Calculate the error in the calculated angle
            errogr = (alpha - alpha_medgr)
            # Calculate the error in the calculated Ue as a percentage
            errorR0 = (Ue - Ue_med) / Ue * 100
            
            # Track the maximum errors
            if abs(errogr) > abs(maxerro):
                maxerro = errogr
                uemaxerro = Ue
            error_alpha.append(errogr)
            error_r0.append(errorR0)

        all_ue.append(mat_ue)
        all_error_alpha.append(error_alpha)
        all_error_r0.append(error_r0)
        print(f", Maxerro = {maxerro}, Ue maxerro ={uemaxerro}, Max Steps ={maxct}")

    # Plot the errors in the calculated angles
    plt.figure(figsize=(10, 6))
    for i in range(len(alpha_values)):
        plt.plot(all_ue[i], all_error_alpha[i], label=f'alpha={alpha_values[i]}')
    plt.xlabel('Ue')
    plt.ylabel('Error in Alpha (degrees)')
    plt.title(f'arctanuell Alpha Error for Different Alpha Values')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot the errors in the calculated Ue values
    plt.figure(figsize=(10, 6))
    for i in range(len(alpha_values)):
        plt.plot(all_ue[i], all_error_r0[i], label=f'alpha={alpha_values[i]}')
    plt.xlabel('Ue')
    plt.ylabel('Error in Ue (%)')
    plt.title(f'arctanuell Ue Error for Different Alpha Values')
    plt.legend()
    plt.grid(True)
    plt.show()

test_arctanuell_ue()
```

### Explanation of the Code

The `test_arctanuell_ue` function is designed to evaluate the accuracy of the `arctanuell_ue` function. This function calculates the inverse of the elliptical functions (`cosuell` and `sinuell`) for given \( x \) and \( y \) coordinates, returning the angle (\( \alpha \)) and Ulianov Ellipse parameter (\( U_e \)).

**Parameters:**
- **`alpha_values`**: A list of angles in degrees to test the function.
- **`nump`**: Number of points used for generating the ellipse.
- **`R0`**: The reference radius for the ellipse.

**Core Testing Process:**
1. **Setting up \( U_e \) values:** The function defines a range of \( U_e \) values, including values close to the limiting value.
2. **Generating Test Data:** For each \( \alpha \) value, the function generates several points on the ellipse:
   - The coordinates \( x_i \) and \( y_i \) are calculated using `cosuell` and `sinuell` for the given angles and \( U_e \) values.
   - These coordinates are then used in the `arctanuell_ue` function to calculate the angle and \( U_e \).
3. **Calculating Errors:** The differences between the original and calculated angles (`errogr`) and the original and calculated \( U_e \) values (`errorR0`) are computed.
4. **Tracking Maximum Errors:** The maximum errors for angle and \( U_e \), along with the corresponding angles, are recorded.

**Visualization:**
The function generates two plots:
1. **Error in Alpha:** Plots the error in the angle calculation (\( \alpha \)) against the calculated \( U_e \) values.
2. **Error in \( U_e \):** Plots the percentage error in the calculated \( U_e \) values against the original angle for different \( \alpha \) values.

These plots provide insights into the accuracy and stability of the `arctanuell_ue` function across different \( \alpha \) and \( U_e \) values.

### Test Results
The graph produced shows the errors in both alpha and \( U_e \) across different test cases, helping to identify any precision issues or inconsistencies in the function's implementation.

![Result of this example](images//errorarctanuellUe.png)

This figure illustrates that the errors in the `arctanuell_ue` function are in the range of \(10^{-10}\%\). This level of accuracy is impressive and is consistent with the precision limits of the numpy library. To achieve even more precise results, it would be necessary to use libraries like `mpmath` which allow configurable precision with a large number of decimal places. The next version of the `ulianovellipse` library plans to include an object named `eump` that will use `mpmath` routines instead of numpy, offering precision up to 100 digits.

