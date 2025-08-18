# Task Reminder Program

# Check if file exists and not empty
import os

filename = "tasks.txt"
if not os.path.exists(filename) or os.path.getsize(filename) == 0:
    with open(filename, "w") as f:
        f.write("Task Reminder Log\n")

# Prompt user for inputs
task = input("Enter your task: ")
time_bound = input("Is this task time-bound? (yes/no): ").lower()
priority = input("Enter priority (High/Medium/Low): ").capitalize()

# Match-case example (reaction based on priority)
match priority:
    case "High":
        reaction = " This needs your full focus!"
    case "Medium":
        reaction = " Manage this task soon."
    case "Low":
        reaction = " Handle it when you have free time."
    case _:
        reaction = "Unknown priority level."

# If statement for time-bound modification
if time_bound == "yes":
    reminder = f"Reminder: '{task}' is a {priority} priority task and requires immediate attention! {reaction}"
else:
    reminder = f"Reminder: '{task}' is a {priority} priority task. {reaction}"

# Provide a customized reminder
print(reminder)

# Save reminder into file
with open(filename, "a") as f:
    f.write(reminder + "\n")
