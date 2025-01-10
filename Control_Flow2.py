#Vowel Counting Program
#Create a Python program that counts the number of vowels in a given string and outputs the result. The program should handle both uppercase and lowercase letters and consider only the English vowels: a, e, i, o, u.
#Example Runs:
#Input: Hello World Output: The total number of vowels in the string is: 3
#Input: Python Output: The total number of vowels in the string is: 1
#Input: (empty string) Output: The input string is empty. No vowels found.

# รับค่า wording แล้วแปลงให้เป็นตัวพิมพ์เล็ก
st = input("Enter any word : ").lower()
# สร้างตัวแปร c ไว้เก็บค่าที่นับ str
c = 0
# เช็คว่าเป็น str ว่าง ไหม?
if not st:
    print("The input string is empty.")
# ถ้าไม่ใช่ str ว่างให้ใช้ loop for เพื่อเช็ค str ทีละตัว
else :
    for x in st:
        if x in 'aeiou': # เช็คว่า st แต่ละตัวมีค่าเป็น a,e,i,o,u ไหม 
            c = c + 1 # ถ้ามีให้ +1 จากที่เป็น 0 แล้วเก็บค่าแทนที่ไว้ที่ c

    if c > 0 : # ถ้า c > 0 ให้แสดงค่า c 
        print("The total number of vowels in the string is : ", c)
    else:
        print("The input string is empty. No vowels found.")


