import numpy as np
import pytest
import allure
from allure_commons.types import Severity

from pycontest.transport import transport

# @allure.title("Test transport (as {loc, vel, dt})")
@allure.title("Test transport function with expected initial values")
@allure.description("""
    Testing the transport function with expected values of:
    initial location, velocity, and a time unit (delta time)
""")
@allure.tag("Transport", "Modeling")
def test_transport_1():
    # allure.dynamic.tag("Transport") # run-time example instead of a decorator
    loc = 3.0
    vel = 1.0
    dt = 0.5

    # assert transport(loc, vel, dt) == 3.5

    # solution
    lof_final = 3 + 0.5 * 1
    assert transport(loc=loc, vel=vel, dt=dt) == lof_final


@allure.title("Test transport with arrays in two dimensions")
@allure.description("""We want to check if it works for arrays with 2d""")
def test_transport_2():
    allure.dynamic.tag("Transport", "Modeling")
    
    loc = np.array([[1, 2], [11, 12]])
    vel = np.array([[1, 1], [-1, -1]])
    dt = 1

    assert (transport(loc, vel, dt) == np.array([[2, 3], [10, 11]])).all()


# let's try one more, with dt that is float
@allure.title("Test transport with integers")
@allure.description("""
    A test that uses:
    integers for location and velocity
    float for time
    
    Example on how to use a decorator with a currently failing test
""")
@allure.severity(Severity.CRITICAL)
# Example on how to use a decorator with a currently failing test
# @pytest.mark.xfail(reason="doesn't work for arrays with dtype=int")
def test_transport_3():
    allure.dynamic.tag("Transport", "Modeling")
    
    loc = np.array([[1, 2], [11, 12]])
    vel = np.array([[1, 1], [-1, -1]])
    dt = 0.5
    
    assert (transport(loc, vel, dt) == np.array([[1.5, 2.5], [10.5, 11.5]])).all()


# fix not shown in workshop: TODO
@allure.title("Test transport with lists")
@allure.description("""Lists as inputs for location and velocity""")
def test_transport_4():
    allure.dynamic.tag("Transport", "Modeling")

    loc = [[1, 2], [11, 12]]
    vel = [[1, 1], [-1, -1]]
    dt = 0.5
    
    assert (transport(loc, vel, dt) == np.array([[1.5, 2.5], [10.5, 11.5]])).all()


# NOTES
# pytest decorators - mark
# marking tests for a known fail / fix later
# @pytest.mark.xfail(reason="doesn't work for arrays with dtype=int")

# https://docs.pytest.org/en/stable/reference/reference.html#marks

# read about skip/xfail
# https://docs.pytest.org/en/stable/how-to/skipping.html

# allure-pytest
# https://allurereport.org/docs/pytest-reference/