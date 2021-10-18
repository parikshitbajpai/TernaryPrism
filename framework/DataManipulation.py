"""
Utility functions for data handling and manipulation
"""

import numpy as np

def normalize(coordinates):
    """
    Function to normalize a list of data.

    Given a set of coordinates as (a,b,c), the function returns normalised coordinates equal to (a/(a+b+c), b/(a+b+c), c/(a+b+c)).

    Parameters
    ----------
    coordinates: list or tuple or numpy array
                 The coordinates to be normalised

    Returns
    -------
    Normalised list or tuple or numpy array

    Raises
    ------
    ValueError if the coordinates sum to zero
    """

    s = float(sum(coordinates))
    if s == 0:
        raise ValueError("Sum of elements of ternay coordinates equal to 0. Cannot normalise.")
    return [val / s for val in coordinates]
