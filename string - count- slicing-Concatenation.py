# Chapter 6: Strings - Examples and Functions

# --- Concept: String as a Sequence & Looping ---
fruit = 'banana'
count = 0
for char in fruit:
    if char == 'a':
        count = count + 1
print(f"Number of 'a's in '{fruit}': {count}")
# A more Pythonic way using the count() method
print(f"Using .count() method: {fruit.count('a')}")
print("-" * 20)


# --- Concept: Slicing ---
s = 'Monty Python'
print(f"Original string: '{s}'")
# Slicing from index 1 up to (but not including) 5
print(f"Slice [1:5] gives: '{s[1:5]}'")
# Slicing from index 6 up to (but not including) 8
print(f"Slice [6:8] gives: '{s[6:8]}'")
# Slicing from index 0 up to 5
print(f"Slice [:5] gives: '{s[:5]}'")
# Slicing from index 6 to the end
print(f"Slice [6:] gives: '{s[6:]}'")
print("-" * 20)


# --- Concept: Immutability and Concatenation ---
word = 'pesto'
# We cannot change the string directly, so we create a new one.
new_word = 'r' + word[1:]
print(f"Changing '{word}' to '{new_word}'")
print("-" * 20)


# --- Concept: The 'in' operator as a logical check ---
def find_in_string(main_string, substring):
    """
    Checks if a substring exists within a main string and prints the result.
    """
    print(f"Searching for '{substring}' in '{main_string}'...")
    if substring in main_string:
        print("--> Found it!")
    else:
        print("--> Not found.")

# Calling the function with different arguments
#find_in_string('programming', 'gram')
#find_in_string('python for everybody', 'java')
