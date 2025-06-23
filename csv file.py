import csv
import os

FILENAME = input("Enter the name of file: ")
HEADERS = ["EmpID", "Name", "Salary"]

def write_records():
    n = int(input("Enter number of employees to enter: "))
    with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)
        for _ in range(n):
            EmpID = input("Enter employee id: ")
            name = input("Enter name: ")
            salary = input("Enter salary: ")
            writer.writerow([EmpID, name, salary])
    print(" Records written successfully.")

def read_records():
    if not os.path.exists(FILENAME):
        print(" File not found.")
        return

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def append_records():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS) 

    n = int(input("Enter number of employees to append: "))
    with open(FILENAME, "a", newline='') as file:
        writer = csv.writer(file)
        for _ in range(n):
            EmpID = input("Enter employee id: ")
            name = input("Enter name: ")
            salary = input("Enter salary: ")
            writer.writerow([EmpID, name, salary])
    print(" Records appended successfully.")

def search_record():
    Emp_ID = input("Enter Employee ID to search: ")
    found = False

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == Emp_ID:
                print(" Record found:", row)
                found = True
                break
    if not found:
        print(" Record not found.")

def delete_record():
    Emp_ID = input("Enter Emp_ID to delete: ")
    new_data = []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != Emp_ID:
                new_data.append(row)

    if len(new_data) == 0 or (len(new_data) == 1 and new_data[0] == HEADERS):
        print(" Record not found.")
    else:
        with open(FILENAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
        print(" Record deleted successfully.")

def menu():
    while True:
        print("\n===== CSV Employee MANAGER =====")
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
            print(" Exiting...")
            break
        else:
            print("! Invalid choice, try again.")

if __name__ == "__main__":
    menu()
