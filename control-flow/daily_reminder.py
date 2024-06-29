task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"**high priority task:** {task}")
    case "medium":
        print(f"**medium priority task:** {task}")
    case "low":
        print(f"**low priority task:** {task}")
    case _:
        print(" Invalid priority level entered.")
        

