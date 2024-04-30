"""A solution to 4 quads. It will take 5 weeks for trainee to work with everybody once and 0 trainees twice."""

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

# The order of the weeks is irrelevant
print("\nWeek 1")
print(make_quad([0, 1, 2, 3], [4, 7, 10, 13], [5, 8, 11, 14], [6, 9, 12, 15]))

print("\nWeek 2")
print(make_quad([0, 4, 5, 6], [1, 7, 11, 15], [2, 8, 12, 13], [3, 9, 10, 14]))

print("\nWeek 3")
print(make_quad([0, 7, 8, 9], [1, 4, 12, 14], [2, 5, 10, 15], [3, 6, 11, 13]))

print("\nWeek 4")
print(make_quad([0, 10, 11, 12], [1, 5, 9, 13], [2, 6, 7, 14], [3, 4, 8, 15]))

print("\nWeek 5")
print(make_quad([0, 13, 14, 15], [1, 6, 8, 10], [2, 7, 9, 11], [3, 5, 7, 12]))
