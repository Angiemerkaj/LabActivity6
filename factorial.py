#!/usr/bin/env
#Enxhi Merkaj 11/5/2023

import math

# Get the user input for the value to calculate the factorial
n = int(input("Enter a non-negative integer: "))

# Calculate the factorial using a for loop
factorial_user = 1
for i in range(1, n + 1):
    factorial_user *= i

# Calculate the factorial using the math module
factorial_math = math.factorial(n)

# Print both values
print("Factorial calculated using a for loop:", factorial_user)
print("Factorial calculated using math.factorial function:", factorial_math)
