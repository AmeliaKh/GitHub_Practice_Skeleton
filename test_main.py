import unittest
from main import *

class TestMain(unittest.TestCase):
    def setUp(self):
        self.bob = Person("Bob", age=22, position_x=10, position_y=5)
        self.alice = Person("Alice", age=30, position_x=2, position_y=3)
        self.math_solver = MathSolver()

    def test_age_difference(self):
        assert self.bob.age_difference(self.alice) == 8

    def test_euclidean_distance(self):
        assert self.math_solver.euclidean_distance(x1=2, y1=4, x2=2, y2=-4) == 8

    def test_subtract(self):
        assert self.math_solver.subtract(3, 4) == -1

    def test_square(self):
        assert self.math_solver.square(4) == 16