from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days):
    """Calculate the future date after adding 'days' to the current date."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Error: Please enter a valid integer for number of days.")

if __name__ == "__main__":
    main()
