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
