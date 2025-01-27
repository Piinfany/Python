# Write a script to manage project dependencies and explain the use of a requirements.txt file.
"""
ไฟล์ requirements.txt คือไฟล์ข้อความธรรมดาที่บันทึกรายชื่อไลบรารีที่โปรเจกต์ต้องการ รวมถึงเวอร์ชันที่ต้องการ
"""
# สร้างไฟล์ requirements.txt ในโฟลเดอร์ Environment_Setup4 >> ใช้เพื่อจัดการ dependencies(เป็นไฟล์ที่เก็บรายชื่อของไลบรารี
# ที่โปรเจกต์ของเราต้องการใช้ รวมถึงเวอร์ชันที่ต้องการ เพื่อให้คนอื่น (หรือแม้กระทั่งตัวเราเอง) สามารถติดตั้งไลบรารีเหล่านี้ได้ในเวอร์ชันที่ถูกต้องเมื่อทำการพัฒนาในอนาคต
""" ทำไมต้องใช้ไฟล์ requirements.txt?
 1. ใช้คำสั่ง pip install -r requirements.txt ระบบจะติดตั้งไลบรารีทั้งหมดที่โปรเจกต์ต้องการโดยอัตโนมัติ และในเวอร์ชันที่ถูกต้อง
 2. แชร์โค้ดให้กับคนอื่น หรือใช้งานในเครื่องที่แตกต่างกัน สามารถมั่นใจได้ว่าโปรเจกต์จะทำงานเหมือนกันในทุกที่ 
    เพราะเวอร์ชันของไลบรารีจะตรงตามที่กำหนดในไฟล์ requirements.txt ทำให้ไม่ต้องกังวลเรื่องเวอร์ชันของไลบรารีที่ต่างกัน """

# สร้างไฟล์ requirements.txt ในโฟลเดอร์ Environment_Setup4

# สร้างโฟลเดอร์ Environment_Setup4
# mkdir Environment_Setup4

# เข้าถึงโฟลเดอร์ Environment_Setup4
# cd Environment_Setup4

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ myenv เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv myenv

# เปิด Virtual Environment >> เห็นว่ามีชื่อ myenv ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source myenv/bin/activate

# สร้างไฟล์ Python ชื่อ Environment_Setup4.py >> เพื่อจัดการ dependencies
# touch Environment_Setup4.py

# ติดตั้ง dependencies
# pip install -r requirements.txt


# นำ โค้ดไปใส่ใน Environment_Setup4.py
# นำเข้า subprocess >> ใช้สำหรับเรียกใช้คำสั่งในระบบปฏิบัติการ และรับผลลัพธ์จากคำสั่งนั้น
import subprocess

# นำเข้า sys >> ใช้สำหรับเข้าถึงค่าที่เกี่ยวข้องกับ Python และระบบปฏิบัติการ เช่น ค่าที่ส่งเข้ามาผ่าน command line
import sys

# นำเข้า os >> ใช้สำหรับการทำงานกับระบบปฏิบัติการ เช่น สร้างโฟลเดอร์ ลบไฟล์ หรือเปลี่ยน directory
import os

# สร้างฟังก์ชัน install_requirements >> ติดตั้ง dependencies จากไฟล์ requirements.txt
def install_requirements(): # สร้างฟังก์ชัน install_requirements โดยไม่มี parameter
    if os.path.exists('requirements.txt'): # ถ้ามีไฟล์ requirements.txt อยู่ ให้ทำการติดตั้ง dependencies จากไฟล์ requirements.txt
        print("กำลังติดตั้ง dependencies จาก requirements.txt...") # แสดงข้อความว่ากำลังติดตั้ง dependencies จาก requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]) # ใช้ subprocess.check_call เพื่อเรียกใช้คำสั่ง pip install -r requirements.txt
    else: # ถ้าไม่มีไฟล์ requirements.txt อยู่ ให้แสดงข้อความว่าไม่พบไฟล์ requirements.txt กรุณาตรวจสอบไฟล์ให้แน่ใจว่ามีอยู่
        print("ไม่พบไฟล์ requirements.txt กรุณาตรวจสอบไฟล์ให้แน่ใจว่ามีอยู่")

# สร้างฟังก์ชัน generate_requirements >> สร้างไฟล์ requirements.txt จาก environment ปัจจุบัน
def generate_requirements(): # สร้างฟังก์ชัน generate_requirements โดยไม่มี parameter
    print("กำลังสร้างไฟล์ requirements.txt...")
    with open('requirements.txt', 'w') as f: # ใช้ open เพื่อสร้างไฟล์ requirements.txt ในโหมดเขียน (w) และเก็บไว้ในตัวแปร f
        subprocess.check_call([sys.executable, "-m", "pip", "freeze"], stdout=f) # ใช้ subprocess.check_call เพื่อเรียกใช้คำสั่ง pip freeze ซึ่งคือ แสดงรายชื่อของไลบรารีที่ติดตั้งและเวอร์ชันที่ติดตั้ง และเก็บไว้ในไฟล์ requirements.txt
    print("ไฟล์ requirements.txt ถูกสร้างเรียบร้อยแล้ว")

