#!/usr/bin/env
#Enxhi Merkaj 11/5/2023

import random
import math

# Number of random points to generate
num_points = 100000

# Initialize counters for points inside the circle
inside_circle = 0

# Generate random points and check if they fall inside the quarter-circle
for _ in range(num_points):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1

# Calculate the approximation for pi
pi_approximation = (inside_circle / num_points) * 4

# Print the approximation and the value of math.pi
print("Approximation of pi:", pi_approximation)
print("Value of math.pi:", math.pi)
