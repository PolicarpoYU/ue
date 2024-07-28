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
