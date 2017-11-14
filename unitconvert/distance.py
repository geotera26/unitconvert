"""
This Python module will convert miles to kilometers and kilometers
to miles
"""

m2k = 1.60934

def miles_to_kilometers(dist):
    """ Given a distance in miles, this outputs the corresponding
        distance in kilometers.

    PARAMETERS
    ----------

    distance: float
        A distance in miles

    RETURNS
    -------

    distance: float
        The corresponding distance in kilometers

    """

    # Convert miles to kilometers and return value

    return dist*m2k

def kilometers_to_miles(dist):
    """ Given a distance in kilometers, this outputs the corresponding
        distance in miles.

    PARAMETERS
    ----------

    distance: float
        A distance in kilometers

    RETURNS
    -------

    distance in mi: float
        The corresponding distance in miles

    """

    # Convert kilometers to miles return value

    return dist/m2k
