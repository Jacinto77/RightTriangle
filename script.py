import numpy as np


def calculate_side(side, hypotenuse):
    square_side = np.square(side)
    square_hypotenuse = np.square(hypotenuse)
    difference = square_hypotenuse - square_side
    return np.sqrt(difference)


def calculate_remaining_angle(theta):
    return (180 - 90) - theta


def calculate_side_hypotenuse(side_a, side_b):
    square_a = np.square(side_a)
    square_b = np.square(side_b)
    return np.sqrt(square_a + square_b)


print("For the following prompts, input 0 for missing values")
angle_theta = float(input("Angle of theta? >"))

side_adjacent = float(input("Adjacent? >"))
side_opposite = float(input("Opposite? >"))
side_hypotenuse = float(input("Hypotenuse? >"))

calculated_adjacent = np.cos(angle_theta) * side_hypotenuse
calculated_opposite = np.sin(angle_theta) * side_hypotenuse

print(f"Missing Angle = {calculate_remaining_angle(angle_theta)}")
print(f"Adjacent = {side_adjacent}")
print(f"Opposite = {side_opposite}")
print(f"Hypotenuse = {side_hypotenuse}")

print(f"Calc-adj = {calculated_adjacent}")
print(f"Calc-opp = {calculated_opposite}")

print()

if side_hypotenuse == 0:
    side_hypotenuse = calculate_side_hypotenuse(side_opposite, side_adjacent)

if side_opposite == 0:
    side_opposite = calculate_side(side_adjacent, side_hypotenuse)

if side_adjacent == 0:
    side_adjacent = calculate_side(side_opposite, side_hypotenuse)

print(f"Missing Angle = {calculate_remaining_angle(angle_theta)}")
print(f"Adjacent = {side_adjacent}")
print(f"Opposite = {side_opposite}")
print(f"Hypotenuse = {side_hypotenuse}")
print()
print(f"Calc-adj = {calculated_adjacent}")
print(f"Calc-opp = {calculated_opposite}")
print()
