'''
Objective:
The purpose of this assignment is to evaluate your ability to interact with public APIs, process data programmatically, and derive insights. By completing this task, you will demonstrate your skills in data fetching, Python programming, and JSON handling.

Assignment Tasks:
    1. Fetch Data from a Public API
        - Use the Universities List API (endpoint: http://universities.hipolabs.com/search?name=university) to fetch a list of universities based on a search term.
        - No sign-up or API key is required for this endpoint.
    2. Process the Data
        - Extract relevant fields such as the university name, country, and web page link.
        - Format the extracted information into a structured format for easy readability.
    3. Generate Insights
        - Provide basic insights from the fetched data. For example:
            - Count the number of universities in each country.
            - Identify the countries with the highest and lowest number of universities.
    4. Save Insights to a JSON File
        - Save the processed data and insights into a JSON file named university_insights.json.

Submission Requirements:
    - Submit the Python script (.py file) used to complete the assignment.
    - Include the generated university_insights.json file in your submission.

Evaluation Criteria:
    1. Code Quality (40%)
        - Proper variable naming.
        - Clear comments explaining the logic.
        - Clean and readable code structure.
    2. Correctness (30%)
        - Correctly fetching data from the API.
        - Accurate processing and extraction of relevant fields.
    3. Insightful Analysis (20%)
        - Deriving meaningful insights from the data.
        - Presenting insights in a structured format.
    4. File Handling and Output (10%)
        - Proper creation and formatting of the university_insights.json file.

Guidelines for Bonus Points:
    - Advanced Insights: Generate additional insights such as the most common words in university names.
    - Error Handling: Implement error handling for cases such as API connectivity issues.
    - Interactive Input: Allow the user to specify a search term dynamically to fetch university data.
    - Enhanced Output: Beautify the JSON output for readability (e.g., proper indentation).

Deliverable Structure:
    - university_script.py: The Python script for fetching and processing data.
    - university_insights.json: The JSON file containing the processed data and insights.
'''
# นำเข้า library requests >> เป็นไลบรารีที่ใช้สำหรับการเชื่อมต่อและส่งคำขอไปยังเว็บไซต์หรือ API
import requests

# นำเข้า library json >> เป็นไลบรารีที่ช่วยในการจัดการข้อมูลแบบ JSON
import json

# นำเข้า library collections >> เป็นไลบรารีที่ช่วยในการจัดการข้อมูลแบบ Collection ใช้สำหรับนับความถี่ของข้อมูล 
from collections import Counter

# นำเข้า library pprint >> เป็นไลบรารีที่ช่วยในการแสดงผลข้อมูลออกทางหน้าจอ ใช้สำหรับการแสดงผลข้อมูลในรูปแบบที่อ่านง่าย
from pprint import pprint

# สร้าง function fetch_univer_data โดยมี parameter search_name ใช้สำหรับค้นหาข้อมูลจาก API โดยใช้ชื่อมหาวิทยาลัยเป็นเงื่อนไข
def fetch_univer_data(search_name):
    try: # ใช้ try เพื่อจัดการข้อผิดพลาดที่อาจเกิดขึ้น
        url = f"http://universities.hipolabs.com/search?name={search_name}" # กำหนด url ของ API ที่ต้องการใช้งาน
        request = requests.get(url) # สร้างตัวแปร request โดยใช้ requests.get() สำหรับการเชื่อมต่อ API
        request.raise_for_status() # ใช้ raise_for_status() เพื่อจัดการข้อผิดพลาดที่อาจเกิดขึ้น หากมีข้อผิดพลาดจะทำการ raise ข้อผิดพลาดนั้นออกมา
        return request.json() # คืนค่าข้อมูลที่ได้จาก API ในรูปแบบ JSON กลับไป
    except requests.exceptions.HTTPError as err: # จัดการข้อผิดพลาดที่เกิดขึ้นเมื่อมีข้อผิดพลาดในการเชื่อมต่อ API 
        print(err)
        return None # คืนค่า None หากเกิดข้อผิดพลาด 
    except requests.exceptions.RequestException as e: # จัดการข้อผิดพลาดที่เกิดขึ้นเมื่อมีข้อผิดพลาดในการส่งคำขอไปยังเว็บไซต์หรือ API
        print(e)
        return None # คืนค่า None หากเกิดข้อผิดพลาด

