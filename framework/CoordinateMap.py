"""
Mapping between Ternary and Cartesian Coordinates.

Functions for converting ternary coordinates into cartesian system used in Matplotlib and vice-versa. All the values will be scaled so that the side length of the triangle is equal to one.
"""

import numpy as np

# Define constants to avoid code repetitions
_sqrt3 = np.sqrt(3.)
_half_sqrt3 = _sqrt3 / 2.

# Ternary to Cartesian Mapping
def ternaryToCartesian(coordinates):
    """
    Maps ternary coordinates to cartesian coordinates.

    Consider an equilateral ternary plot where a = 1 is placed at (0,0) and b = 1 is placed at (1,0). Then c = 1 will be at (1/2, sqrt(3)/2).
    The 3-tuple (a,b,c) will have the cartesian coordinates (b+c/2, sqrt(3)c/2, z), where a+b+c = 1.

    Parameters
    ----------
    coordinates: list / tuple / numpy array of size three
                 The coordinates to be converted from ternary to cartesian

    Returns
    -------
    numpy array of size two
    """
    return(np.array([(coordinates[1] + coordinates[2] / 2.), (_half_sqrt3 * coordinates[2])]))

# Cartesian to Ternary Mapping
def cartesianToTernary(coordinates, sigma = 1.):
    """
    Maps cartesian coordinates to ternary coordinates.

    Mapping from cartesian to ternary coordinates requires an additional equation. If the sum of the ternary coordinates is known (say n), one can use the equations
    for ternary to cartesian mapping and a+b+c = n to get (x-y/sqrt(3), 2y/sqrt(3), n-a-b)

    Parameters
    ----------
    coordinates: list / tuple / numpy array of size two
                The coordinates to be converted from cartesian to ternary

    sigma: Real
            Sum of (a, b, c) that the ternary coordinates should sum to.

    Returns
    -------
    numpy array of size three
    """
    c = coordinates[1] / _half_sqrt3
    b = coordinates[0] - c / 2.
    a = sigma - (b + c)
    return(np.array([a,b,c]))
