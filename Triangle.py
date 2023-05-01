import numpy as np


class Triangle:
    def __init__(self,
                 angle_a=0,
                 angle_b=0,
                 angle_c=0,
                 side_adjacent=0,
                 side_opposite=0,
                 side_hypotenuse=0
                 ):

        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c

        self.side_adjacent = side_adjacent
        self.side_opposite = side_opposite
        self.side_hypotenuse = side_hypotenuse

        self.angle_a_rad = self.convert_deg_to_rad(float(self.angle_a))
        self.angle_b_rad = self.convert_deg_to_rad(float(self.angle_b))
        self.angle_c_rad = self.convert_deg_to_rad(float(self.angle_c))

        self.is_known_adjacent = False
        self.is_known_opposite = False
        self.is_known_hypotenuse = False

        self.is_known_angle_a = False
        self.is_known_angle_b = False
        self.is_known_angle_c = False

        self.num_known_sides = 0
        self.num_known_angles = 0

        self.list_angles = []
        self.list_sides = []
        self.assign_list_angles()
        self.assign_list_sides()

        self.set_known_angles()

        if self.num_known_angles == 2:
            if not self.is_known_angle_a:
                self.angle_a = self.calculate_missing_angle()
            elif not self.is_known_angle_b:
                self.angle_b = self.calculate_missing_angle()
            elif not self.is_known_angle_c:
                self.angle_c = self.calculate_missing_angle()
            self.set_known_angles()
            self.assign_list_angles()

        self.set_known_sides()

        if self.num_known_sides == 2:
            if int(self.side_hypotenuse) == 0:
                self.calculate_hypotenuse()
            else:
                self.calculate_missing_side()
            self.set_known_sides()
            self.assign_list_sides()

    """---------------------------------------------------------------------"""

    def set_known_sides(self):
        """Sets the boolean variables for whether a side is known"""
        if self.side_adjacent != 0:
            self.is_known_adjacent = True
            self.num_known_sides += 1
        if self.side_opposite != 0:
            self.is_known_opposite = True
            self.num_known_sides += 1
        if self.side_hypotenuse != 0:
            self.is_known_hypotenuse = True
            self.num_known_sides += 1

    def set_known_angles(self):
        """Sets the boolean variables for whether an angle is known"""
        if self.angle_a != 0:
            self.is_known_angle_a = True
            self.num_known_angles += 1
        if self.angle_b != 0:
            self.is_known_angle_b = True
            self.num_known_angles += 1
        if self.angle_c != 0:
            self.is_known_angle_c = True
            self.num_known_angles += 1

    def assign_list_angles(self):
        """Assigns the current values of the angles to a list"""
        self.list_angles = [self.angle_a, self.angle_b, self.angle_c]

    def assign_list_sides(self):
        """Assigns the current values of the sides to a list"""
        self.list_sides = [self.side_adjacent, self.side_opposite, self.side_hypotenuse]

    def print_sides(self):
        """Prints sides of the triangle"""
        print(f"Adj - {self.side_adjacent}")
        print(f"Opp - {self.side_opposite}")
        print(f"Hyp - {self.side_hypotenuse}")

    def print_angles(self):
        """Prints angles of the triangle"""
        print(f"Angle A - {self.angle_a}")
        print(f"Angle B - {self.angle_b}")
        print(f"Angle C - {self.angle_c}")

    def count_angles(self):
        """Counts known angles of the triangle"""
        for angle in self.list_angles:
            if angle > 0:
                self.num_known_angles += 1

    def count_sides(self):
        """Counts known sides of the triangle"""
        for side in self.list_sides:
            if side > 0:
                self.num_known_sides += 1

    def convert_deg_to_rad(self, degree):
        """Returns given degree as radians"""
        return degree * (np.pi / 180)

    def convert_rad_to_deg(self, radian):
        """Returns given radian as degrees"""
        return radian * (180/np.pi)

    def calculate_hypotenuse(self):
        """Calculates the hypotenuse of a right triangle given the two known sides

        Precondition: The opposite and adjacent sides are known
        Postcondition: The hypotenuse of the Triangle is assigned"""
        square_a = self.side_opposite ** 2
        square_b = self.side_adjacent ** 2
        self.side_hypotenuse = np.sqrt(square_a + square_b)

    def calculate_side(self, known_side):
        """Calculates missing side of a right triangle given the hypotenuse
        and one known side

        Precondition: Hypotenuse and one side are known
        Postcondition: Returns the calculated missing sides length"""
        square_side = known_side ** 2
        square_hypotenuse = self.side_hypotenuse ** 2
        difference = square_hypotenuse - square_side
        return np.sqrt(difference)

    def calculate_missing_angle(self):
        """Determines the missing angle of a triangle given two angles

        Precondition: Two angles must be known prior to calling
        Postcondition: Returns remaining angle in degrees"""
        sum_angles = 0
        for angle in self.list_angles:
            if angle == 0:
                continue
            else:
                sum_angles += angle

        return 180 - sum_angles

    def calculate_missing_side(self):
        """Determines the remaining side's length, not the hypotenuse.

        Precondition: The hypotenuse of the triangle is known
        Postcondition: The missing side of the triangle is assigned"""
        if self.num_known_sides < 2:
            return

        elif self.side_adjacent == 0:
            self.side_adjacent = self.calculate_side(self.side_opposite)

        elif self.side_opposite == 0:
            self.side_opposite = self.calculate_side(self.side_adjacent)
            