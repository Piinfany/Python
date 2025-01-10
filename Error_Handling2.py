# Add error handling to a script that divides two numbers entered by the user, ensuring division by zero is handled.

# สร้าง function 
def divide_number():
    try: # พยายามรับค่าที่แปลงเป็น float 
        number1 = float(input("Enter first number : "))
        number2 = float(input("Enter second number : "))
        result = number1 / number2
    except ZeroDivisionError: # ถ้าป้อนตัวหารเป็น 0 จะแสดง error พร้อมกับข้อความ
        print("ไม่สามารถใช้ตัวหารเป็นศูนย์ได้")
    except ValueError: # ถ้าป้อนอะไรที่ไม่ใช่ตัวเลขจะแสดง error พร้อมกับข้อความ
        print("Please enter numeric ")
    else : # ถ้าไม่มีข้อผิดพลาดเกิดขึ้น (ทั้งจากการหารและการป้อนข้อมูล) จะแสดง result
        print("The result of ", number1, "/", number2,"is", result)

divide_number()