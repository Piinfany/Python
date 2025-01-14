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
    name = input("Enter student name: ").strip() # ให้ป้อนชื่อของนักเรียน
    if name in students: # ถ้า name ของนักเรียนอยู่ใน student จะไม่ได้ทำอะไรและแสดงข้อความ
        print("Student already exists!!")
        return
    score = get_valid_score() # ถ้าไม่มีก็ให้ผู้ใช้กรอกคะแนน และเรียกฟังก์ชันเพื่อรับคะแนนที่ถูกต้อง 
    students[name] = score # เพิ่ม name และ score ลงใน student พร้อมกับแสดงข้อความ
    print(f"Student '{name}' added successfully!")

# สร้าง function เพื่อแก้ไข score ล่าสุดของ นักเรียนไปใน dict : students
def update_score():
    name = input("Enter student name: ").strip() # ให้ป้อนชื่อของนักเรียน
    if name not in students: # ถ้า name ของนักเรียนไม่อยู่ใน student จะไม่ได้ทำอะไรและแสดงข้อความ
        print(f"Students '{name}' not found!")
    score = get_valid_score("Enter the new score :") # กรอกคะแนนใหม่
    students[name] = score # เพิ่ม new score ลงใน student พร้อมกับแสดงข้อความ
    print(f"Score for '{name}' updated successfully!")


# สร้าง function เพื่อลบรายชื่อนักเรียนไปใน dict : students
def delete_student():
    name = input("Enter student name to delete: ").strip() # ให้ป้อนชื่อของนักเรียน
    if students.pop(name, None): # ถ้าชื่อนั้นมีใน students ก็จะลบชื่อออกจาก students ถ้ามี และจะแสดงข้อความ
        print(f"Student '{name}' deleted successfully!")
    else:
        print(f"Student '{name}' not found!")


# สร้าง function เพื่อคำนวณคะแนนเฉลี่ยของรายชื่อนักเรียนใน dict : students
def calculate_average():
    if not students: # ถ้าไม่มีนักเรียน จะไม่ได้ทำอะไรและแสดงข้อความ
        print("No students available.")
        return
   # ถ้ามีนักเรียน จะนำคะแนนรวมของนักเรียน หารด้วย ขนาดของนักเรียนทั้งหมด พร้อมกับแสดงข้อความ
    avg_score = sum(students.values()) / len(students) # คำนวณคะแนนเฉลี่ย
    print("Average score :", avg_score)

def get_valid_score(prompt="Enter student score : "):
    while True: # ใช้ loop เพื่อให้ผู้ใช้กรอกคะแนนที่เป็นจำนวนเต็ม
        try:
            return int(input(prompt)) # พยายามแปลงค่าที่ผู้ใช้กรอกเป็นจำนวนเต็ม
        except ValueError: # ถ้าเกิดข้อผิดพลาดในการแปลง จะแสดงข้อความว่าไม่ใช่จำนวนเต็ม
            print("Invalid input. Please enter an integer.")

# สร้าง function เมนูเพื่อให้ user ได้เลือกใช้งาน
def display_menu():
    # สร้างเมนูไว้เรียกใช้งาน
    menu_options = {
        "1": add_student,
        "2": update_score,
        "3": delete_student,
        "4": calculate_average,
        "5": exit_program,
    }
    while True: # สร้าง loop ให้เลือก menu
        print("\nStudent Score Manager")
        print("1. Add a student")
        print("2. Update a score")
        print("3. Delete a student")
        print("4. Calculate average score")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip() # ให้ป้อน menu ที่ต้องการเลือก
        # ใช้ menu_options.get(choice) เพื่อหาฟังก์ชันที่ตรงกับตัวเลือกที่เลือก
        action = menu_options.get(choice) # หาเมนูที่เลือก
        if action:
            action() # ถ้าเมนูที่เลือกถูกต้อง จะเรียกใช้งานฟังก์ชันที่เกี่ยวข้อง
        else:
            print("Invalid choice. Please try again.") # ถ้าเลือกเมนูไม่ถูกต้อง

# สร้าง function เพื่อออกจากโปรแกรม
def exit_program():
    print("Exiting program. Goodbye!")
    sys.exit() # ออกจากโปรแกรม

# เรียกใช้ function
# ใช้การตรวจสอบ if __name__ == "__main__": เพื่อให้โปรแกรมเริ่มทำงานเมื่อเปิดไฟล์นี้เป็นโปรแกรมหลัก (ไม่ใช่เมื่อทำการนำเข้าเป็นโมดูลในไฟล์อื่น)
if __name__ == "__main__":
    display_menu() # เรียกใช้งานฟังก์ชัน display_menu() เพื่อเริ่มต้นโปรแกรม
