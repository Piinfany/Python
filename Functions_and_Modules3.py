# Create a Python function that reverses a given string. You will then test this function with multiple inputs to ensure it works correctly.

'''
1. Function Requirements:
    - Name your function reverse_string.
    - The function should accept a single argument, input_string, which is a string.
    - The function should return the reversed version of input_string.
2. Example Behavior:
    - For a string "hello", the reversed string should be "olleh".
    - For an empty string "", the reversed string should also be "".
    - For a string "12345", the reversed string should be "54321".
3. Code Example:
    - The function should behave as follows:
        - print(reverse_string("hello"))  # Output: "olleh"
        - print(reverse_string(""))       # Output: ""
        - print(reverse_string("12345"))  # Output: "54321"
'''

# สร้าง function การกลับตัวอักษร โดยรับ parameters คือ st
def reverse_string(st):
    if not isinstance(st,str): # ตรวจสอบว่าเป็น str ไหม 
        raise ValueError("Input isn't string!!!.") # ถ้าไม่ใช่จะโยน valueerror พร้อมกับข้อความมา
    return st[::-1] # ให้ย้อนกลับลำดับของคำ

# เรียกใช้งาน function
word = str(input("Enter any word : "))
print(reverse_string(word))
    
