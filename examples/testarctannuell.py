import numpy as np
import matplotlib.pyplot as plt
# Import the ulianovellipse library for Ulianov elliptical functions
from ulianovellipse import eu

def test_arctanuell(lim=0):
    """
    Tests the accuracy of the arctanuell function across a range of Ue values.

    Parameters:
    lim (int): The number of Ue values to test from the list. If set to 0, all values in the list are tested.
    """
    Ue_values = [1.2, 1.5, 1.8, 1.9, 1.95, 1.99, 1.999, 1.9999, 1.99999, 1.999999, 1.99999999, eu.Lim_Ue]
    nump = 5000  # Number of points for generating the ellipse
    R0 = 10000  # Reference radius
    all_alpha = []  # Store all original angles
    all_error_alpha = []  # Store errors in calculated angles
    all_error_R0 = []  # Store errors in calculated R0

    if lim == 0:
        lim = len(Ue_values)
    if lim > len(Ue_values):
        lim = len(Ue_values)
    for i in range(lim):
        Ue = Ue_values[i]
        print(f"Testing arctanuell for Ue={Ue}")
        alpha = []  # List to store the original angles in degrees
        error_alpha = []  # List to store the angle errors
        error_R0 = []  # List to store the R0 errors

        maxerro = 0
        maxerroR0 = 0
        maxct = 0
        mostra = 0
        for t in range(nump):
            ag = (t) * np.pi * 2 / nump  # Calculate the angle in radians
            aggr = ag * 180 / np.pi  # Convert the angle to degrees
            alpha.append(aggr)
            
            # Compute the x and y coordinates on the Ulianov ellipse for the given angle
            ex = R0 * eu.cosuell(ag, Ue)
            ey = R0 * eu.sinuell(ag, Ue)
            
            # Use the arctanuell function to retrieve the angle and R0 from (ey, ex)
            agn, R0n = eu.arctanuell(ey, ex, Ue)
            if eu.last_functon_steps() > maxct:
                maxct = eu.last_functon_steps()
            agngr = agn * 180 / np.pi  # Convert the calculated angle to degrees
            
            # Calculate the error in the calculated angle
            errogr = (agngr - aggr)
            # Calculate the error in the calculated R0 as a percentage
            errorR0 = (R0 - R0n) / R0 * 100
            
            # Track the maximum errors
            if abs(errogr) > abs(maxerro):
                maxerro = errogr
                angerromax = aggr
            if abs(errorR0) > abs(maxerroR0):
                maxerroR0 = errorR0
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
        print(f"\nMaxerro R0 = {maxerroR0} in angle {angerromaxR0}, Max Steps ={maxct}")

    # Plot the errors in the calculated angles
    plt.figure(figsize=(10, 6))
    for i in range(lim):
        plt.plot(all_alpha[i], all_error_alpha[i], label=f'Ue={Ue_values[i]}')
    plt.xlabel('Original Alpha')
    plt.ylabel('Error in Alpha (degrees)')
    plt.title(f'arctanuell Alpha Error for Different Ue Values')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot the errors in the calculated R0 values
    plt.figure(figsize=(10, 6))
    for i in range(lim):
        plt.plot(all_alpha[i], all_error_R0[i], label=f'Ue={Ue_values[i]}')
    plt.xlabel('Original Alpha')
    plt.ylabel('Error in R0 (%)')
    plt.title(f'arctanuell R0 Error for Different Ue Values')
    plt.legend()
    plt.grid(True)
    plt.show()


test_arctanuell(4)
