# ch06_string_operations.py

# --- Exercise 1: Counting 'a' in 'banana' ---
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(f"Number of 'a' in '{word}': {count}")

# You can also use the built-in count method for comparison
print(f"Using .count() method: {word.count('a')}")
print("-" * 20)


# --- Exercise 2: Extracting domain from a string ---

data_string = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Approach 1: Two-Point Search (More efficient)
def extract_domain_v1(data):
    """
    Extracts the domain using the two-point find method.
    This approach works directly on the original string.
    """
    print("Executing Approach 1: Two-Point Search")
    at_pos = data.find('@')
    # Start searching for a space FROM the position of '@'
    space_pos = data.find(' ', at_pos)
    domain = data[at_pos + 1 : space_pos]
    print(f"The extracted domain is: {domain}\n")
    return domain

# Approach 2: Two-Step Slice (Intuitive and clever)
def extract_domain_v2(data):
    """
    Extracts the domain by creating a temporary substring first.
    This approach simplifies the problem by breaking it down.
    """
    print("Executing Approach 2: Two-Step Slice")
    at_pos = data.find('@')
    # Create a new, smaller string starting from '@'
    from_at_onward = data[at_pos:]
    # Find the first space in the NEW string
    space_in_new_str = from_at_onward.find(' ')
    # Slice the new string to get the domain (remember to skip '@')
    domain = from_at_onward[1:space_in_new_str]
    print(f"The extracted domain is: {domain}\n")
    return domain

# --- Calling the functions to see the results ---
#extract_domain_v1(data_string)
#extract_domain_v2(data_string)
