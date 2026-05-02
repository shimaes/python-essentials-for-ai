#python-for-everybody
#python-learning-journey



# Author: [Shima Eslami]
# Date: 2026-03-16
# Chapter 3 Exercise: Advanced Pay Calculator with Overtime

# Get input from the user
hrs_str = input("Enter Hours: ")
rate_str = input("Enter Rate: ")

# Convert inputs to float within a try-except block for validation
try:
    f_hrs = float(hrs_str)
    f_rate = float(rate_str)
except:
    print("Error, please enter numeric input")
    # Quit the program if the input is invalid
    quit()

# Calculate the pay
if f_hrs > 40:
    # Overtime logic
    regular_pay = 40 * f_rate
    overtime_pay = (f_hrs - 40) * (f_rate * 1.5)
    total_pay = regular_pay + overtime_pay
else:
    # Regular pay logic
    total_pay = f_hrs * f_rate

# Print the final result
print("Pay:", total_pay)
