# daily_reminder.py

# Prompt for the task, its priority, and if it's time-bound
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Validate and process the task based on priority and time sensitivity
match priority:
    case "high":
        priority_message = f"**High Priority Task:** {task}"
    case "medium":
        priority_message = f"**Medium Priority Task:** {task}"
    case "low":
        priority_message = f"**Low Priority Task:** {task}"
    case _:
        priority_message = "Invalid priority level entered."

# Check if the priority level is valid before proceeding
if priority in ["high", "medium", "low"]:
    if time_bound.lower() == "yes":
        time_bound_message = f"**Reminder:** '{task}' requires immediate attention today!"
    else:
        time_bound_message = f"**Note:** '{task}' is a {priority} priority task. Consider completing it when you have free time."

    # Provide a customized reminder
    print(f"{priority_message}\n{time_bound_message}")
else:
    print("Invalid priority level entered.")
