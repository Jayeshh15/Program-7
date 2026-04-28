# Import all modules from utils package
from utils import math_tools, datetime_tools, random_tools, file_tools
import uuid  # built-in module for unique ID

def menu():
    while True:
        print("\n=== Multi-Utility Toolkit ===")
        print("1. Math Tools")
        print("2. Date & Time Tools")
        print("3. Random Tools")
        print("4. UUID Generator")
        print("5. File Tools")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            math_tools.run()

        elif choice == "2":
            datetime_tools.run()

        elif choice == "3":
            random_tools.run()

        elif choice == "4":
            print("Generated UUID:", uuid.uuid4())

        elif choice == "5":
            file_tools.run()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()