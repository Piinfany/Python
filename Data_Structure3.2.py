# Dictionaries and Sets
# Title: Leveraging Dictionaries and Sets
'''
Understand the use cases and best practices for dictionaries and sets in Python. 
By the end of this assignment, you will create a data processing 
application using dictionaries and sets to manage unique and paired data efficiently.
'''
'''
1. Scenario: You are tasked with building a contact management system. Each contact should have:
    - A name and phone number stored in a dictionary.
    - A unique list of contact groups (e.g., 'family', 'work') stored in a set.
2. Requirements:
    - Use a dictionary to store the contact details.
    - Use a set to manage the contact groups.
    - Implement the following functions:
        - add_contact(contact_dict, name, phone):
            - Adds a new contact. Ensure names are unique.
        - remove_contact(contact_dict, name):
            - Removes a contact by name.
        - update_groups(contact_groups, name, group):
            - Adds a contact to a group. Use a set to avoid duplicate groups.
        - remove_group(contact_groups, name, group):
            - Removes a contact from a group.
    - Simulate adding and removing contacts and updating groups.
'''

# สร้าง dictionary เป็นค่าว่างเพื่อเก็บข้อมูลของผู้ติดต่อ
contact_dict = {}

# สร้าง dictionary ชื่อ contact_groups เพื่อเก็บข้อมูลกลุ่ม
contact_groups = {}

# เพิ่ม function add_contact() เพื่อเพิ่มข้อมูลติดต่อใหม่ลงใน contact_dict
def add_contact(contact_dict, name, phone):
    if name in contact_dict: # ถ้ามีชื่ออยู่ใน contact_dict ฟังก์ชันจะแสดงข้อความ
        print("Contact name already exists.")
    else:
        contact_dict[name] = phone # ถ้าไม่มีชื่ออยู่ใน contact_dict จะเพิ่มชื่อและหมายเลขโทรศัพท์

# เพิ่ม Function remove_contact เพื่อลบข้อมูลติดต่อจาก contact_dict
def remove_contact(contact_dict, name):
    if name in contact_dict: # ถ้ามีชื่ออยู่ใน contact_dict ฟังก์ชันจะลบข้อมูลติดต่อออก
        del contact_dict[name]
    else:
        print("Contact not found.") # ถ้าไม่มีชื่ออยู่ใน contact_dict จะแสดงข้อความ

# เพิ่ม Function update_groups เพื่อเพิ่มกลุ่มให้กับผู้ติดต่อใน contact_groups
def update_groups(contact_dict, name, group):
    if name not in contact_dict: # ถ้าไม่มีชื่ออยู่ใน contact_dict จะหยุดการทำงานและแสดงข้อความ
        print("Contact not found.")
        return
    # ถ้ามีชื่ออยู่แล้ว แต่ยังไม่มีการสร้าง contact_groups สำหรับผู้ติดต่อคนนี้ ฟังก์ชันจะสร้าง set() ว่างๆ สำหรับเก็บกลุ่ม
    if name not in contact_groups:
        contact_groups[name] = set()
    contact_groups[name].add(group) # จากนั้นจะเพิ่มกลุ่มที่ระบุไปใน set

# เพิ่ม Function remove_group เพื่อลบกลุ่มออกจากผู้ติดต่อใน contact_groups
def remove_group(contact_dict, name, group): 
    if name not in contact_groups or group not in contact_groups[name]: # ถ้าไม่มีชื่ออยู่ใน contact_groups จะหยุดการทำงานและแสดงข้อความ
        print("Group not found for contact!")
        return
    contact_groups[name].remove(group) # ถ้าผู้ติดต่อและกลุ่มมีอยู่จริง จะลบกลุ่มออกจาก set ของผู้ติดต่อ
    if len(contact_groups[name]) == 0:
        del contact_groups[name] # ถ้าผู้ติดต่อไม่มีกลุ่ม(set ของ group เป็น set ว่าง)จะลบผู้ติดต่อออกจาก contact_groups

# สร้าง Function เพื่อแก้ไขข้อมูล 
def simulate():
    add_contact(contact_dict, "Alice", "123-456-7890") # เพิ่มข้อมูล
    update_groups(contact_dict, "Alice", "family") # เพิ่มกลุ่ม family ให้กับ Alice
    
    add_contact(contact_dict, "Bob", "987-654-3210") # เพิ่มข้อมูล
    update_groups(contact_dict, "Bob", "work") # เพิ่มกลุ่ม work ให้กับ Bob
    
   
    print("Contacts :", contact_dict) # แสดงผลรายชื่อผู้ติดต่อ
    print("Groups :", contact_groups) # แสดงผลรายชื่อกลุ่ม
    
    remove_group(contact_dict, "Alice", "family") # ลบกลุ่ม
    remove_contact(contact_dict, "Alice") # ลบรายชื่อผู้ติดต่อ
    
   
    print("Groups after removal :", contact_groups) # กลุ่มหลังทำการลบ
    print("Contacts after removal :", contact_dict) # รายชื่อผู้ติดต่อหลังทำการลบ


# เรียกใช้ function
simulate()
