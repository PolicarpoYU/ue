# UlianovOrbit
## Overview

The **UlianovOrbit** repository contains two Python libraries designed for modeling and analyzing elliptical orbits using the Ulianov Orbital Model (UOM). This model provides a unique approach to studying orbits, using Ulianov elliptical functions to calculate various parameters and transformations related to elliptical paths in space.

## Libraries

### 1. ulianovellips.py

This library provides functions and classes for handling Ulianov elliptical functions, which are essential for modeling and analyzing elliptical orbits in the UOM. It includes calculations for Ulianov Elliptical Cosine and Sine, conversions between different parameter sets, and various other tools for working with ellipses in a general context.

#### Key Functions:
- `cosuell`
- `sinuell`
- `calc_Ue`
- `calc_ab`
- `rotate_axis`
- `ulianov_ellipse_ue`
- `ulianov_ellipse_ab`
- `ellipse_ab`
- `ellipse_ue`

### 2. ulianovorbit.py

This library focuses on the calculations of orbital parameters using the Ulianov Orbital Model. It includes routines for both 2D and 3D orbital calculations, providing methods to derive parameters from velocity and position data. The main classes, `uom_params` and `orbit_vect`, store model parameters and orbital vectors, respectively.

#### Key Functions:
- `calc_time`
- `calc_angle`
- `calc_orb_angle`
- `calc_orb_time`
- `kepler_to_ulianov`
- `kepler_to_ulianov_6p`
- `ulianov_to_kepler`
- `get_UOM_params_2D_vel` (to be implemented)
- `get_UOM_params_2D_pos` (to be implemented)
- `get_UOM_params_3D_vel` (to be implemented)
- `get_UOM_params_3D_pos` (to be implemented)

## Getting Started

To use these libraries, simply clone this repository and import the desired modules into your Python scripts. Ensure that you have `numpy` installed, as it is a dependency for these libraries.

```bash
IN THE FUTURE WILL BE AVALIBLE: pip install numpy
