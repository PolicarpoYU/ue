import numpy as np
from ulianovellipse import eu

"""
ulianovorbit.py

This library contains a set of functions and classes for calculating orbital parameters using the Ulianov Orbital Model (UOM).
It includes routines for both 2D and 3D orbital calculations, providing methods to derive parameters from velocity and 
position data. The main classes are `uom_params` and `orbit_vect`, which store model parameters and orbital vectors, respectively.

Available functions and methods:
- calc_time
- calc_angle
- calc_orb_angle
- calc_orb_time
- kepler_to_ulianov
- kepler_to_ulianov_6p
- ulianov_to_kepler
- get_UOM_params_2D_vel (to be implemented)
- get_UOM_params_2D_pos (to be implemented)
- get_UOM_params_3D_vel (to be implemented)
- get_UOM_params_3D_pos (to be implemented)
"""

class uom_params:
    """
    Class to define the parameters of the Ulianov Orbital Model.
    Parameters include initial distance (R0), velocity (V0), Ulianov ellipse parameter (Ue),
    inclination (ang_i), longitude of ascending node (ang_omega), argument of periapsis (ang_ell),
    and initial time (time_alpha0).
    """
    def __init__(self, R0=1, V0=1, Ue=1, ang_i=0, ang_omega=0, ang_ell=0, time_alpha0=0):
        self.R0 = R0
        self.Ue = Ue
        self.V0 = V0
        self.ang_i = ang_i
        self.ang_omega = ang_omega
        self.ang_ell = ang_ell
        self.time_alpha0 = time_alpha0

class orbit_vect:
    """
    Class to store orbital vectors such as position, velocity, and time points.
    Attributes include position vectors (e_x, e_y, e_z), velocity vectors (v_x, v_y, v_z),
    and corresponding time and angle (alpha).
    """
    def __init__(self):
        self.e_x = []
        self.e_y = []
        self.e_z = []
        self.v_x = []
        self.v_y = []
        self.v_z = []
        self.alpha = []
        self.time = []
        self.num_point = []

