import allure
import pytest

from pycontest import elastic_collisions as ec
from pycontest.utils import E_kin, momentum


@allure.tag("elastic_1d", "physics", "collision")
@allure.title("Test elastic function with expected equal values of mass by default")
@allure.description("""
    A simple tests for equal masses (balls should exchange velocities)
    using default values of m1 and m2
""")
# TODO: try attaching the video generated from elastic_collisions.py
# pytest_movie_1d_dt_0.5.mp4
def test_collision_1d_1():
    v1_f, v2_f = ec.collision_1d(v1_i=1, v2_i=-2)


