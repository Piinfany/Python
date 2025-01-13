# Exploring Dictionaries and Sets
# Learn how dictionaries and sets are used and their unique features.
'''
1. Create a dictionary with student names as keys and grades as values.
2. Perform operations:
    - Add students: {"Alice": 90, "Bob": 85, "Charlie": 88}
    - Update Charlie’s grade to 92.
    - Remove Bob.
    - Retrieve Alice’s grade.
3. Create a set of programming languages: {"Python", "Java", "C++"}. 
    Perform operations:
    - Add C# and Go.
    - Check if Python exists in the set.
    - Find intersection and union with {"Python", "JavaScript", "Ruby"}.
'''

# สร้าง dictionary
student = {"Alice": 90, "Bob": 85, "Charlie": 88}
print("Original Dictionary : ", student)

# แก้ไขคะแนนของ Charlie
student["Charlie"] = 92
print("Updated Dictionary : ", student)

# ลบ Bob ออกไป
del student["Bob"]
print("หลัง Remove Bob. : ", student)

# นำคะแนนของ alice มาเก็บไว้ในตัวแปร alice 
alice = student["Alice"]
print("Alice's Grade :", alice)

# สร้าง set
programming_languages = {"Python", "Java", "C++"}
print("Original Set : ", programming_languages)

# เพิ่มข้อมูลลงใน set
programming_languages.add("C#")
programming_languages.add("Go")
print("Set after adding : ", programming_languages)

# ตรวจสอบว่า Python อยู่ใน set ไหม?
is_python = "Python" in programming_languages
print("Does Python exist? :", is_python)

# สร้าง set เพิ่ม เพื่อดูว่า intersection(ใน set มีสมาชิกที่เหมือนกันไหม?)
set_programming = {"Python", "JavaScript", "Ruby"}
intersection = programming_languages.intersection(set_programming)
print("Intersection :",intersection)

# นำสมาชิกใน set มา Union(เอาสมาชิกใน set ทุกตัว)
union = programming_languages.union(set_programming)
print("Union :",union)

