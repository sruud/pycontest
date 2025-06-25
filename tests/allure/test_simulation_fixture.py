import allure
import numpy as np
import pytest

from pycontest import simulation as sim
from pycontest.utils import E_kin, momentum


@pytest.fixture(scope="module")
def data(request):

    print("\n create data")
    # initial condition and simulation parameters
    domain = ([-2, 12], [0, 3])
    dt = 0.5
    t_max = 6
    loc_0 = np.array([[0, 1.5],[10, 1.5]])
    vel_0 = np.array([[1, 0], [-1, 0]])
    radius = 1
    mass = [1, 1]

    loc, vel = sim.simulation(t_max, dt, mass, radius, loc_0, vel_0, domain)

    my_data = {}
    my_data["loc_0"] = loc_0
    my_data["vel_0"] = vel_0
    my_data["loc"] = loc
    my_data["vel"] = vel
    my_data["mass"] = mass

    def data_cleanup():
        print("\n removing data")
        my_data.clear()

    request.addfinalizer(data_cleanup)
    return my_data

@allure.tag("simulation", "fixture")
@allure.title("Energy Test Simulation fixture example")
# TODO: can you grab the docstring from the function I'm testing with allure?
# I noticed std out is being grabbed by allure
@allure.description("""
    Fixture with initial condition and simulation parameters
    Verify resulting energy value
""")
def test_energy(data):

    print("\n test energy")

    E_ini = E_kin(data["vel_0"], data["mass"])
    E_end = E_kin(data["vel"], data["mass"])

    assert E_ini == E_end

@allure.tag("simulation", "fixture")
@allure.title("Momentum Test Simulation fixture example")
@allure.description("""
    Fixture with initial condition and simulation parameters
    Verify resulting momentum value
""")
def test_momentum(data):

    print("\n test momentum")

    p_ini = momentum(data["vel_0"], data["mass"])
    p_end = momentum(data["vel"], data["mass"])

    assert np.all(p_ini == p_end)
