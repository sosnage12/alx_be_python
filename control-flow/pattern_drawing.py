# pattern_drawing.py
# Draw square pattern using while + nested for loops

# Prompt for user input
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # new line after each row
    row += 1
