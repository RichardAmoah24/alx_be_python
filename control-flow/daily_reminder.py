# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop to make sure priority input is valid
while priority not in ["high", "medium", "low"]:
    print("Invalid input. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Process the Task Based on Priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task with unspecified priority"

# Add time-bound check
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Provide a Customized Reminder
print("\nReminder:", reminder)
