import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def Salete_Flower(a, b, R0, Ue, ptn=24, gp=0, cla1="green", cla2="red", num_flor_user=0):
    """
    Plots a "Salete Flower" pattern using standard elliptical functions for the first layer and Ulianov elliptical functions for the second layer.

    Parameters:
    a (float): Semi-major axis length for the first layer ellipses.
    b (float): Semi-minor axis length for the first layer ellipses.
    R0 (float): Minimum orbital distance for the Ulianov ellipses.
    Ue (float): Ulianov Ellipse Parameter for the Ulianov ellipses.
    ptn (int): Number of petals (default is 24).
    gp (float): Rotation angle in degrees for the petals (default is 0).
    cla1 (str): Color for standard ellipses (default is "green").
    cla2 (str): Color for Ulianov ellipses (default is "red").
    num_flor_user (int): Identifier for the flower pattern (default is 0).

    The function generates a plot of a flower pattern with two layers: one using standard ellipses and the other using Ulianov ellipses.
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
        UE_x, UE_y = eu.ulianov_ellipse_ue(R0, Ue, ang_ellipse_degrees=ang_ellipse)
        if cla2 != "none":
            plt.plot(np.array(UE_x), UE_y, color=cla2)

    # Finalize plot settings
    plt.ylabel("y")
    plt.xlabel("x")
    plt.axis('off')
    plt.axis('equal')
    plt.title(f"Salete Flower N$^0${num_flor_user}: a={a},b={b},R0={R0},Ue={Ue},NP={ptn},G={gp}$^o$,C1={cla1},C2={cla2}")
    plt.savefig(f"SaleteFlower{num_flor_user}.jpg")  # Save the plot as an image
    plt.show()

# Example usage with different parameters for each flower
Salete_Flower(a=80, b=60, R0=31.6, Ue=1.625, ptn=36, gp=0, cla1='green', cla2='red', num_flor_user=224)
Salete_Flower(a=240, b=30, R0=7.89, Ue=1.5521, ptn=24, gp=180, cla1='red', cla2='blue', num_flor_user=202)
Salete_Flower(a=80, b=30, R0=15.5, Ue=1.3535, ptn=24, gp=0, cla1='green', cla2='red', num_flor_user=203)
Salete_Flower(a=50, b=40, R0=12.6, Ue=1.512, ptn=24, gp=0, cla1='green', cla2='red', num_flor_user=204)
Salete_Flower(a=80, b=30, R0=15.5, Ue=1.8535, ptn=24, gp=0, cla1='green', cla2='red', num_flor_user=205)
Salete_Flower(a=240, b=20, R0=40.11, Ue=1.625, ptn=36, gp=180, cla1='green', cla2='red', num_flor_user=277)
Salete_Flower(a=240, b=30, R0=70.89, Ue=1.521, ptn=24, gp=180, cla1='green', cla2='red', num_flor_user=207)
Salete_Flower(a=80, b=30, R0=15.5, Ue=1.3535, ptn=24, gp=180, cla1='green', cla2='red', num_flor_user=208)
Salete_Flower(a=50, b=40, R0=12.6, Ue=1.512, ptn=24, gp=180, cla1='green', cla2='red', num_flor_user=209)
Salete_Flower(a=80, b=30, R0=15.5, Ue=1.3535, ptn=24, gp=180, cla1='green', cla2='red', num_flor_user=233)
