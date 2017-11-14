import pytest

from unitconvert import distance, temperature

def test_distance():
    # 0 km should also be 0 miles
    assert distance.miles_to_kilometers(0) == 0
    assert distance.kilometers_to_miles(0) == 0

    # check approximate conversions
    assert(round(distance.miles_to_kilometers(25),2)) == 40.23
    assert(round(distance.kilometers_to_miles(25),2)) == 15.53

    # good to check that you get an error for too many inputs
    with pytest.raises(TypeError):
        distance.miles_to_kilometers(1,2)
        distance.kilometers_to_miles(1,2)


def test_temperature():
    # Let's test a couple of known values
    assert temperature.fahrenheit_to_celsius(-40) == -40
    assert temperature.celsius_to_fahrenheit(-40) == -40

    assert temperature.fahrenheit_to_celsius(50) == 10
    assert temperature.celsius_to_fahrenheit(10) == 50

    # And also check that we can't have more than 1 input
    with pytest.raises(TypeError):
        temperature.fahrenheit_to_celsius(1,2)
        temperature.celsius_to_fahrenheit(1,2)
