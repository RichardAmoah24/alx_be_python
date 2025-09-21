# task_reminder.py
# A program that processes a single task based on priority and time sensitivity.

# --- Prompt user for task details ---
task = input("Enter the task description: ").strip()
priority = input("Enter the task priority (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# --- Process task with match case ---
match priority:
    case "high":
        reminder = f" {task} is a HIGH priority task."
    case "medium":
        reminder = f" {task} is a MEDIUM priority task."
    case "low":
        reminder = f" '{task} is a LOW priority task."
    case _:
        reminder = f" {task} has an UNKNOWN priority."

# --- Modify reminder if task is time-bound ---
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# --- Print the customized reminder ---
print("\n=== Task Reminder ===")
print(reminder)
