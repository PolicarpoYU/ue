import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def Poliana_Flower(a, b, R0, Ue, ptn=24, gp=0, cla1="green", cla2="red", clb1="yellow", clb2="blue", num_flor_user=0):
    """
    Plots a "Poliana Flower" pattern using both standard and Ulianov elliptical functions.

    Parameters:
    a (float): Semi-major axis length for the ellipses.
    b (float): Semi-minor axis length for the ellipses.
    R0 (float): Minimum orbital distance for Ulianov ellipses.
    Ue (float): Ulianov Ellipse parameter.
    ptn (int): Number of petals (default is 24).
    gp (float): Rotation angle in degrees for the petals (default is 0).
    cla1 (str): Color for standard ellipses in the first and third flower layers (default is "green").
    cla2 (str): Color for Ulianov ellipses in the first and third flower layers (default is "red").
    clb1 (str): Color for standard ellipses in the second and fourth flower layers (default is "yellow").
    clb2 (str): Color for Ulianov ellipses in the second and fourth flower layers (default is "blue").
    num_flor_user (int): Identifier for the flower pattern (default is 0).

    The function generates a plot of a flower pattern with alternating layers of standard and Ulianov ellipses.
    """
    # Ensure a >= b for correct ellipse plotting
    if b > a:
        a, b = b, a  

    # Set up the plot
    plt.figure(figsize=(10, 6))
    for j in range(4):
        giroEL = 0 
        if j == 1:
            giroEL = gp / 180 * np.pi / ptn  # Calculate the rotation for the petals
        if j == 0 or j == 2:
            Usa_ab=True
            cl1 = cla1 
            cl2 = cla2
        else:     
            Usa_ab=False
            cl1 = clb1
            cl2 = clb2
      
        for i in range(ptn):
            ang_ellipse = (giroEL + (2 * np.pi / ptn * i)) * 180 / np.pi  # Calculate angle for each petal
            if Usa_ab:         
                SE_x, SE_y = eu.ellipse_ab(a, b, ang_ellipse_degrees=ang_ellipse)  # Standard ellipse coordinates
                UE_x, UE_y = eu.ulianov_ellipse_ab(a, b, ang_ellipse_degrees=ang_ellipse)  # Ulianov ellipse coordinates
            else:
                SE_x, SE_y = eu.ellipse_ue(R0, Ue, ang_ellipse_degrees=ang_ellipse)  # Standard ellipse coordinates
                UE_x, UE_y = eu.ulianov_ellipse_ue(R0, Ue,  ang_ellipse_degrees=ang_ellipse)  # Ulianov ellipse coordinates
                
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
    plt.title(f"Poliana Flower N$^0${num_flor_user}: a={a},b={b},R0={R0},Ue={Ue},NP={ptn},G={gp}$^o$,C1={cla1},C2={cla2},C3={clb1},C4={clb2}")
    plt.savefig(f"PolianaFlower{num_flor_user}.jpg")  # Save the plot as an image
    plt.show()

# Example usage with different parameters for each flower
Poliana_Flower(a=80, b=60, R0=31.6, Ue=0.625, ptn=36, gp=0, cla1='green', cla2='red', clb1='black', clb2='blue', num_flor_user=24)
Poliana_Flower(a=240, b=30, R0=7.89, Ue=0.0521, ptn=24, gp=180, cla1='none', cla2='none', clb1='black', clb2='blue', num_flor_user=2)
Poliana_Flower(a=80, b=30, R0=15.5, Ue=0.3535, ptn=24, gp=0, cla1='green', cla2='red', clb1='black', clb2='blue', num_flor_user=3)
Poliana_Flower(a=50, b=40, R0=12.6, Ue=0.512, ptn=24, gp=0, cla1='green', cla2='red', clb1='black', clb2='blue', num_flor_user=4)
Poliana_Flower(a=80, b=30, R0=15.5, Ue=0.3535, ptn=24, gp=0, cla1='green', cla2='red', clb1='black', clb2='blue', num_flor_user=5)
Poliana_Flower(a=240, b=20, R0=4.11, Ue=0.00625, ptn=36, gp=180, cla1='green', cla2='red', clb1='black', clb2='blue', num_flor_user=77)
Poliana_Flower(a=240, b=30, R0=7.89, Ue=0.0521, ptn=24, gp=180, cla1='green', cla2='red', clb1='black', clb2='blue', num_flor_user=7)
Poliana_Flower(a=80, b=30, R0=15.5, Ue=0.3535, ptn=24, gp=180, cla1='green', cla2='red', clb1='black', clb2='blue', num_flor_user=8)
Poliana_Flower(a=50, b=40, R0=12.6, Ue=0.512, ptn=24, gp=180, cla1='green', cla2='red', clb1='black', clb2='blue', num_flor_user=9)
Poliana_Flower(a=80, b=30, R0=15.5, Ue=0.3535, ptn=24, gp=180, cla1='green', cla2='red', clb1='black', clb2='blue', num_flor_user=33)
