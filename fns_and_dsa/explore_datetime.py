# explore_datetime.py

# 1. Import datetime components
from datetime import datetime, timedelta

# 2. Function to display the current date and time


def display_current_datetime():
    # save the current date inside current_date variable
    current_date = datetime.now()
    # format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # return the formatted date
    return formatted_date

# 3. Function to calculate a future date


def calculate_future_date(days):
    # save the current date
    current_date = datetime.now()
    # calculate the future date
    future_date = current_date + timedelta(days=days)
    # format the future date
    return future_date.strftime("%Y-%m-%d")


# Run the program
if __name__ == "__main__":
    # Part 1: Display current date and time
    print("Current Date and Time:", display_current_datetime())

    # Part 2: Calculate a future date
    try:
        number_of_days = int(
            input("Enter the number of days to add to the current date: "))
        print("Future Date:", calculate_future_date(number_of_days))
    except ValueError:
        print("Please enter a valid integer for the number of days.")
