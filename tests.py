import Triangle

sides = input("enter 3 sides").split()
angles = input("enter 3 angles").split()

triangle = Triangle.Triangle(float(angles[0]), float(angles[1]), float(angles[2]),
                             float(sides[0]), float(sides[1]), float(sides[2]))

triangle.print_sides()
triangle.print_angles()
