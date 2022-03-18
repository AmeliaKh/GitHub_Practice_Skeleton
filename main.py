import math


class Person():
    def __init__(self, name, age, position_x, position_y):
        self.name = name
        self.age = age
        self.position_x = position_x
        self.position_y = position_y
        self.math_solver = MathSolver()

    def distance_to(self, other_person):
        return self.math_solver.euclidean_distance(
            self.position_x,
            self.position_y,
            other_person.position_x,
            other_person.position_y,
        )

    def age_difference(self, other_person):
        """
        Return the *absolute* age difference between this person and the other person. The "absolute"
        value of a number x is the non-negative value of x e.g the absolute value of -2 is 2 and the
        absolute value of 2 is also 2.
        """
        ######################################################
        # Jessie to complete
        ######################################################

        return 5

class MathSolver():
    def euclidean_distance(self, x1, y1, x2, y2):
        # This is also called the 'Pythagorean distance'
        # = sqrt((x2-x1)^2 + (y2-y1)^2)

        ######################################################
        # Helena to complete
        ######################################################

        return math.sqrt(self.square(self.subtract(y1, x1)) + self.square(self.subtract(y2, x2)))

    def subtract(self, a, b):
        ######################################################
        # Allegra to complete
        ######################################################

        return a + b

    def square(self, a):
        ######################################################
        # Allegra to complete
        ######################################################

        return a