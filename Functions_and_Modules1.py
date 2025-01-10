# Create a Python function that processes a list of numbers and calculates the sum of all even numbers in the list.

'''
1. Function Definition:
    - Name the function sum_of_evens.
    - The function should take one parameter: a list of integers.
2. Logic:
    - Iterate through the list and identify even numbers.   
    - Sum all the even numbers.
3. Input Validation:
    - Ensure the input is a list.
    - Ensure all elements in the list are integers. If the input is invalid, raise a ValueError with an appropriate message.
4. Return Value:
    - The function should return the sum of all even numbers in the list.
    - Edge Cases to Handle:
    - The input list is empty. (Should return 0.)
    - The list contains no even numbers. (Should return 0.)
    - The list contains negative numbers.
'''


# สร้าง function ชื่อ even_sum และรับพารามิเตอร์ชื่อ numbers
def sum_of_evens(numbers):
    if not isinstance(numbers,list): # ตรวจสอบว่าเป็น list ไหม?
        raise ValueError("Input isn't list.") # ถ้าไม่ใช่จะโยน valueerror พร้อมกับข้อความมา
    if not all (isinstance(i,int) for i in numbers): # ตรวจสอบว่าใน list เป็น int ไหม?
        raise ValueError("All elements in the list isn't integers.") # ถ้าไม่ใช่จะโยน valueerror พร้อมกับข้อความมา
    sum = 0 # ให้ค่าเริ่มต้นเป็น 0 ไว้เก็บค่า
    for i in numbers: # สร้าง loop โดยรับค่าจาก numbers
        if i % 2 == 0: # ถ้า i หาร 2 ลงตัว 
            sum = sum + i # ให้บวกค่า i ไปใน sum
    return sum # ให้ function นี้ส่งค่า sum กลับมา

# การเรียกใช้ function
numbers = [1,2,3,4,5,6,7,8,9,10,-2]
result = sum_of_evens(numbers)
print("sum of all even numbers in", numbers, "is", result)
