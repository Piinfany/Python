#  Set up a virtual environment and install libraries like NumPy and requests, then write a script to use them.

# สร้างโฟลเดอร์โปรเจ็กต์
# mkdir Environment_Setup1

# เข้าถึงโฟลเดอร์โปรเจ็กต์
# Environment_Setup1

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ myenv เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv myenv

# เปิด Virtual Environment >> เห็นว่ามีชื่อ myenv ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source myenv/bin/activate

# ติดตั้ง NumPy และ requests
# pip install numpy requests

# สร้างไฟล์ Python ชื่อ use_libraries.py >> เพื่อใช้งาน NumPy และ requests
# touch use_libraries.py # สร้างไฟล์ Python

# เขียนโค้ด Python ในไฟล์ use_libraries.py
import numpy as np
import requests

url_data = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1" # ส่งคำขอไปยัง API ของ CoinGecko.
data = requests.get(url_data).json() # ส่งคำขอ GET ไปยัง API และเก็บข้อมูลที่ได้ในรูปแบบของ JSON

price = [coin['current_price'] for coin in data] # ดึงราคาปัจจุบันของเหรียญทั้งหมดจาก data และเก็บไว้ใน price

np_price = np.array(price) # แปลง list ของราคาเหรียญเป็น NumPy array

# คำนวณค่าสถิติเบื้องต้นก่อน
mean_price = np.mean(np_price) # คำนวณค่าเฉลี่ยของราคาเหรียญ
max_price = np.max(np_price) # คำนวณค่าสูงสุดของราคาเหรียญ
min_price = np.min(np_price) # คำนวณค่าต่ำสุดของราคาเหรียญ
std_price = np.std(np_price) # คำนวณค่าเบี่ยงเบนมาตรฐาน

# Output
print(f"ราคาของเหรียญ 5 อันดับแรก :")
for i in range(5):
    print(f"{data[i]['name']} : {data[i]['current_price']} USD")

print(f"\nค่าสถิติเบื้องต้นของราคาเหรียญ :")
print(f"ค่าเฉลี่ย : {mean_price:.2f} USD")
print(f"ค่าสูงสุด : {max_price:.2f} USD")
print(f"ค่าต่ำสุด : {min_price:.2f} USD")
print(f"ค่าเบี่ยงเบนมาตรฐาน : {std_price:.2f} USD")

# pip install requests numpy

# ทดสอบการทำงานโดยรันไฟล์ Python
# รันโค้ด Python ในไฟล์ use_libraries.py
# python use_libraries.py






