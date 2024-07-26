import numpy as np

"""
ulianovellips.py

This library provides a set of functions and classes for handling Ulianov elliptical functions, which are used to model
and analyze elliptical orbits in the Ulianov Orbital Model (UOM) as well as in other applications involving ellipses in 
general. The functions include calculations for various properties and transformations related to ellipses, such as 
Ulianov Elliptical Cosine and Sine. Additionally, the library offers conversions between different parameter sets, 
enabling a broad range of analyses and computations. This makes it a versatile tool for both theoretical and practical 
studies of elliptical phenomena.

Available functions and methods:
- last_functon_steps
- lim_ue
- calc_Ue
- calc_ab
- cosuell
- sinuell
- calc_R0
- arctanuell_1p
- calcula_angulo_rad
- arctanuell
- arctanuell_ue
- rotate_axis
- ulianov_ellipse_ue
- ulianov_ellipse_ab
- ellipse_ab
- ellipse_ue
"""




class UlianovEllipse:
    def __init__(self):
        self.version = "V1.0 - 01/07/2024"
        self.Lim_Ue = 1.99999999999999
        self.nuber_steps = 0
       
    def last_functon_steps(self):
        """
        Returns the number of steps taken by the last function executed.
        """
        return self.nuber_steps

    def lim_ue(self, Ue):
        """
        Limits the value of Ue to be within the defined range.

        Parameters:
        Ue (float): The original Ue value.

        Returns:
        float: The limited Ue value.
        """
        if Ue > self.Lim_Ue:
            Ue = self.Lim_Ue
        if Ue < 1 / self.Lim_Ue:
            Ue = 1 / self.Lim_Ue
        return Ue

    def calc_Ue(self, a, b):
        """
        Calculates R0 and Ue based on the semi-major axis (a) and semi-minor axis (b).

        Parameters:
        a (float): Semi-major axis.
        b (float): Semi-minor axis.

        Returns:
        tuple: (R0, Ue)
        R0 (float): Ellipse parameter R0.
        Ue (float): Ellipse parameter Ue.
        """
        if (a > 0) and (b > 0): 
            if (a > b):
                R0 = a - np.sqrt(a**2 - b**2)
                Ue = b**2 / (a * R0)
            else:
                R0 = b - np.sqrt(b**2 - a**2)
                Ue = - a**2/(b * R0)   
        else:
            R0 = max(a,b)
            Ue = 1
        return R0, Ue
    
    def calc_ab(self, R0, Ue):
        """
        Calculates the semi-major axis (a) and semi-minor axis (b) from R0 and Ue.

        Parameters:
        R0 (float): Ellipse parameter R0.
        Ue (float): Ellipse parameter Ue (ranges from 0.500000000000002 to 1.99999999999999).

        Returns:
        tuple: (a, b)
        a (float): Semi-major axis.
        b (float): Semi-minor axis.
        """
        tolerance = 1e-6  # Definir a tolerância para a verificação
       
        inv=False
        if Ue < 0:
           Ue = abs(Ue)
           inv= True 
       
        if Ue < 2-tolerance:
           kx = 1 / (2 - Ue)
           ky = 0
           if Ue>0:
              ky = 1 / np.sqrt((2 / Ue) - 1)
           a = R0 * kx
           b = R0 * ky
        else:
           a = R0
           b = R0    
        if inv:
           a,b = b,a 
        return a, b
 
    def cosuell(self, alpha, Ue):
        if Ue<0:
            return self.sinuell(alpha,abs(Ue))  
        tolerance = 1e-6  # Definir a tolerância para a verificação
        if abs(Ue - 2) < tolerance:
            # Para Ue = 2, retornamos a equação paramétrica da parábola
            return 1 - (np.sinh(alpha) ** 2) / 4
        elif Ue > 2:
            kx = 1 / (2 - Ue)
            return kx * (np.cosh(alpha) - 1) + 1  # Usar a função hiperbólica cosh para Ue > 2
        else:
            kx = 1 / (2 - Ue)
            return kx * (np.cos(alpha) - 1) + 1

    def sinuell(self, alpha, Ue):
        if Ue<0:
            return self.cosuell(alpha,abs(Ue))  
        tolerance = 1e-6  # Definir a tolerância para a verificação
        if abs(Ue - 2) < tolerance:
            # Para Ue = 2, retornamos um valor linear em relação a alpha
            return np.sinh(alpha)
        elif Ue > 2:
            ky = 1 / np.sqrt(1 - (2 / Ue))
            return ky * np.sinh(alpha)  # Usar a função hiperbólica sinh para Ue > 2
        else:
            if Ue>0:
                ky = 1 / np.sqrt((2 / Ue) - 1)
            else:
                ky = 0    
            return ky * np.sin(alpha)

    def calc_R0(self, x, y, ang, Ue):
        """
        Calculates the R0 parameter for the ellipse based on coordinates and angle.

        Parameters:
        x (float): X-coordinate.
        y (float): Y-coordinate.
        ang (float): Angle in radians.
        Ue (float): Ellipse parameter Ue (ranges from 0.500000000000002 to 1.99999999999999).

        Returns:
        float: Calculated R0 value.
        """
        Ue=self.lim_ue(Ue)  
        cx = self.cosuell(ang, Ue)
        sy = self.sinuell(ang, Ue)
        if cx != 0:
            R0x = abs(x / cx)
        else:
            R0x = abs(y / sy)
        R0y = R0x
        if sy != 0:
            R0y = abs(y / sy)
        R0 = (R0x + R0y) / 2
        return R0

    def arctanuell_1p(self, y, x, Ue):
        """
        Calculates the Ulianov Ellipse arctangent for a given x and y coordinate and Ue.

        Parameters:
        y (float): Y-coordinate.
        x (float): X-coordinate.
        Ue (float): Ellipse parameter Ue (ranges from 0.500000000000002 to 1.99999999999999).

        Returns:
        tuple: (angle, R0)
        angle (float): Calculated angle in radians.
        R0 (float): Calculated R0 value.
        """
        Ue=self.lim_ue(Ue)  
        anguloS = np.arctan2(y, x)
        d = np.sqrt(x**2 + y**2)
        ux = x + d * (Ue - 1)
        uy = y
        angulo = np.arctan2(uy, ux) + 2 * np.pi
        if angulo > (2 * np.pi):
            angulo = angulo - 2 * np.pi
        if abs(anguloS) < np.pi / 1000000:
            angulo = anguloS
        R0 = self.calc_R0(x, y, angulo, Ue)
        return angulo, R0

    def calcula_angulo_rad(self, Ue, ang):
        """
        Calculates the angle for a given Ue and initial angle in radians.

        Parameters:
        Ue (float): Ellipse parameter Ue (ranges from 0.500000000000002 to 1.99999999999999).
        ang (float): Initial angle in radians.

        Returns:
        float: Calculated angle in radians.
        """
        Ue = self.lim_ue(Ue)
        xi = 1000 * self.cosuell(ang, Ue)
        yi = 1000 * self.sinuell(ang, Ue)
        ag_arctanuell, R0n = self.arctanuell_1p(yi, xi, Ue)
        return ag_arctanuell
 
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
        Ue = self.lim_ue(Ue)
        angulo_procurado, R0n = self.arctanuell_1p(y, x, Ue)
        ang_inicial = angulo_procurado
        ang_atual = self.calcula_angulo_rad(Ue, ang_inicial)
        
        if angulo_procurado > ang_atual:
            dir = 1
            ang_limite = angulo_procurado - np.pi /2
        else:
            dir = -1
            ang_limite = angulo_procurado + np.pi / 2
        self.nuber_steps=0
        delta_ang = 10 * np.pi / 180
        npassos = 0
        max_passos = int(200 * np.log10(1 / precision) / np.log10(1 / 1e-12))
        while (delta_ang * 180 / np.pi > precision / 100) and (npassos < max_passos):
            npassos += 1
            self.nuber_steps+=1
            ult_ang_inicial = ang_inicial
            ang_inicial += dir * delta_ang
            ang_atual = self.calcula_angulo_rad(Ue, ang_inicial)
            if (dir == 1):
                if (ang_atual < ang_limite):
                    ang_novo = ang_atual + 2 * np.pi
                    ang_atual = ang_novo
            
                if ang_atual > angulo_procurado:
                    delta_ang /= 2
                    ang_inicial = ult_ang_inicial
            else:
                if (ang_atual > ang_limite):
                    ang_novo = ang_atual - 2 * np.pi
                    ang_atual = ang_novo
            
                if (ang_atual < angulo_procurado):
                    delta_ang /= 2
                    ang_inicial = ult_ang_inicial
        
        ang_final = ang_inicial
        R0n = self.calc_R0(x, y, ang_final, Ue)
        
        if ang_final < 0:
            ang_final += 2 * np.pi
        elif ang_final >= 2 * np.pi:
            ang_final -= 2 * np.pi

        return ang_final, R0n

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
        step=0
        erromax = 1e20
        npassos=20
        Ndig = 20
        # Primeiro estágio: busca inicial grosseira
        precision_factor = 5  # Ajusta a precisão conforme necessário
        Ue= 1 
        UeOK = 1
        dtUe = 0.1
        while Ue <= self.Lim_Ue:
            step+=1
            angulo, R0calc0 = self.arctanuell(y, x, Ue)
            R0calc = self.calc_R0_np(x, y, angulo, Ue)
            erro = abs(R0calc - R0) / R0 * 100
            if erro < erromax:
                erromax = erro 
                UeOK = Ue
                Ue_max = Ue+10*dtUe
                Ue_min = Ue-10*dtUe
            dtUe1 = min(0.1, (self.Lim_Ue - Ue) / precision_factor)
            if dtUe1<0.0000000001:
                dtUe1=0.0000000001
            if dtUe1>0.01:
                dtUe1=0.01
            Ue += dtUe1
        for D in range(Ndig):
            step+=1
            for Ue in np.linspace(Ue_min, Ue_max, npassos):
                if (Ue >=1) and (Ue<self.Lim_Ue):
                    angulo, R0calc0 = self.arctanuell(y, x, Ue)
                    R0calc = self.calc_R0(x, y, angulo, Ue)
                    erro = abs(R0calc - R0) / R0 * 100
                    if erro < erromax:
                        erromax = erro
                        UeOK = Ue
            Ue_min = UeOK - (Ue_max - Ue_min) / (npassos /2)
            Ue_max = UeOK + (Ue_max - Ue_min) / (npassos /2)
        last_functon_step=step
        angulo, R0calc0 = self.arctanuell(y, x, UeOK)
        return angulo, UeOK

    def rotate_axis(self, x, y, alfa):
        """
        Rotates the coordinates x and y by the angle alfa.

        Parameters:
        x (float): X-coordinate.
        y (float): Y-coordinate.
        alfa (float): Angle in radians.

        Returns:
        tuple: (xn, yn)
        xn (float): Rotated X-coordinate.
        yn (float): Rotated Y-coordinate.
        """
        cos_alfa = np.cos(alfa)
        sin_alfa = np.sin(alfa)
        xn = x * cos_alfa - y * sin_alfa
        yn = x * sin_alfa + y * cos_alfa
        return xn, yn
    
    def ulianov_ellipse_ue(self, R0, Ue, delta_ang=0.1, ang_ini_degrees=0, ang_fim_degrees=360, ang_ellipse_rad=0, ang_ellipse_degrees=0):
        """
        Calculates the coordinates of the Ulianov ellipse using R0 and Ue.

        Parameters:
        R0 (float): Ellipse parameter R0.
        Ue (float): Ellipse parameter Ue (ranges from 0.500000000000002 to 1.99999999999999).
        delta_ang (float): Angular step size in degrees (default is 0.1).
        ang_ini_degrees (float): Initial angle in degrees (default is 0).
        ang_fim_degrees (float): Final angle in degrees (default is 360).
        ang_ellipse_rad (float): Ellipse rotation angle in radians (default is 0).
        ang_ellipse_degrees (float): Ellipse rotation angle in degrees (default is 0).

        Returns:
        tuple: (UE_x, UE_y)
        UE_x (ndarray): X-coordinates of the ellipse.
        UE_y (ndarray): Y-coordinates of the ellipse.
        """
        if ang_fim_degrees <= ang_ini_degrees:
            ang_fim_degrees = ang_ini_degrees + 90
        npassos = int(float((ang_fim_degrees - ang_ini_degrees) / delta_ang))
        alpha = np.linspace(ang_ini_degrees * np.pi / 180, ang_fim_degrees * np.pi / 180, npassos)
        UE_x = R0 * self.cosuell(alpha, Ue)
        UE_y = R0 * self.sinuell(alpha, Ue)
        if ang_ellipse_degrees != 0:
            ang_ellipse_rad = ang_ellipse_degrees / 180 * np.pi
        if ang_ellipse_rad != 0:
            UE_x, UE_y = self.rotate_axis(UE_x, UE_y, ang_ellipse_rad)
        return UE_x, UE_y

    def ulianov_ellipse_ab(self, a, b, delta_ang=0.1, ang_ini_degrees=0, ang_fim_degrees=360, ang_ellipse_rad=0, ang_ellipse_degrees=0):
        """
        Calculates the coordinates of the Ulianov ellipse using a and b.

        Parameters:
        a (float): Semi-major axis.
        b (float): Semi-minor axis.
        delta_ang (float): Angular step size in degrees (default is 0.1).
        ang_ini_degrees (float): Initial angle in degrees (default is 0).
        ang_fim_degrees (float): Final angle in degrees (default is 360).
        ang_ellipse_rad (float): Ellipse rotation angle in radians (default is 0).
        ang_ellipse_degrees (float): Ellipse rotation angle in degrees (default is 0).

        Returns:
        tuple: (UE_x, UE_y)
        UE_x (ndarray): X-coordinates of the ellipse.
        UE_y (ndarray): Y-coordinates of the ellipse.
        """
        R0, Ue = self.calc_Ue(a, b)
        return self.ulianov_ellipse_ue(R0, Ue, delta_ang, ang_ini_degrees, ang_fim_degrees, ang_ellipse_rad, ang_ellipse_degrees)

    def ellipse_ab(self, a, b, delta_ang=0.1, ang_ini_degrees=0, ang_fim_degrees=360, ang_ellipse_rad=0, ang_ellipse_degrees=0):
        """
        Calculates the coordinates of a standard ellipse using a and b.

        Parameters:
        a (float): Semi-major axis.
        b (float): Semi-minor axis.
        delta_ang (float): Angular step size in degrees (default is 0.1).
        ang_ini_degrees (float): Initial angle in degrees (default is 0).
        ang_fim_degrees (float): Final angle in degrees (default is 360).
        ang_ellipse_rad (float): Ellipse rotation angle in radians (default is 0).
        ang_ellipse_degrees (float): Ellipse rotation angle in degrees (default is 0).

        Returns:
        tuple: (SE_x, SE_y)
        SE_x (ndarray): X-coordinates of the ellipse.
        SE_y (ndarray): Y-coordinates of the ellipse.
        """
        if ang_fim_degrees <= ang_ini_degrees:
            ang_fim_degrees = ang_ini_degrees + 90
        npassos = int(float((ang_fim_degrees - ang_ini_degrees) / delta_ang))
        alpha = np.linspace(ang_ini_degrees * np.pi / 180, ang_fim_degrees * np.pi / 180, npassos)
        SE_x = a * np.cos(alpha)
        SE_y = b * np.sin(alpha)
        if ang_ellipse_degrees != 0:
            ang_ellipse_rad = ang_ellipse_degrees / 180 * np.pi
        if ang_ellipse_rad != 0:
            SE_x, SE_y = self.rotate_axis(SE_x, SE_y, ang_ellipse_rad)
        return SE_x, SE_y

    def ellipse_ue(self, R0, Ue, delta_ang=0.1, ang_ini_degrees=0, ang_fim_degrees=360, ang_ellipse_rad=0, ang_ellipse_degrees=0):
        """
        Calculates the coordinates of a standard ellipse using R0 and Ue.

        Parameters:
        R0 (float): Ellipse parameter R0.
        Ue (float): Ellipse parameter Ue (ranges from 0.500000000000002 to 1.99999999999999).
        delta_ang (float): Angular step size in degrees (default is 0.1).
        ang_ini_degrees (float): Initial angle in degrees (default is 0).
        ang_fim_degrees (float): Final angle in degrees (default is 360).
        ang_ellipse_rad (float): Ellipse rotation angle in radians (default is 0).
        ang_ellipse_degrees (float): Ellipse rotation angle in degrees (default is 0).

        Returns:
        tuple: (SE_x, SE_y)
        SE_x (ndarray): X-coordinates of the ellipse.
        SE_y (ndarray): Y-coordinates of the ellipse.
        """
        a, b = self.calc_ab(R0, Ue)
        return self.ellipse_ab(a, b, delta_ang, ang_ini_degrees, ang_fim_degrees, ang_ellipse_rad, ang_ellipse_degrees)

eu = UlianovEllipse()
