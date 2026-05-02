python-learning-journey 
# 1. Display a clear welcome message
print("Welcome to the Gross Pay Calculator")

# 2. Get user input with better prompts
# and convert the type to float to support decimal numbers
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate per Hour: "))

# 3. Calculate the gross pay
pay = hours * rate

# 4. Display the final result using an f-string for a clean and readable output
print(f"Gross Pay: {pay}")
