# Create a Python function to determine whether a given year is a leap year. A leap year has special rules, and your function should evaluate these rules correctly.

'''
1. Function Requirements:
    - Name your function is_leap_year.
    - The function should accept a single argument, year, which is an integer representing the year to check.
    - The function should return True if the year is a leap year and False otherwise.
2. Leap Year Rules:
    - A year is a leap year if:
        - It is divisible by 4, and
        - It is not divisible by 100, unless it is also divisible by 400.
    - Examples:
        - 2000 is a leap year (divisible by 400).
        - 1900 is not a leap year (divisible by 100 but not by 400).
        - 2024 is a leap year (divisible by 4 and not divisible by 100).
        - 2023 is not a leap year (not divisible by 4).
4. Code Example:
    - The function should work as shown below:
        - print(is_leap_year(2000))  # Output: True
        - print(is_leap_year(1900))  # Output: False
        - print(is_leap_year(2024))  # Output: True
        - print(is_leap_year(2023))  # Output: False
'''

# สร้าง function ตรวจสอบปีอธิกสุรทิน รับ parameters เป็น years
def is_leap_year(years):
    if years % 4 == 0: # ตรวจสอบว่า years หารด้วย 4 ลงตัวไหม?
        if years % 100 == 0: # ตรวจสอบว่า years หารด้วย 100,400 ลงตัวไหม? ซึ่งถ้าหาร 100 ลงตัวอย่างเดียวก็จะเป็น False
            if years % 400 == 0: # ตรวจสอบว่า years หารด้วย 400 ลงตัวไหม?
                return True
            else : # ถ้าหาร 400 ไม่ลงตัวจะส่งค่ากลับเป็น False
                return False
        else : # ถ้าไม่หารด้วย 100 หรือ หาร 100 ไม่ลงตัวจะเป็น True
           return True 
    else : # ถ้าหาร 4 ไม่ลงตัวจะส่งค่ากลับเป็น False
        return False
    
print(is_leap_year(2000))
print(is_leap_year(1900))
print(is_leap_year(2024))
print(is_leap_year(2023))