task = input("Enter your task:")
task_priority = input("Priority (high/medium/low):")
lower_task_priority = task_priority.lower()
time_bounded = input("Is it time-bound? (yes/no):")
lower_time_bounded = time_bounded.lower()
match lower_task_priority:
   case "high":
    if lower_time_bounded == "yes":
       print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    elif lower_time_bounded =="no":
       print(f"Reminder: '{task}' is a high priority task Consider completing it when you have free time.")
   case "medium":
    if lower_time_bounded == "yes":
       print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
    elif lower_time_bounded =="no":
       print(f"Reminder: '{task}' is a medium priority task Consider completing it when you have free time.")
   case "low":
    if lower_time_bounded == "yes":
       print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
    elif lower_time_bounded =="no":
       print(f"Reminder: '{task}' is a low priority task Consider completing it when you have free time.")     