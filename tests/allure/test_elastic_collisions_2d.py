import allure
import pytest

from pycontest import elastic_collisions as ec
from pycontest.utils import momentum, E_kin


# let's start from 2 balls that have only x velocity, and r12 also has only x component
@allure.tag("elastic_2d", "physics", "collision")
@allure.title("Test elastic function with expected equal values of mass by default")
@allure.description("""
    2d are more complicated, depends on the vector r12
    Similar to the 1d cases
""")
def test_collision_2d_1():
    v1_f, v2_f = ec.collision_2d(v1=[1, 0], v2=[-2, 0], r12=[1, 0], m1=1, m2=1)
    assert (v1_f == [-2, 0]).all()
    assert (v2_f == [1, 0]).all()

# you cannow do the same for y components
def test_collision_2d_2():
    pass

# you can also check the energy and momentum



