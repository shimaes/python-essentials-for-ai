# Author: [Shima Eslami]
# Date: 2026-03-17
# Chapter 4: Exercise 1 - Defining a simple function with parameters

def add_two_numbers(a, b):
    """
    This function takes two arguments, converts them to integers,
    calculates their sum, and prints the result.
    """
    # Convert input arguments to integers to ensure mathematical addition
    try:
        num1 = int(a)
        num2 = int(b)
        
        # Calculate the sum
        total = num1 + num2
        
        # Print the final result
        print("The sum is:", total)
        
    except ValueError:
        print("Error: Please provide valid numbers as arguments.")


# --- Function Calls (Examples of how to use it) ---

print("Calling the function with numbers 5 and 7:")
add_two_numbers(5, 7)

print("\nCalling the function with string numbers '10' and '20':")
add_two_numbers("10", "20")

print("\nCalling the function with invalid input to see the error handling:")
add_two_numbers("hello", "world")
