students = [
    {"id": 101, "name": "Alice Johnson", "age": 20, "course": "Computer Science", "marks": 85},
    {"id": 102, "name": "Bob Smith", "age": 21, "course": "Information Technology", "marks": 78},
    {"id": 103, "name": "Charlie Brown", "age": 19, "course": "Data Science", "marks": 92},
    {"id": 104, "name": "Diana Prince", "age": 22, "course": "Cyber Security", "marks": 88}
    ]

def add_stud():
    sid=int(input("Enter student ID: "))
    for s in students:
        if s["id"]==sid:
            print("Student already exits")
            return
    name=input("Enter name : ")
    age=int(input("Enter age:"))
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    students.append({"id" : sid, "name": name, "age": age,
            "course": course,
            "marks": marks })
        
    print("Student Added successfully")

def view_stud():
    if not students:
        print("No student records found.")
        return
    for s in students:
        print(s)

def search_stud():
    sid = int(input("Enter Student ID to search: "))
    for s in students:
        if s["id"] == sid:
            print(s)
            return
    print("Student not found.")

def update_stud():
    sid = int(input("Enter Student ID to update: "))
    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            s["age"] = int(input("Enter new age: "))
            s["course"] = input("Enter new course: ")
            s["marks"] = int(input("Enter new marks: "))
            print("Student updated successfully!")
            return
    print("Student not found.")

def delete_stud():
    sid = int(input("Enter Student ID to delete: "))
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print("Student not found.")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_stud()
    elif choice == "2":
        view_stud()
    elif choice == "3":
        search_stud()
    elif choice == "4":
        update_stud()
    elif choice == "5":
        delete_stud()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")

