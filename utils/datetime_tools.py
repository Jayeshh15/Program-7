from datetime import datetime

# Show current date & time
def current_datetime():
    print("Current Date & Time:", datetime.now())

# Difference between two dates
def date_difference():
    d1 = input("Enter first date (YYYY-MM-DD): ")
    d2 = input("Enter second date (YYYY-MM-DD): ")

    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")

    print("Difference:", abs((d2 - d1).days), "days")

# Format current date
def format_date():
    now = datetime.now()
    print("Formatted Date:", now.strftime("%d-%m-%Y %H:%M:%S"))

# Menu
def run():
    while True:
        print("\n-- Date & Time Tools --")
        print("1. Current Date-Time")
        print("2. Date Difference")
        print("3. Format Date")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            current_datetime()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            format_date()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")