import random

# Generate random number
def random_number():
    print("Random Number:", random.randint(1, 100))

# Generate random list
def random_list():
    lst = [random.randint(1, 50) for _ in range(5)]
    print("Random List:", lst)

# Shuffle list
def shuffle_list():
    lst = [1, 2, 3, 4, 5]
    random.shuffle(lst)
    print("Shuffled List:", lst)

# Menu
def run():
    while True:
        print("\n-- Random Tools --")
        print("1. Random Number")
        print("2. Random List")
        print("3. Shuffle List")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            random_number()
        elif choice == "2":
            random_list()
        elif choice == "3":
            shuffle_list()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")