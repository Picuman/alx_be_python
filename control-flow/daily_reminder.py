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
if time_bound == "yes":
    print(f"**Reminder:** '{task}' is a high prority task that requires immediatee attention today!")
else:
    print(f"**Note:** '{task}' is a low priority task. Consider completing it when you have free time.")
    
    print(f"Priority (high/medium/low):" , priority )
    print(f"Is it time-bound? (yes/no):" , time_bound )

 else:
      print("Invalid priority level entered.")
     
if time_bound == "yes":
    print(f"**{task}:** that requires immediate attention today!")
 

