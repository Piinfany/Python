# Write a script to manage project dependencies and explain the use of a requirements.txt file.

# สร้างไฟล์ requirements.txt ในโฟลเดอร์ Environment_Setup4 >> ใช้เพื่อจัดการ dependencies(เป็นไฟล์ที่เก็บรายชื่อของไลบรารี
# ที่โปรเจกต์ของเราต้องการใช้ รวมถึงเวอร์ชันที่ต้องการ เพื่อให้คนอื่น (หรือแม้กระทั่งตัวเราเอง) สามารถติดตั้งไลบรารีเหล่านี้ได้ในเวอร์ชันที่ถูกต้องเมื่อทำการพัฒนาในอนาคต
""" ทำไมต้องใช้ไฟล์ requirements.txt?
 1. ใช้คำสั่ง pip install -r requirements.txt ระบบจะติดตั้งไลบรารีทั้งหมดที่โปรเจกต์ต้องการโดยอัตโนมัติ และในเวอร์ชันที่ถูกต้อง
 2. แชร์โค้ดให้กับคนอื่น หรือใช้งานในเครื่องที่แตกต่างกัน สามารถมั่นใจได้ว่าโปรเจกต์จะทำงานเหมือนกันในทุกที่ 
    เพราะเวอร์ชันของไลบรารีจะตรงตามที่กำหนดในไฟล์ requirements.txt ทำให้ไม่ต้องกังวลเรื่องเวอร์ชันของไลบรารีที่ต่างกัน """

# สร้างไฟล์ requirements.txt ในโฟลเดอร์ Environment_Setup4
# mkdir Environment_Setup4
# cd Environment_Setup4
# touch requirements.txt

