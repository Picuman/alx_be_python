task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case "high":
        priority_message = f"**High Priority Task:** {task}"
    case "medium":
        priority_message = f"**Medium Priority Task:** {task}"
    case "low":
        priority_message = f"**Low Priority Task:** {task}"
    case _:
        priority_message = "Invalid priority level entered."

    if time_bound.lower() == "yes":
        time_bound_message = f"**Reminder:** '{task}' requires immediate attention today!"
    else:
        time_bound_message = f"**Note:** '{task}' is a {priority} priority task. Consider completing it when you have free time."

    
    print(f"{priority_message}\n{time_bound_message}")
else:
    print("Invalid priority level entered.")
