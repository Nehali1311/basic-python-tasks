# Function to calculate factorial using a loop
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# # Take input from user
# number = int(input("please enter number : "))
#
# # Print the factorial
# print(f"The factorial of {number} is: {factorial(number)}")

import math

# Ask user for input
num = float(input("please enter number : "))

# Perform calculations using math module
sqrt_val = math.sqrt(num)
log_val = math.log(num)     # natural logarithm (base e)
sine_val = math.sin(num)    # sine of the number in radians

# Display results
print(f"Square root : {sqrt_val}")
print(f"Logarithm : {log_val}")
print(f"Sine : {sine_val}")

