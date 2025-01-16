# Review and refactor a piece of Python code for readability and suggest improvements.
'''
# This script calculates student grades

students = ["Alice", "Bob", "Charlie"]
grades = [[85, 90, 78], [92, 88, 84], [70, 75, 80]]

def get_avg(grades):
    total = 0
    for grade in grades:
        total += grade
    return total/len(grades)

def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

for i in range(len(students)):
    avg = get_avg(grades[i])
    letter = get_letter_grade(avg)
    print(students[i] + "'s average grade is " + str(avg) + " and the letter grade is " + letter)
'''
# This script calculates student grades

students = ["Alice", "Bob", "Charlie"]
grades = [[85, 90, 78], [92, 88, 84], [70, 75, 80]]

def get_avg(grades):
    return sum(grade for grade in grades) / len(grades)

def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
# สร้าง loop โดย student >> เก็บชื่อของนักเรียน และ student_grades >> เก็บเกรดของนักเรียน
for student,student_grade in zip(students,grades): # ใช้ zip เพื่อจับคู่เข้าด้วยกันจาก 2 รายการ
    avg_grade = get_avg(student_grade) # get_avg() จะคำนวณค่าเฉลี่ยจากเกรดทั้งหมดในรายการ student_grades
    letter_grade = get_letter_grade(avg_grade) # get_letter_grade() จะแปลงค่าเฉลี่ยเป็นเกรดตามตัวอักษร
    print(f"\n{student}'s average grade is {avg_grade:.2f} and the letter grade is {letter_grade}\n")