# Student Score Manager
'''
Develop a Python program to manage student scores. The program will:
1. Store students and their scores.
2. Allow adding, updating, and deleting student scores.
3. Calculate the average score.

Task Details
1. Create Initial Data Structure
    - Use a dictionary where:
        - Keys are student names (strings).
        - Values are their scores (integers).
2. Implement Basic Functions Write the following functions:
    1. Add a Student
        - Input:
            - Student name.
            - Student score.
        - Add the student to the dictionary.
        - If the student already exists, print a message saying, "Student already exists."
    2. Update a Score
        - Input:
            - Student name.
            - New score.
            - Update the student's score in the dictionary.
            - If the student doesn't exist, print a message saying, "Student not found."
    3. Delete a Student
        - Input:
            - Student name.
        - Remove the student from the dictionary.
        - If the student doesn't exist, print a message saying, "Student not found."
    4. Calculate the Average Score
        - Calculate the average of all student scores in the dictionary.
        - Print the average score.

'''

# ข้อมูลเริ่มต้น ซึ่งจะกำหนดให้ ชื่อของนักเรียน >> Key และ คะแนน >> value
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}


# สร้าง function เพื่อเพิ่มนักเรียนไปใน dict : students
def add_student():
    name = input("Enter student name: ") # ให้ป้อนชื่อของนักเรียน
    score = int(input("Enter student score: ")) # ให้ป้อนคะแนนของนักเรียน
    
    if name in students: # ถ้า name ของนักเรียนอยู่ใน student จะไม่ได้ทำอะไรและแสดงข้อความ
        print("Student already exists!!")
    else: # ถ้า name ของนักเรียนไม่อยู่ใน student ให้เพิ่ม name แลพ score ลงใน student พร้อมกับแสดงข้อความ
        students[name] = score
        print("Student added successfully!")

# สร้าง function เพื่อแก้ไข score ล่าสุดของ นักเรียนไปใน dict : students
def update_score():
    name = input("Enter student name: ") # ให้ป้อนชื่อของนักเรียน
    
    if name not in students: # ถ้า name ของนักเรียนไม่อยู่ใน student จะไม่ได้ทำอะไรและแสดงข้อความ
        print("Student not found!!")
    else: # ถ้า name ของนักเรียนอยู่ใน student ให้กรอก score แล้วเพิ่มไปใน name ของนักเรียนคนนั้น
        new_score = int(input("Enter new score: "))
        students[name] = new_score
        print("Score updated for ", name)

# สร้าง function เพื่อลบรายชื่อนักเรียนไปใน dict : students
def delete_student():
    name = input("Enter student name to delete: ") # ให้ป้อนชื่อของนักเรียน
    
    if name in students: # ถ้า name ของนักเรียนอยู่ใน student จะให้ลบ name ของนักเรียนใน student พร้อมกับแสดงข้อความ
        del students[name]
        print("Student deleted successfully!")
    else: # ถ้า name ของนักเรียนไม่อยู่ใน student จะไม่ได้ทำอะไรและแสดงข้อความ
        print("Student not found.")

# สร้าง function เพื่อคำนวณคะแนนเฉลี่ยของรายชื่อนักเรียนใน dict : students
def calculate_average():
    if len(students) == 0: # ถ้าขนาดของนักเรียน = 0 (หรือไม่มีนักเรียนในนี้ class เลย) จะไม่ได้ทำอะไรและแสดงข้อความ
        print("No students available.")
    else: # ถ้ามีนักเรียน จะนำคะแนนรวมของนักเรียน หารด้วย ขนาดของนักเรียนทั้งหมด พร้อมกับแสดงข้อความ
        avg_score = sum(students.values()) / len(students)
        print("Average score :", avg_score) 

# สร้าง function เมนูเพื่อให้ user ได้เลือกใช้งาน
def display_menu():
    while True: # สร้าง loop ให้เลือก menu
        print("\nStudent Score Manager")
        print("1. Add a student")
        print("2. Update a score")
        print("3. Delete a student")
        print("4. Calculate average score")
        print("5. Exit")
        
        choice = input("Choose an option: ") # ให้ป้อน menu ที่ต้องการเลือก
        
        if choice == "1": # ถ้า choice = 1 จะเรียกใช้ function : add_student()
            add_student()
        elif choice == "2": # ถ้า choice = 2 จะเรียกใช้ function : update_score()
            update_score()
        elif choice == "3": # ถ้า choice = 3 จะเรียกใช้ function : delete_student()
            delete_student()
        elif choice == "4": # ถ้า choice = 4 จะเรียกใช้ function : calculate_average()
            calculate_average()
        elif choice == "5": # ถ้า choice = 5 จะแสดงข้อความพร้อมกับหยุดการใช้ loop (หยุดการทำงาน!!)
            print("Exiting program. Goodbye!")
            break
        else: # ถ้า choice ไม่ใช่เลขที่กำหนดในเงื่อนไข จะแสดงข้อความพร้อมกับเริ่มการทำงานของ loop ใหม่
            print("Invalid choice. Please try again.")

# เรียกใช้ function
display_menu()
