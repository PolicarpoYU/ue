import numpy as np
import matplotlib.pyplot as plt
# Import the ulianovellipse library for Ulianov elliptical functions
from ulianovellipse import eu

def test_arctanuell_ue():
    """
    Tests the accuracy of the arctanuell_ue function across a range of alpha values.

    This function checks the precision of converting between coordinates (x, y) and (alpha, Ue) on the Ulianov ellipse.
    """
    # List of alpha values (in degrees) to test
    alpha_values = [5.12345, 30.1234, 45.12345, 60.12345, 90.12345, 125.12345, 180.12345, 270.12345, 339.12345, 355.12345]
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
