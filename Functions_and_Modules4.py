#Write a Python function to filter names that start with a vowel. The function will accept a list of names and return a new list containing only the names that start with a vowel. Additionally, apply advanced processing to ensure the solution is efficient, flexible, and robust.
# ฟังก์ชันยอมรับรายชื่อและส่งคืนรายการใหม่ที่มีเฉพาะชื่อที่ขึ้นต้นด้วยสระเท่านั้น
# สร้าง function โดยมี parameters คือ
# name >> list
# ignore_case >> ไม่สนใจตัวพิมพ์ใหญ่พิมพ์เล็กไม่สนใจตัวพิมพ์ใหญ่พิมพ์เล็ก ค่าเริ่มต้นเป็น True (ไม่สนใจ)
# vowel >> เป็น str มีตัวอักษร 5 ตัว คือ a,e,i,o,u

def filter_vowel_names_advanced(names: list, ignore_case: bool = True, vowel: str = "aeiou") -> list:
    if ignore_case: # ถ้า ignore_case เป็น True จะแปลงค่า vowels เป็นตัวพิมพ์เล็กให้หมด
        vowel = vowel.lower() # **สร้างตัวแปรใหม่
    result = [name.strip() for name in names # ใช้ strip เพื่อลบช่องว่างซ้ายขวาของ name
                  # ตรวจสอบว่า name เป็น str หรือไม่
                  # จากนั้นก็ strip เพื่อลบช่องว่างซ้ายขวาอีกครั้ง
                  # แปลงเป็นตัวพิมพ์เล็ก แล้วตรวจสอบว่าอยู่ใน vowel >>  a,e,i,o,u ไหม
                  if isinstance(name,str) and name.strip() and name.strip()[0].lower() in vowel] 
    return result
    
input_names = ["Alice", "Bob", "Oscar", "Uma", "Ian"]
result = filter_vowel_names_advanced(input_names)
print(result)

input_names = ["Alice", "Oscar", "Uma", "ian"]
result = filter_vowel_names_advanced(input_names, ignore_case=False, vowel="io")
print(result)

input_names = [" Bob", "Uma ", "alice", 123, None]
result = filter_vowel_names_advanced(input_names)
print(result)
