import os

import allure
import numpy as np
import pytest

from pycontest import simulation as sim
from pycontest.movies import Movie_2d


@allure.tag("simulation", "mp4")
@allure.title("Test Simulation function with expected initial values")
# TODO: can you grab the docstring from the function I'm testing with allure?
@allure.description("""
    initial condition and simulation parameters
                    
    This test creates a movie.mp4
    alculating positions and velocities of particles after one step

    Arguments:
        dt: time steps
        mass: masses
        radius: radius for all balls
        loc: locations of balls
        vel: 2d velocities of balls
        domain: domain for the box
    Returns:
         positions and velocities of particles after one step
""")
def test_simulation_1():
    # initial condition and simulation parameters
    domain = ([-2, 12], [0, 3])
    t_max = 6
    dt = 0.5
    loc_0 = np.array([[0, 1.5],[10, 1.5]])
    vel_0 = np.array([[1, 0], [-1, 0]])
    radius = 1
    mass = [1, 1]

    # running the simulation
    loc, vel = sim.simulation(t_max, dt, mass, radius, loc_0, vel_0, domain)

    # creating a movie
    movie_name = f"pytest_movie_1d_dt_{dt}"
    movie_filename = f"{movie_name}.mp4"
    movie_path = os.path.join(os.path.dirname(__file__), "..", "..", movie_filename)

    movie = Movie_2d(sim.simulation_step, dt, t_max - dt, loc, vel, domain, mass, radius)
    # movie.animate("pytest_movie_1d_dt_{}".format(dt))
    movie.animate(movie_name)

    # Attach to the test report
    with open(movie_path, "rb") as f:
        allure.attach(f.read(), name="Simulation Video", attachment_type="video/mp4")

    # test location and velocities after collision
    assert loc[0][0] < 5
    assert loc[1][0] > 5
    # Y component should stay the same
    assert (loc[0][1], loc[1][1]) == (loc_0[0][1], loc_0[1][1])

    # particles will exchange vel_x
    assert vel[0][0] == -1
    assert vel[1][0] == 1
    # Y component should stay the same
    assert (vel[0][1], vel[1][1]) == (vel_0[0][1], vel_0[1][1])
