# Organize your Python project into multiple modules and create a main script that integrates them.

# สร้างโปรเจ็กต์ Python และแบ่งโปรเจ็กต์เป็น module หลายๆ ส่วน และสร้าง script หลักเพื่อนำ function แต่ละ module มาใช้งานร่วมกัน
# สร้างโฟลเดอร์โปรเจ็กต์
# mkdir Environment_Setup3

# เข้าถึงโฟลเดอร์โปรเจ็กต์
# cd Environment_Setup3

# สร้างโฟลเดอร์ย่อย module1, module2, module3
# mkdir module1 module2 module3 

# cd module1
# touch greeting.py
# สร้าง function greeting
# def greeting(name):
#    print(f"Hello {name}, welcome to my Python project from Module 1!")

# cd module2
# touch goodbye.py
# สร้าง function goodbye
# def goodbye(name):
#    print(f"Goodbye {name}, see you again soon from Module 2!")

# cd module3
# touch print_result.py
# สร้าง function สำหรับการแสดงผลลัพธ์
# def print_result(text):
#    print(f"Result: {text}")

# cd ..
# touch main.py
# สร้าง scrip หลัก เพื่อนำ function แต่ละ module มาใช้งานร่วมกัน
# from module1 import greeting
# from module2 import goodbye
# from module3 import print_result

# def main():
#    name = input("Enter your name: ")
#    greeting(name)
#    print_result(greeting)
#    goodbye(name)
#    print_result(goodbye)

# เรียกใช้ function main
# if __name__ == "__main__": # ถ้าไฟล์ถูกเรียกใช้โดยตรงจะเรียกใช้ function main
#    main() # รัน function main

# สร้างโครงสร้างโปรเจ็กต์
# Environment_Setup3/
# ├── myenv/
# ├── module1/greeting
# ├── module2/goodbye
# ├── module3/print_result
# └── main.py

# สร้างไฟล์ main.py ในโฟลเดอร์ Environment_Setup3
# cd ..
# touch main.py
# สร้าง scrip หลัก เพื่อนำ function แต่ละ module มาใช้งานร่วมกัน
from module1.greeting import greet
from module2.goodbye import bye
from module3.print_result import result

def main():
    name = input("\nEnter your name: ")
    text = greet(name)
    result(text)
    text = bye(name)
    result(text)

# เรียกใช้ function main
if __name__ == "__main__": # ถ้าไฟล์ถูกเรียกใช้โดยตรงจะเรียกใช้ function main
    main() # รัน function main