# สร้าง function process_univer_data โดยมี parameter data ใช้เพื่อทำการแปรรูปข้อมูลที่ได้จาก API ให้อยู่ในรูปแบบที่ต้องการ
def process_univer_data(data):
    univer = [] # สร้าง list ว่าง ชื่อ univer เพื่อเก็บข้อมูลที่ได้จาก API
    for item in data: # วนลูปเพื่อดึงข้อมูลที่ต้องการจาก data ที่ได้จาก API
        name = item.get('name', 'N/A') # ดึงชื่อมหาวิทยาลัย ถ้าไม่พบก็ใช้ "N/A" เป็นค่าเริ่มต้น.
        country = item.get('country', 'N/A') # ดึงชื่อประเทศ ถ้าไม่พบก็ใช้ "N/A" เป็นค่าเริ่มต้น.
        web_page = item.get('web_pages', ['N/A'])[0] # ดึงเว็บไซต์ ถ้าไม่พบก็ใช้ "N/A" เป็นค่าเริ่มต้น.
        univer.append({'name': name, 'country': country, 'web_page': web_page}) # เพิ่มข้อมูลที่ดึงมาจาก API ลงใน list univer
    return univer # คืนค่า list ที่เก็บข้อมูลที่ดึงมาจาก API ส่งคืนลิสต์ของมหาวิทยาลัย

# สร้าง function generate_insights โดยมี parameter data ใช้เพื่อคำนวณข้อมูลเชิงลึกจากข้อมูลของมหาวิทยาลัย จาก API
def gen_insign(univer):
    count_country = Counter([item['country'] for item in univer]) # นับจำนวนมหาวิทยาลัยในแต่ละประเทศ
    most_univer = count_country.most_common(1) # หาประเทศที่มีมหาวิทยาลัยมากที่สุด
    least_univer = count_country.most_common()[-1] # หาประเทศที่มีมหาวิทยาลัยน้อยที่สุด
    return {'Total Universities' : len(univer) ,'Count Country': dict(count_country), 'Most Universities': most_univer, 'Least Universities': least_univer} # คืนค่าข้อมูลที่คำนวณได้

# สร้าง function save_to_json โดยมี parameter data ใช้เพื่อบันทึกข้อมูลที่ได้จาก API ลงในไฟล์ JSON
def save_to_json(filename,data):
    with open(filename, 'w',encoding='utf-8') as file: # สร้างไฟล์ JSON ชื่อ university_insights.json โดยใช้โหมด w สำหรับการเขียนไฟล์ และใช้ utf-8 สำหรับการเขียนภาษาไทย
        json.dump(data, file, indent=4) # บันทึกข้อมูลที่ได้จาก API ลงในไฟล์ JSON โดยใช้ indent=4 สำหรับการจัดรูปแบบข้อมูลให้สวยงาม

# สร้าง function main ที่ใช้เรียกใช้งาน function ทั้งหมด
def main():
    search_name = 'university' # กำหนดคำค้นหาเป็น university
    data = fetch_univer_data(search_name) # เรียกใช้ function fetch_univer_data โดยใช้คำค้นหาเป็นพารามิเตอร์
    if data: # ถ้ามีข้อมูลจาก API
        univer = process_univer_data(data) # เรียกใช้ function process_univer_data โดยใช้ข้อมูลที่ได้จาก API ในพารามิเตอร์
        insights = gen_insign(univer) # เรียกใช้ function gen_insign โดยใช้ข้อมูลที่ได้จาก API ในพารามิเตอร์
        save_to_json('university_insights.json', insights) # เรียกใช้ function save_to_json โดยใช้ข้อมูลที่ได้จาก API ในพารามิเตอร์
        pprint(insights) # แสดงผลข้อมูลที่ได้จาก API ในรูปแบบที่อ่านง่าย
    else: # ถ้าไม่มีข้อมูลจาก API
        print("No data fetched!") # แสดงข้อความว่าไม่มีข้อมูลที่ได้จาก API

# เรียกใช้ function main เพื่อรันโปรแกรม
if __name__ == "__main__": # ตรวจสอบว่าไฟล์ถูกเรียกใช้โดยตรงหรือไม่
    main() # เรียกใช้ function main เพื่อรันโปรแกรม
