"""
This Python module will convert a temperature in Fahrenheit to the corresponding
temperature in Celsius or vice versa
"""

def fahrenheit_to_celsius(temp):
    """ Given a temperature in Fahrenheit, this outputs the corresponding
        temperture in degrees Celsius.

    PARAMETERS
    ----------

    temperature: float
        A temperature in Fahrenheit

    RETURNS
    -------

    temperature: float
        The corresponding temperature in Celsius

    """

    # Convert Fahrenheit to Celsius and return value

    return((temp-32)*5/9)

def celsius_to_fahrenheit(temp):
    """ Given a temperature in Celsius, this outputs the corresponding
        temperature in Fahrenheit.

    PARAMETERS
    ----------

    temperature: float
        A temperature in Celsius

    temperature: float
        The corresponding temperature in Fahrenheit

    """

    # Convert Celsius to Fahrenheit and return value

    return((temp)*9/5 + 32)
