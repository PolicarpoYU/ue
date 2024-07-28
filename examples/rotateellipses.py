import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu

def Plot_Two_Ellipses_rotate_degrees_ab(a, b, ang_ellipse=0):
    """
    Plots two ellipses (standard and Ulianov) with the given semi-major (a) and semi-minor (b) axes,
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
    """
    Plots two ellipses (standard and Ulianov) using the parameters R0 and Ue, rotated by a specified
    angle in radians.

    Parameters:
    R0 (float): Minimum orbital distance for the Ulianov ellipse.
    Ue (float): Ulianov Ellipse Parameter.
    ang_ellipse (float): Rotation angle in radians for the ellipses.

    The function generates a plot showing both the standard and Ulianov ellipses.
    """
    plt.figure(figsize=(10, 6))
    UE_x, UE_y = eu.ulianov_ellipse_ue(R0, Ue, ang_ellipse_rad=ang_ellipse)
    SE_x, SE_y = eu.ellipse_ue(R0, Ue, ang_ellipse_rad=ang_ellipse)
    plt.plot(np.array(SE_x), SE_y, color="red", label='Standard')
    plt.plot(np.array(UE_x), UE_y, color="blue", label='Ulianov')
    plt.legend()
    plt.ylabel("y")
    plt.xlabel("x")
    plt.axis('equal')
    plt.title(f"Ellipses R0={R0}, Ue={Ue}, angle={ang_ellipse*180/np.pi}°")
    plt.grid()
    plt.show()

def Plot_Two_Ellipses_incomplete(a, b, ang_ellipse=0):
    """
    Plots incomplete segments of two ellipses (standard and Ulianov) with the given semi-major (a) 
    and semi-minor (b) axes, rotated by a specified angle in degrees. The ellipses are drawn in 
    different color segments.

    Parameters:
    a (float): Semi-major axis length.
    b (float): Semi-minor axis length.
    ang_ellipse (float): Rotation angle in degrees for the ellipses.

    The function generates a plot showing segments of the standard and Ulianov ellipses in different colors.
    """
    plt.figure(figsize=(10, 6))
    # First half of the ellipses
    UE_x, UE_y = eu.ulianov_ellipse_ab(a, b, ang_ini_degrees=-90, ang_fim_degrees=90, ang_ellipse_degrees=ang_ellipse)
    SE_x, SE_y = eu.ellipse_ab(a, b, ang_ini_degrees=0, ang_fim_degrees=180, ang_ellipse_degrees=ang_ellipse)
    plt.plot(np.array(SE_x), SE_y, color="red", label='Standard')
    plt.plot(np.array(UE_x), UE_y, color="blue", label='Ulianov')

    # Second half of the ellipses
    R0, Ue = eu.calc_ue(a, b)
    UE_x, UE_y = eu.ulianov_ellipse_ue(R0, Ue, ang_ini_degrees=90, ang_fim_degrees=270, ang_ellipse_degrees=ang_ellipse)
    SE_x, SE_y = eu.ellipse_ue(R0, Ue, ang_ini_degrees=180, ang_fim_degrees=360, ang_ellipse_degrees=ang_ellipse)
    plt.plot(np.array(SE_x), SE_y, color="green", label='Standard')
    plt.plot(np.array(UE_x), UE_y, color="black", label='Ulianov')

    plt.legend()
    plt.ylabel("y")
    plt.xlabel("x")
    plt.axis('equal')
    plt.title(f"Ellipses a={a}, b={b}, angle rotate={ang_ellipse}°")
    plt.show()

# Example usage: Plotting rotated ellipses
Plot_Two_Ellipses_rotate_rad_ue(10, 1.8, ang_ellipse=np.pi/4)
Plot_Two_Ellipses_rotate_degrees_ab(50, 10, ang_ellipse=30)
Plot_Two_Ellipses_incomplete(50, 30, ang_ellipse=45)
