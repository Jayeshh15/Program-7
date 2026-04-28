import math  # math module for calculations

# Factorial function
def factorial():
    n = int(input("Enter number: "))
    print("Factorial:", math.factorial(n))

# Square root function
def sqrt():
    n = int(input("Enter number: "))
    print("Square Root:", math.sqrt(n))

# Trigonometry functions
def trig():
    angle = int(input("Enter angle in degrees: "))
    print("Sin:", math.sin(math.radians(angle)))
    print("Cos:", math.cos(math.radians(angle)))

# Menu for math module
def run():
    while True:
        print("\n-- Math Tools --")
        print("1. Factorial")
        print("2. Square Root")
        print("3. Trigonometry")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            factorial()
        elif choice == "2":
            sqrt()
        elif choice == "3":
            trig()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")