# UlianovEllipse

## Overview

The **UlianovEllipse** library provides a comprehensive set of functions and classes for working with Ulianov elliptical functions. These functions are utilized in the Ulianov Orbital Model (UOM) to analyze and model elliptical orbits. The library also includes general utilities for handling and transforming elliptical shapes in various applications.

## Key Features

- **Ulianov Elliptical Cosine and Sine Functions:** These functions (`cosuell`, `sinuell`) are used to calculate the cosine and sine of an angle for Ulianov ellipses, which differ from standard trigonometric functions.
- **Parameter Conversion:** Methods like `calc_Ue` and `calc_ab` convert between different sets of parameters (e.g., semi-major and semi-minor axes, Ulianov parameters).
- **Axis Rotation:** The `rotate_axis` function allows for the rotation of coordinates, useful in transforming elliptical data.
- **Elliptical Path Calculations:** Functions such as `ulianov_ellipse_ue` and `ulianov_ellipse_ab` provide tools for calculating points along an ellipse using various parameterizations.

## Getting Started

To use the `UlianovEllipse` library, first ensure you have `numpy` installed, as it is a required dependency. You can install it using pip:


```bash
pip install numpy
IN THE FUTURE WILL BE AVALIBLE: pip install ullianovellipse