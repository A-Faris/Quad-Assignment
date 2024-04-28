"""To find the arrangement of quads"""

import math

names = ["Alina", "Berkay", "Dan", "Ella",
         "Eyuale", "Fariha", "Faris", "Freddy",
         "Joe", "Nabiha", "Pedro", "Punima",
         "Umar", "Will", "Zhi"]

QUAD_SIZE = 4
EVERY_NUM_WEEK = 1
print(f"""The quad size is {QUAD_SIZE}
      and they change every {EVERY_NUM_WEEK} weeks.""")

NUM_TRAINEES = len(names)

NUM_QUADS = math.ceil(NUM_TRAINEES/QUAD_SIZE)
FULL = QUAD_SIZE * NUM_QUADS  # Number of trainees if every quad was full

MISSING = FULL - NUM_TRAINEES
print(f"""There's {NUM_TRAINEES} trainees so there will be
      {NUM_QUADS} quads with a quad missing {MISSING} member.""")

# Minimum number of weeks/quads needed for each person to work with each other once
MIN_NUM_WEEKS = math.ceil((FULL-1)/(QUAD_SIZE - 1)) * EVERY_NUM_WEEK
MIN_NUM_QUADS = math.ceil((FULL-1)/(QUAD_SIZE - 1))

# Number of times a trainee will work with the same person
SAME_PERSON = MIN_NUM_QUADS*(QUAD_SIZE - 1) - (FULL-1)
print(f"""It will take at least {MIN_NUM_WEEKS} weeks/{MIN_NUM_QUADS}
      quads for each trainee to work with each other once and {SAME_PERSON} trainees twice.""")
