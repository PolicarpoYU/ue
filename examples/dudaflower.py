import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def Duda_Flower(a, b, ptn=24, gp=0, cla1="green", cla2="red", num_flor_user=0):
    """
    Plots a simplified "Duda Flower" pattern using standard and Ulianov elliptical functions.

    Parameters:
    a (float): Semi-major axis length for the ellipses.
    b (float): Semi-minor axis length for the ellipses.
    ptn (int): Number of petals (default is 24).
    gp (float): Rotation angle in degrees for the petals (default is 0).
    cla1 (str): Color for standard ellipses (default is "green").
    cla2 (str): Color for Ulianov ellipses (default is "red").
    num_flor_user (int): Identifier for the flower pattern (default is 0).

    The function generates a plot of a flower pattern with two layers of ellipses.
    """
    # Ensure a >= b for correct ellipse plotting
    if b > a:
        a, b = b, a  

    # Set up the plot
    plt.figure(figsize=(10, 6))

    # First layer with standard ellipses
    for i in range(ptn):
        ang_ellipse = (gp / 180 * np.pi / ptn + (2 * np.pi / ptn * i)) * 180 / np.pi
        SE_x, SE_y = eu.ellipse_ab(a, b, ang_ellipse_degrees=ang_ellipse)
        if cla1 != "none":
            plt.plot(np.array(SE_x), SE_y, color=cla1)

    # Second layer with Ulianov ellipses
    for i in range(ptn):
        ang_ellipse = (gp / 180 * np.pi / ptn + (2 * np.pi / ptn * i)) * 180 / np.pi
        UE_x, UE_y = eu.ulianov_ellipse_ab(a, b, ang_ellipse_degrees=ang_ellipse)
        if cla2 != "none":
            plt.plot(np.array(UE_x), UE_y, color=cla2)

    # Finalize plot settings
    plt.ylabel("y")
    plt.xlabel("x")
    plt.axis('off')
    plt.axis('equal')
    plt.title(f"Duda Flower N$^0${num_flor_user}: a={a},b={b},NP={ptn},G={gp}$^o$,C1={cla1},C2={cla2}")
    plt.savefig(f"DudaFlower{num_flor_user}.jpg")  # Save the plot as an image
    plt.show()

# Example usage with different parameters for each flower
Duda_Flower(a=80, b=60, ptn=36, gp=0, cla1='green', cla2='red', num_flor_user=124)
Duda_Flower(a=240, b=30, ptn=24, gp=180, cla1='red', cla2='blue', num_flor_user=102)
Duda_Flower(a=80, b=30, ptn=24, gp=0, cla1='green', cla2='red', num_flor_user=103)
Duda_Flower(a=50, b=40, ptn=24, gp=0, cla1='green', cla2='blue', num_flor_user=104)
Duda_Flower(a=80, b=30, ptn=24, gp=0, cla1='green', cla2='red', num_flor_user=105)
Duda_Flower(a=240, b=20, ptn=36, gp=180, cla1='green', cla2='red', num_flor_user=177)
Duda_Flower(a=240, b=30, ptn=24, gp=180, cla1='green', cla2='blue', num_flor_user=107)
Duda_Flower(a=80, b=30, ptn=24, gp=180, cla1='green', cla2='red', num_flor_user=108)
Duda_Flower(a=50, b=40, ptn=24, gp=180, cla1='green', cla2='blue', num_flor_user=109)
Duda_Flower(a=80, b=30, ptn=24, gp=180, cla1='green', cla2='blue', num_flor_user=133)
