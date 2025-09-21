# pattern_drawing.py
# A program that draws a square pattern of asterisks (*) based on user input.

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to control rows
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing one row
    print()
    # Increment row counter
    row += 1
