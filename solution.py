"""A solution to 4 quads. It will take 6 weeks for trainee to work with everybody once and 3 trainees twice."""

import random
from pandas import DataFrame
from main import names, MISSING

random.shuffle(names)
names += [""]*MISSING


def make_quad(quad_1, quad_2, quad_3, quad_4):
    "Make quad"
    return DataFrame({
        "Quad 1": [names[quad] for quad in quad_1],
        "Quad 2": [names[quad] for quad in quad_2],
        "Quad 3": [names[quad] for quad in quad_3],
        "Quad 4": [names[quad] for quad in quad_4],
    })


print("\nWeek 1")  # Horizontal
print(make_quad([0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]))

print("\nWeek 2")  # Vertical
print(make_quad([0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]))

print("\nWeek 3")  # Diagonal
print(make_quad([0, 5, 10, 15], [1, 6, 11, 12], [2, 7, 8, 13], [3, 4, 9, 14]))

print("\nWeek 4")  # Zig-zag 1
print(make_quad([0, 9, 2, 11], [4, 13, 6, 15], [8, 1, 10, 3], [12, 5, 14, 7]))

print("\nWeek 5")  # Zig-zag 2
print(make_quad([0, 6, 8, 14], [1, 7, 9, 15], [2, 4, 10, 12], [3, 5, 11, 13]))

print("\nWeek 6")  # Opposite Diagonal
print(make_quad([0, 7, 10, 13], [1, 4, 11, 14], [2, 5, 8, 15], [3, 6, 9, 12]))