class UlianovOrbit:
    """
    Main class to handle the calculations of the Ulianov Orbital Model.
    """
    def __init__(self):
        self.version = "V1.0 - 22/07/2024"

    def calc_time(self, param, alpha_dg, delta_angle_dg=0.01, case_3d=False):
        """
        Calculate time, position, and velocity at a given angle alpha_dg.

        Parameters:
        param (uom_params): The orbital parameters.
        alpha_dg (float): The angle in degrees.
        delta_angle_dg (float): Incremental angle step in degrees.
        case_3d (bool): Flag to consider 3D calculations.

        Returns:
        tuple: (time, ex, ey, ez, vx, vy, vz) at the given angle.
        """
        # Initialization and setup
        time = param.time_alpha0
        alpha = 0
        ex = param.R0
        ey = 0
        ez = 0
        vx = 0
        vy = param.V0
        vz = 0

        # Handling special case where alpha_dg is zero
        if alpha_dg == 0:
            ex, ey = eu.rotate_axis(ex, ey, param.ang_ell)
            vx, vy = eu.rotate_axis(vx, vy, param.ang_ell)
            return time, ex, ey, ez, vx, vy, vz

        # Determining direction based on alpha_dg sign
        if alpha_dg > 0:
            direction = 1
        else:
            direction = -1
            alpha_dg = -alpha_dg

        delta_angle = delta_angle_dg * np.pi / 180
        alpha_max = alpha_dg * np.pi / 180

        # Iterative calculation of position and velocity
        while abs(alpha) < abs(alpha_max):
            ex = param.R0 * eu.cosuell(alpha, param.Ue)
            ey = param.R0 * eu.sinuell(alpha, param.Ue)
            de = np.sqrt(ex**2 + ey**2)
            exn = param.R0 * eu.cosuell(alpha + direction * delta_angle, param.Ue)
            eyn = param.R0 * eu.sinuell(alpha + direction * delta_angle, param.Ue)
            dx = exn - ex
            dy = eyn - ey
            dde = np.sqrt(dx**2 + dy**2)
            vteo = param.V0 * np.sqrt(1 + (2 / param.Ue) * (param.R0 / de - 1))
            dt = dde / vteo
            vx = dx / dt
            vy = dy / dt
            time += direction * dt
            alpha += direction * delta_angle

        ex, ey = eu.rotate_axis(ex, ey, param.ang_ell)
        vx, vy = eu.rotate_axis(vx, vy, param.ang_ell)

        return time, ex, ey, ez, vx, vy, vz

    def calc_angle(self, param, target_time, delta_angle_dg=0.01, case_3d=False):
        """
        Calculate the orbital angle for a given time.

        Parameters:
        param (uom_params): The orbital parameters.
        target_time (float): The target time.
        delta_angle_dg (float): Incremental angle step in degrees.
        case_3d (bool): Flag to consider 3D calculations.

        Returns:
        tuple: (alpha, ex, ey, ez, vx, vy, vz) at the given time.
        """
        # Initialization and setup
        time = param.time_alpha0
        alpha = 0
        ex = param.R0
        ey = 0
        ez = 0
        vx = 0
        vy = param.V0
        vz = 0

        # Handling special case where target_time equals initial time
        if target_time == param.time_alpha0:
            ex, ey = eu.rotate_axis(ex, ey, param.ang_ell)
            vx, vy = eu.rotate_axis(vx, vy, param.ang_ell)
            return alpha, ex, ey, ez, vx, vy, vz

        # Determining direction based on target_time sign
        if target_time > param.time_alpha0:
            direction = 1
        else:
            direction = -1
            target_time = -target_time

        delta_angle = delta_angle_dg * np.pi / 180
        alpha_previous = alpha
        time_previous = time

        # Iterative calculation of position and velocity until target time is reached
        while abs(time) < abs(target_time):
            ex = param.R0 * eu.cosuell(alpha, param.Ue)
            ey = param.R0 * eu.sinuell(alpha, param.Ue)
            de = np.sqrt(ex**2 + ey**2)
            exn = param.R0 * eu.cosuell(alpha + direction * delta_angle, param.Ue)
            eyn = param.R0 * eu.sinuell(alpha + direction * delta_angle, param.Ue)
            dx = exn - ex
            dy = eyn - ey
            dde = np.sqrt(dx**2 + dy**2)
            vteo = param.V0 * np.sqrt(1 + (2 / param.Ue) * (param.R0 / de - 1))
            dt = dde / vteo
            vx = dx / dt
            vy = dy / dt
            time_previous = time
            alpha_previous = alpha
            time += direction * dt
            alpha += direction * delta_angle

        # Linear interpolation to find the exact angle for the target time
        if time != target_time:
            time_fraction = (target_time - time_previous) / (time - time_previous)
            alpha = alpha_previous + time_fraction * (alpha - alpha_previous)
            ex = param.R0 * eu.cosuell(alpha, param.Ue)
            ey = param.R0 * eu.sinuell(alpha, param.Ue)
            de = np.sqrt(ex**2 + ey**2)
            vx = dx / dt
            vy = dy / dt
        ex, ey = eu.rotate_axis(ex, ey, param.ang_ell)
        vx, vy = eu.rotate_axis(vx, vy, param.ang_ell)
        return alpha, ex, ey, ez, vx, vy, vz
    
    def calc_orb_angle(self, param, alpha0_dg, alpha_max_dg, delta_alpha_dg, time_max=None, msg=False, case_3d=False):
        """
        Calculate the orbital path using a series of angles.

        Parameters:
        param (uom_params): The orbital parameters.
        alpha0_dg (float): Initial angle in degrees.
        alpha_max_dg (float): Maximum angle in degrees.
        delta_alpha_dg (float): Incremental angle step in degrees.
        time_max (float, optional): Maximum simulation time.
        msg (bool, optional): Flag to display progress messages.
        case_3d (bool, optional): Flag to consider 3D calculations.

        Returns:
        orbit_vect: Object containing the calculated positions, velocities, and times.
        """
        # Initialize orbit vectors and setup parameters
        orbit_values = orbit_vect()
        if time_max is None:
            time_max = 1E1000
        delta_alpha = delta_alpha_dg * np.pi / 180
        alpha = alpha0_dg * np.pi / 180
        alpha_max = alpha_max_dg * np.pi / 180
        time0, ex, ey, ez, vx, vy, vz = self.calc_time(param, alpha0_dg, case_3d=case_3d)
        orbit_values.time.append(time0)
        orbit_values.num_point.append(0)
        orbit_values.alpha.append(alpha)
        orbit_values.e_x.append(ex)
        orbit_values.e_y.append(ey)
        orbit_values.v_x.append(vx)
        orbit_values.v_x.append(vy)
        orbit_values.v_z.append(vz)
        orbit_values.e_z.append(ez)
        mostra = 0
        num_point = 0
        t = time0

        # Iterative calculation of the orbital path
        while (alpha < alpha_max) and (t < time_max):
            num_point += 1
            mostra += 1
            ex = param.R0 * eu.cosuell(alpha, param.Ue)
            ey = param.R0 * eu.sinuell(alpha, param.Ue)
            de = np.sqrt(ex**2 + ey**2)
            exn = param.R0 * eu.cosuell(alpha + delta_alpha, param.Ue)
            eyn = param.R0 * eu.sinuell(alpha + delta_alpha, param.Ue)
            dx = exn - ex
            dy = eyn - ey
            dde = np.sqrt(dx**2 + dy**2)
            vteo = param.V0 * np.sqrt(1 + (2 / param.Ue) * (param.R0 / de - 1))
            dt = dde / vteo
            vx = dx/dt
            vy = dy/dt
            t += dt
            alpha += delta_alpha
            if (mostra > 100) and msg:
                mostra = 0
                print(f"\r Angle = {alpha*180/np.pi:.4f} , time = {t/60/60/24:.2f} days, x={ex:.2f}, y={ey:.2f}, v={vteo:.2f} ", end="")
            ex, ey = eu.rotate_axis(ex, ey, param.ang_ell)
            vx, vy = eu.rotate_axis(vx, vy, param.ang_ell)
            orbit_values.time.append(t)
            orbit_values.num_point.append(num_point)
            orbit_values.alpha.append(alpha)
            orbit_values.e_x.append(ex)
            orbit_values.e_y.append(ey)
            orbit_values.v_x.append(vx)
            orbit_values.v_y.append(vy)
            orbit_values.v_z.append(vz)
            orbit_values.e_z.append(ez)
        return orbit_values

    def calc_orb_time(self, param, time0, delta_time, time_max, alpha_max_dg=None, msg=False, case_3d=False):
        """
        Calculate the orbital path using a series of time steps.

        Parameters:
        param (uom_params): The orbital parameters.
        time0 (float): Initial time.
        delta_time (float): Time step.
        time_max (float): Maximum simulation time.
        alpha_max_dg (float, optional): Maximum angle in degrees.
        msg (bool, optional): Flag to display progress messages.
        case_3d (bool, optional): Flag to consider 3D calculations.

        Returns:
        orbit_vect: Object containing the calculated positions, velocities, and times.
        """
        # Initialize orbit vectors and setup parameters
        orbit_values = orbit_vect()
        if alpha_max_dg is None:
            time_max = 1E100
        alpha_max = alpha_max_dg * np.pi / 180
        t = time0
        alpha, ex, ey, ez, vx, vy, vz = self.calc_angle(param, time0, case_3d=case_3d)
        orbit_values.time.append(t)
        orbit_values.num_point.append(0)
        orbit_values.alpha.append(alpha)
        orbit_values.e_x.append(ex)
        orbit_values.e_y.append(ey)
        orbit_values.v_x.append(vx)
        orbit_values.v_y.append(vy)
        orbit_values.v_z.append(vz)
        orbit_values.e_z.append(ez)
        mostra = 0
        num_point = 0

        # Begin with a small delta_alpha
        delta_alpha1 =  np.pi / 100000 
        while (alpha < alpha_max) and (t < time_max):
            num_point += 1
            mostra += 1
            ex = param.R0 * eu.cosuell(alpha, param.Ue)
            ey = param.R0 * eu.sinuell(alpha, param.Ue)
            de = np.sqrt(ex**2 + ey**2)
            exn = param.R0 * eu.cosuell(alpha + delta_alpha1, param.Ue)
            eyn = param.R0 * eu.sinuell(alpha + delta_alpha1, param.Ue)
            dx = exn - ex
            dy = eyn - ey
            dde = np.sqrt(dx**2 + dy**2)
            vteo = param.V0 * np.sqrt(1 + (2 / param.Ue) * (param.R0 / de - 1))
            dtc = dde / vteo
            delta_alpha = delta_alpha1 / dtc * delta_time 
            vx = dx / delta_time
            vy = dy / delta_time
            t += delta_time
            alpha += delta_alpha
            if (mostra > 100) and msg:
                mostra = 0
                print(f"\r Angle = {alpha*180/np.pi:.4f} , time = {t/60/60/24:.2f} days, x={ex:.2f}, y={ey:.2f}, v={vteo:.2f} ", end="")
            ex, ey = eu.rotate_axis(ex, ey, param.ang_ell)
            vx, vy = eu.rotate_axis(vx, vy, param.ang_ell)
            orbit_values.time.append(t)
            orbit_values.num_point.append(num_point)
            orbit_values.alpha.append(alpha)
            orbit_values.e_x.append(ex)
            orbit_values.e_y.append(ey)
            orbit_values.v_x.append(vx)
            orbit_values.v_y.append(vy)
            orbit_values.v_z.append(vz)
            orbit_values.e_z.append(ez)
        return orbit_values
    
    def kepler_to_ulianov(self, a, e, M):
        """
        Convert Keplerian orbital elements to Ulianov parameters.

        Parameters:
        a (float): Semi-major axis.
        e (float): Eccentricity.
        M (float): Mass of the primary body.

        Returns:
        tuple: (R0, Ue, V0) Ulianov parameters.
        """
        # Calculate b using the eccentricity formula
        G = 6.67384e-11
        b = a * np.sqrt(1 - e**2)
        R0, Ue = eu.calc_Ue(a, b)
        V0 = np.sqrt(Ue * G * M / R0)
        return R0, Ue, V0

    def kepler_to_ulianov_6p(self, a, e, ang_i_dg, ang_omega_dg, ang_ell_dg, alpha_dg, t0, v, M):
        """
        Convert full set of Keplerian orbital elements to Ulianov parameters.

        Parameters:
        a (float): Semi-major axis.
        e (float): Eccentricity.
        ang_i_dg (float): Inclination in degrees.
        ang_omega_dg (float): Longitude of ascending node in degrees.
        ang_ell_dg (float): Argument of periapsis in degrees.
        alpha_dg (float): True anomaly in degrees.
        t0 (float): Time at periapsis passage.
        v (float): Velocity.
        M (float): Mass of the primary body.

        Returns:
        uom_params: Object containing the calculated Ulianov parameters.
        """
        # Calculate b using the eccentricity formula
        G = 6.67384e-11
        b = a * np.sqrt(1 - e**2)
        R0, Ue = eu.calc_Ue(a, b)
        V0 = np.sqrt(Ue * G * M / R0)
        ang_i = ang_i_dg * np.pi / 180
        ang_omega = ang_omega_dg * np.pi / 180
        ang_ell = ang_ell_dg * np.pi / 180

        param = uom_params(R0=R0, V0=V0, Ue=Ue, ang_i=ang_i, ang_omega=ang_omega, ang_ell=ang_ell, time_alpha0=0)
        time0, ex, ey, ez, vx, vy, vz = self.calc_time(param, alpha_dg)
        param.time_alpha0 = t0 - time0
        return param

    def ulianov_to_kepler(self, R0, Ue):
        """
        Convert Ulianov parameters to Keplerian orbital elements.

        Parameters:
        R0 (float): Minimum orbital distance.
        Ue (float): Ulianov Ellipse Parameter.

        Returns:
        tuple: (a, e) Semi-major axis and eccentricity.
        """
        a, b = eu.calc_ab(R0, Ue)
        e = np.sqrt(1 - (b**2 / a**2))
        return a, e
        
    def get_UOM_params_2D_vel(x0, y0, t0, vx0, vy0, M):
        """
        Calculates UOM parameters from a position and velocity vector in 2D.
    
        Parameters:
        x0 (float): Initial x-coordinate of the position.
        y0 (float): Initial y-coordinate of the position.
        t0 (float): Time associated with the initial position.
        vx0 (float): Velocity component in the x direction.
        vy0 (float): Velocity component in the y direction.
        M (float): Mass of the body being orbited.
    
        Returns:
        uom_params: Object containing the calculated UOM parameters.
        """
        # Placeholder for actual implementation
        return uom_params()
    
    
    def get_UOM_params_2D_pos(x0, y0, t0, x1, y1, t1, M):
        """
        Calculates UOM parameters from two position vectors in 2D.
    
        Parameters:
        x0 (float): Initial x-coordinate of the position.
        y0 (float): Initial y-coordinate of the position.
        t0 (float): Time associated with the initial position.
        x1 (float): Final x-coordinate of the position.
        y1 (float): Final y-coordinate of the position.
        t1 (float): Time associated with the final position.
        M (float): Mass of the body being orbited.
    
        Returns:
        uom_params: Object containing the calculated UOM parameters.
        """
        # Placeholder for actual implementation
        return uom_params()
    
    
    def get_UOM_params_3D_vel(x0, y0, z0, t0, vx0, vy0, vz0, M):
        """
        Calculates UOM parameters from a position and velocity vector in 3D.
    
        Parameters:
        x0 (float): Initial x-coordinate of the position.
        y0 (float): Initial y-coordinate of the position.
        z0 (float): Initial z-coordinate of the position.
        t0 (float): Time associated with the initial position.
        vx0 (float): Velocity component in the x direction.
        vy0 (float): Velocity component in the y direction.
        vz0 (float): Velocity component in the z direction.
        M (float): Mass of the body being orbited.
    
        Returns:
        uom_params: Object containing the calculated UOM parameters.
        """
        # Placeholder for actual implementation
        return uom_params()
    
    
    def get_UOM_params_3D_pos(x0, y0, z0, t0, x1, y1, z1, t1, M):
        """
        Calculates UOM parameters from two position vectors in 3D.
    
        Parameters:
        x0 (float): Initial x-coordinate of the position.
        y0 (float): Initial y-coordinate of the position.
        z0 (float): Initial z-coordinate of the position.
        t0 (float): Time associated with the initial position.
        x1 (float): Final x-coordinate of the position.
        y1 (float): Final y-coordinate of the position.
        z1 (float): Final z-coordinate of the position.
        t1 (float): Time associated with the final position.
        M (float): Mass of the body being orbited.
    
        Returns:
        uom_params: Object containing the calculated UOM parameters.
        """
        # Placeholder for actual implementation
        return uom_params()

ou= uom_params()