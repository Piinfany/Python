# Create a Python function that processes a list of numbers and calculates the sum of all even numbers in the list.

# สร้าง function ชื่อ even_sum และรับพารามิเตอร์ชื่อ numbers
def even_sum(numbers):
    sum = 0 # ให้ค่าเริ่มต้นเป็น 0 ไว้เก็บค่า
    for i in numbers: # สร้าง loop โดยรับค่าจาก numbers
        if i % 2 == 0: # ถ้า i หาร 2 ลงตัว 
            sum = sum + i # ให้บวกค่า i ไปใน sum
    return sum # ให้ function นี้ส่งค่า sum กลับมา

# การเรียกใช้ function
numbers = [1,2,3,4,5,6,7,8,9,10] 
result = even_sum(numbers)
print("sum of all even numbers in", numbers, "is", result)
