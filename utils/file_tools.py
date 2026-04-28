# Create file
def create_file():
    name = input("Enter filename: ")
    with open(name, "w") as f:
        f.write("This is a sample file.")
    print("File created successfully!")

# Read file
def read_file():
    name = input("Enter filename: ")
    try:
        with open(name, "r") as f:
            print("\nFile Content:\n", f.read())
    except:
        print("File not found!")

# Append to file
def append_file():
    name = input("Enter filename: ")
    data = input("Enter text to append: ")
    with open(name, "a") as f:
        f.write("\n" + data)
    print("Data appended!")

# Menu
def run():
    while True:
        print("\n-- File Tools --")
        print("1. Create File")
        print("2. Read File")
        print("3. Append File")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            append_file()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")