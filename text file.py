import os

FILENAME = input("Enter the name of file to be created: ")

def write_to_file():
    data = input("Enter text to write to the file: ")
    try:
        with open(FILENAME, "w") as file:
            file.write(data)
        print(" Data written successfully.")
    except Exception as e:
        print(f" Error writing to file: {e}")

def append_to_file():
    data = input("Enter text to append to the file: ")
    try:
        with open(FILENAME, "a") as file:
            file.write("\n" + data)
        print("Data appended successfully.")
    except Exception as e:
        print(f" Error appending to file: {e}")

def read_file():
    try:
        with open(FILENAME, "r") as file:
            content = file.read()
        print("\n File Content:\n")
        print(content)
    except FileNotFoundError:
        print("File not found. Please write to it first.")
    except Exception as e:
        print(f"Error reading file: {e}")
        
def search_word():
    word = input("Enter word to search: ")
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
        found = False
        for i, line in enumerate(lines, 1):
            if word in line:
                print(f" Found in line {i}: {line.strip()}")
                found = True
        if not found:
            print(" Word not found.")
    except Exception as e:
        print(f"Error searching file: {e}")

def menu():
    while True:
        print("\n==== TEXT FILE HANDLER ====")
        print("1. Write to file")
        print("2. Append to file")
        print("3. Read file")
        print("4. Search word")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            write_to_file()
        elif choice == "2":
            append_to_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            search_word()
        elif choice == "5":
            print(" Exiting. Goodbye!")
            break
        else:
            print(" ! Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
