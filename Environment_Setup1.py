# Set up a virtual environment, install Pandas, and write a script that reads data from a CSV file.

# สร้างโฟลเดอร์โปรเจ็กต์
# mkdir Environment_Setup1

# เข้าถึงโฟลเดอร์โปรเจ็กต์
# cd Environment_Setup1

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ myenv เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv myenv

# เปิด Virtual Environment >> เห็นว่ามีชื่อ myenv ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source myenv/bin/activate

# สร้างไฟล์ Python ชื่อ read_csv.py >> เพื่ออ่านไฟล์ CSV
# touch read_csv.py # สร้างไฟล์ Python

# ติดตั้ง Pandas
# pip install pandas

# นำโค้ดไปใส่ในไฟล์ read_csv.py
# เขียนโค้ด Python ในไฟล์ read_csv.py
import pandas as pd

# ใส่ที่มาของไฟล์ที่ต้องการให้อ่าน
file_path = '/Users/piinfany/Downloads/departments.csv'

# ใช้ Pandas ในการอ่านไฟล์ CSV โดยใช้คำสั่ง read_csv() และมีการใช้การเข้ารหัสพิเศษ (เช่น UTF-8) หรือใช้ตัวแบ่งที่ไม่ใช่เครื่องหมายจุลภาค (เช่น ; แทน ,)
data = pd.read_csv(file_path, encoding='utf-8', delimiter=';')

# แสดงข้อมูลบางส่วนที่อ่านได้
print(data.head())

# ทดสอบการทำงานโดยรันไฟล์ Python
# cd .. # ออกจากโฟลเดอร์ Environment_Setup1
# python read_csv.py
