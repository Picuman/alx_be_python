import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + datetime.timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

if __name__ == "__main__":
    # Part 1: Display the Current Date and Time
    current_date = display_current_datetime()

    # Part 2: Calculate a Future Date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")
