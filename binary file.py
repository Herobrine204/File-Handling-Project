import pickle
import os

FILENAME = input("Enter the name of binary file to be created: ")


def write_records():
    n = int(input("Enter number of students to write: "))
    records = []
    for _ in range(n):
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        records.append({"roll": roll, "name": name, "marks": marks})

    with open(FILENAME, "wb") as f:
        pickle.dump(records, f)
    print(" Records written successfully.")

def read_records():
    if not os.path.exists(FILENAME):
        print(" File not found.")
        return

    with open(FILENAME, "rb") as f:
        records = pickle.load(f)
        print("\n All Student Records:")
        for rec in records:
            print(rec)

def append_records():
    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            records = pickle.load(f)
    else:
        records = []

    n = int(input("Enter number of students to append: "))
    for _ in range(n):
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        records.append({"roll": roll, "name": name, "marks": marks})

    with open(FILENAME, "wb") as f:
        pickle.dump(records, f)
    print(" Records appended successfully.")

def search_record():
    if not os.path.exists(FILENAME):
        print(" File not found.")
        return

    roll_search = int(input("Enter roll number to search: "))
    with open(FILENAME, "rb") as f:
        records = pickle.load(f)

    found = False
    for rec in records:
        if rec["roll"] == roll_search:
            print("🔍 Record found:")
            print(rec)
            found = True
            break

    if not found:
        print(" Record not found.")

def delete_record():
    if not os.path.exists(FILENAME):
        print(" File not found.")
        return

    roll_delete = int(input("Enter roll number to delete: "))
    with open(FILENAME, "rb") as f:
        records = pickle.load(f)

    new_records = [rec for rec in records if rec["roll"] != roll_delete]

    if len(records) == len(new_records):
        print(" Record not found.")
    else:
        with open(FILENAME, "wb") as f:
            pickle.dump(new_records, f)
        print(" Record deleted successfully.")

def menu():
    while True:
        print("\n===== BINARY FILE STUDENT MANAGER =====")
        print("1. Write new records")
        print("2. Read all records")
        print("3. Append new records")
        print("4. Search by roll number")
        print("5. Delete by roll number")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            write_records()
        elif choice == "2":
            read_records()
        elif choice == "3":
            append_records()
        elif choice == "4":
            search_record()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("❗ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
