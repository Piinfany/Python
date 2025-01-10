# Create a Python program that acts as a simple calculator, allowing users to perform basic arithmetic operations. The program should handle various errors gracefully and provide meaningful feedback to the user.

'''
1. User Input:
    - Prompt the user to enter two numbers and an operator (+, -, *, /, %).
    - Handle cases where:
        - The user inputs invalid numbers (e.g., letters or symbols).
        - The user inputs an invalid operator.
2. Perform Calculation:
    - Perform the calculation based on the operator provided.
    - Handle cases where:
        - Division by zero occurs (for / or % operators).
        - The result of the operation is too large for Python to handle.
3. Graceful Termination:
    - Allow the user to exit the program by entering a specific command (e.g., exit).
    - Ensure the program terminates gracefully after providing feedback for any errors.
4. Looping:
    - Keep the program running until the user decides to exit.
    - After each calculation, ask if the user wants to perform another calculation or exit.

'''

# สร้าง function สำหรับรับค่า parameter 3 ตัวก่อน 
def oper_calculat(number1,number2,oper): 
    try: # พยายามรับค่าที่เป็น float ของ num1,num2
        number1 = float(number1)
        number2 = float(number2)
    except ValueError: # ถ้าป้อนอะไรที่ไม่ใช่ตัวเลขจะแสดง error พร้อมกับข้อความ 
        return "Please enter numeric!!!"
    if oper == '+': # ตรวจสอบเงื่อนไข +
        return number1 + number2
    elif oper == '-': # ตรวจสอบเงื่อนไข -
        return number1 - number2
    elif oper == '*': # ตรวจสอบเงื่อนไข *
        return number1 * number2
    elif oper == '/': # ตรวจสอบเงื่อนไข /
        if number2 == 0: # ตรวจสอบเงื่อนไขถ้าตัวหารเป็น 0
            return "ไม่สามารถใช้ตัวหารเป็นศูนย์ได้"
        return number1 / number2
    elif oper == '%': # ตรวจสอบเงื่อนไข %
        if number2 == 0: # ตรวจสอบเงื่อนไขถ้าตัวหารเป็น 0
            return "ไม่สามารถใช้ตัวหารเป็นศูนย์ได้"
        return number1 % number2
    else : # ตรวจสอบเงื่อนไขเมื่อป้อน operator ผิด
        return "Please use one of the following: +, -, *, /, %"

# สร้าง function สำหรับการรับค่าตามที่ user เรียกใช้
def simple_calculator():
    print("Welcome to the Simple Calculator!")
    while True: # loop ไม่รู้รอบ
        number1 = input("Enter your first number (or type 'exit' to quit): ")
        if number1.lower() == 'exit': # ตรวจสอบเงื่อนไขเมื่อเจอคำว่า exit ให้แสดง goodbye program แล้วหยุดการทำงาน
            print("Exiting the program. Goodbye!")
            break
        number2 = input("Enter your second number :")
        oper = input("Enter the operator (+, -, *, /, %): ")
        result = oper_calculat(number1,number2,oper) # เก็บค่าผลลัพธ์
        print("The result of",number1, oper, number2 ,"is", result ) # แสดงผลลัพธ์

simple_calculator()



