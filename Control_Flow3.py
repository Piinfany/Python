#FizzBuzz Program
'''
Write a Python program that iterates through the numbers 1 to 100 and 
applies specific rules to determine what to print for each number. 
This exercise will help you practice working with loops, conditionals, and basic arithmetic operators.
'''
# ใช้ function range เพื่อจัดลำดับของตัวเลข
# ใช้ loop for เพราะรู้จำนวนรอบที่จะให้ทำ โดยในข้อนี้ ให้เริ่มที่ index[1] จำนวน 101 รอบ >> 1-100
for fizzbuzz in range(1,101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz)


#Additional Challenge
# เพิ่มการใช้ input
number1 = int(input("Enter your number1 : "))
number2 = int(input("Enter your number2 : "))
# validate number1 และ number2
# validate อะไรบ้าง ลอง research ดู
for fizzbuzz in range(number1,number2+1):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz)
