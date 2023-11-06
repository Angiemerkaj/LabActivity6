#!/usr/bin/env
#Enxhi Merkaj 11/5/2023

import math

# Get the user input for radians
radians = float(input("Enter the value in radians: "))

# Convert radians to degrees using the formula
degrees_conversion = radians * (180 / math.pi)

# Use the degrees function from the math module to calculate the conversion
degrees_math = math.degrees(radians)

# Print the conversion using the formula and the math module
print("Conversion using the formula:", degrees_conversion)
print("Conversion using math.degrees:", degrees_math)
