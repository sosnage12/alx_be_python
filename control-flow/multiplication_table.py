# multiplication_table.py
# Generate multiplication table using for loop

# Prompt for user input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