# สร้างฟังก์ชัน update_requirements >> อัพเดตไฟล์ requirements.txt เมื่อ dependencies เปลี่ยนแปลง
def update_requirements(): # สร้างฟังก์ชัน update_requirements โดยไม่มี parameter
    print("กำลังอัพเดตไฟล์ requirements.txt...")
    generate_requirements() # เรียกใช้ฟังก์ชัน generate_requirements เพื่อสร้างไฟล์ requirements.txt ใหม่

# สร้างฟังก์ชัน install_package >> ติดตั้งไลบรารีที่ระบุ
def install_package(package): # สร้างฟังก์ชัน install_package โดยมี parameter package
    print(f"กำลังติดตั้ง {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package]) # ใช้ subprocess.check_call เพื่อเรียกใช้คำสั่ง pip install และติดตั้งไลบรารีที่ระบุ
    update_requirements() # เรียกใช้ฟังก์ชัน update_requirements เพื่ออัพเดตไฟล์ requirements.txt

# สร้างฟังก์ชัน uninstall_package >> ลบไลบรารีที่ระบุ
def uninstall_package(package): # สร้างฟังก์ชัน uninstall_package โดยมี parameter package
    print(f"กำลังลบ {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package]) # ใช้ subprocess.check_call เพื่อเรียกใช้คำสั่ง pip uninstall และลบไลบรารีที่ระบุ
    update_requirements() # เรียกใช้ฟังก์ชัน update_requirements เพื่ออัพเดตไฟล์ requirements.txt

# สร้างฟังก์ชัน exit_program >> ออกจากโปรแกรม       
def exit_program():
    print("ออกจากโปรแกรม")
    sys.exit() # ออกจากโปรแกรม

# สร้างฟังก์ชัน main >> ฟังก์ชันหลักเพื่อให้ผู้ใช้สามารถเลือกการดำเนินการต่าง ๆ
def main(): # สร้างฟังก์ชัน main โดยไม่มี parameter
    print("สคริปต์จัดการ dependencies ของโปรเจกต์")
    # สร้างเมนูเลือกต่าง ๆ ที่ผู้ใช้สามารถเลือก
    menu_options = { 
        "1": install_requirements,
        "2": generate_requirements,
        "3": install_package,
        "4": uninstall_package,
        "5": exit_program,
    }

    while True: # วนลูปเพื่อให้ผู้ใช้สามารถเลือกตัวเลือกที่ต้องการ
        print("\nเลือกตัวเลือกที่ต้องการ:")
        print("1. ติดตั้ง dependencies จากไฟล์ requirements.txt")
        print("2. สร้างไฟล์ requirements.txt จาก environment ปัจจุบัน")
        print("3. ติดตั้งไลบรารีที่ต้องการ")
        print("4. ลบไลบรารีที่ไม่ต้องการ")
        print("5. ออกจากโปรแกรม")

        choice = input("กรุณากรอกหมายเลขที่ต้องการ: ").strip() # รับค่าจากผู้ใช้เพื่อเลือกตัวเลือกที่ต้องการ และใช้ strip() เพื่อลบช่องว่างที่อาจจะมีอยู่
        action = menu_options.get(choice) # ใช้ get เพื่อเลือกฟังก์ชันที่ต้องการจากเมนูตัวเลือก

        if action: # ถ้ามี action ให้ทำการดำเนินการตามที่ผู้ใช้เลือก
            if choice == "3" or choice == "4": # ถ้าผู้ใช้เลือกตัวเลือกที่ต้องการติดตั้งหรือลบไลบรารี
                package = input("กรุณากรอกชื่อไลบรารีที่ต้องการ: ").strip() # รับชื่อไลบรารีที่ต้องการจากผู้ใช้ และใช้ strip() เพื่อลบช่องว่างที่อาจจะมีอยู่
                action(package) # เรียกใช้ฟังก์ชันที่ผู้ใช้เลือกพร้อมส่งชื่อไลบรารีที่ต้องการ
            else: # ถ้าผู้ใช้เลือกตัวเลือกที่ไม่ใช่ติดตั้งหรือลบไลบรารี
                action() # เรียกใช้ฟังก์ชันที่ผู้ใช้เลือก
        else: # ถ้าไม่มี action ให้แสดงข้อความว่าตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")


# เรียกใช้ฟังก์ชัน main เพื่อเริ่มการทำงานของโปรแกรม
if __name__ == "__main__": # ใช้เพื่อตรวจสอบว่าโค้ดถูกเรียกใช้โดยตรงหรือไม่
    main() # เรียกใช้ฟังก์ชัน main เพื่อเริ่มการทำงานของโปรแกรม

# ทดสอบการทำงานโดยรันไฟล์ Python
# cd .. >> ออกจากโฟลเดอร์ Environment_Setup4
# python Environment_Setup4.py

# ปิด Virtual Environment
# deactivate
