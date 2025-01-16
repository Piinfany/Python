# Review and refactor a piece of Python code for readability and suggest improvements.
'''
# This script calculates the factorial of a number

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)

def print_fact(n):
    print("Factorial of", n, "is", fact(n))

number = int(input("Enter a number: "))
print_fact(number)
'''
# This script calculates the factorial of a number

# สร้าง function สำหรับคิด factorial
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1) # เรียกตัวเองซ้ำไปจนกว่าจะถึงฐาน (เมื่อ n ลดลงเหลือ 0 หรือ 1)

# สร้าง function สำหรับการแสดงผลลัพธ์
def display_fac(n):
    print(f"Factorial of {n} is {fact(n)}")

# สร้าง function สำหรับการป้อน
def main():
    while True: # ใช้ while True เพื่อให้โปรแกรมวนลูป
        # การตรวจสอบการป้อนข้อมูลที่ไม่ใช่ตัวเลข
        try:
            number = (input("Enter a number (or 'exit' to quit):")).strip().lower() # ใช้ strip() ช่วยลบช่องว่าง และแปลงเป็นตัวพิมพ์เล็ก
            if number == 'exit':
                print("Goodbye program")
                break # break ใช้เพื่อออกจากลูปเมื่อผู้ใช้พิมพ์ exit
            new_number = int(number)
            # การตรวจสอบค่าติดลบ
            if new_number < 0: # หากผู้ใช้ป้อนเลขติดลบ
                print("Factorial is not defined for negative numbers.")
            else :
                display_fac(new_number)
        except RecursionError: # หากเกิด RecursionError (เช่น ค่า n ใหญ่เกินไป)
            print("Recursion limit reached. Please provide a smaller number.")           
        except ValueError as e: # หากเกิด ValueError (เช่น ผู้ใช้ป้อนข้อมูลที่ไม่ใช่ตัวเลข)
            print(e)
            
            
if __name__ == "__main__":
    main()
    
        


