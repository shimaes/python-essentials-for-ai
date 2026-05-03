# Author: [Shima Es]
# Date: 2026-03-18
# Chapter 5 Challenge: Sum, Count, and Average of User Inputs
# Style: Dr. Chuck's standard approach + robust average calculation

total = 0.0
count = 0

while True:
    sval = input('Enter a number: ')
    
    # Check for the sentinel value to exit
    if sval == 'done':
        break
        
    # Validate and convert the input
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue # Skip the rest of the loop for this iteration
    
    # Update accumulators
    count = count + 1
    total = total + fval

# Final calculation and output
print('All done')

if count > 0:
    average = total / count
    print('Total:', total, 'Count:', count, 'Average:', average)
else:
    print('No numbers were entered.')
  
