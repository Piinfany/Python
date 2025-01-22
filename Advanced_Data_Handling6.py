"""
Assignment Title
Develop a Script to Consolidate Data from Multiple File Formats

Objective
The goal of this assignment is to create a Python script that can read data from CSV, Excel, and JSON files, and consolidate the data into a single output. This output should be a combined CSV file.

Key Deliverables
    1. Python Script: A functional Python script that performs the required tasks.
    2. Output File: A single consolidated CSV file combining data from all input files.

Expected Features
    - Input File Handling:
        - Accept multiple input file paths (CSV, Excel, and JSON) via command-line arguments or a configuration file.
        - Use Python libraries like pandas for data processing.
    - Error Handling:
        - Handle missing files, unsupported formats, or incorrect file paths gracefully.
        - Log errors for debugging purposes.
    - Output Format:
        - The final output should be saved as consolidated_output.csv.

Steps to Complete
    1. Environment Setup:
        - Ensure Python is installed (version 3.7+ recommended).
            Install required libraries: pandas and openpyxl (for Excel file support).
            pip install pandas openpyxl


    2. Script Requirements:
        - Read CSV Files: Use pandas.read_csv() to load CSV data.
        - Read Excel Files: Use pandas.read_excel() to load Excel data.
        - Read JSON Files: Use pandas.read_json() to load JSON data.
        - Combine Data: Use pandas.concat() to merge data into a single DataFrame.
    3. Ensure Column Alignment:
        - Standardize column names across files before merging.
    4. Save Output:
        - Save the combined DataFrame to a CSV file using to_csv().

Additional Guidance
    - Use functions to modularize your script (e.g., separate functions for reading each file type).
    - Add comments to explain your code.
Example Input Files
CSV File (data1.csv):
ID,Name,Age
1,Alice,25
2,Bob,30

Excel File (data2.xlsx):
ID
Name
Age
3
Charlie
35
4
Diana
40



JSON File (data3.json):

[
    {"ID": 5, "Name": "Eve", "Age": 45},
    {"ID": 6, "Name": "Frank", "Age": 50}
]



Expected Output
Consolidated CSV (consolidated_output.csv):

ID,Name,Age
1,Alice,25
2,Bob,30
3,Charlie,35
4,Diana,40
5,Eve,45
6,Frank,50


Evaluation Criteria
    - Script functionality and correctness.
    - Code readability and maintainability.
    - Proper error handling.
    - Successful generation of the consolidated output file.
"""
# นำเข้า library os >> เป็นไลบรารีที่ใช้ในการจัดการไฟล์และโฟลเดอร์ เช่น การตรวจสอบว่าไฟล์นั้นมีอยู่จริงหรือไม่
import os

# นำเข้า library pandas >> เป็นไลบรารีที่ใช้สำหรับการจัดการข้อมูลในรูปแบบ DataFrame ซึ่งเป็นโครงสร้างข้อมูลหลักที่ใช้ในโปรแกรมนี้
import pandas as pd

# นำเข้า library logging >> เป็นไลบรารีที่ใช้สำหรับบันทึกข้อความต่างๆ ในการทำงานของโปรแกรม เช่น การแจ้งเตือนหรือข้อผิดพลาด
import logging

# นำเข้า library sys >> ใช้สำหรับการจัดการกับ arguments ที่ถูกส่งจาก command-line
import sys

# กำหนดรูปแบบของ log โดยกำหนดรูปแบบของข้อความที่จะแสดงออกมา โดยระบุวันเวลา ระดับของข้อความ และข้อความที่ต้องการแสดง
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# สร้างตัวแปร logger สำหรับใช้บันทึกข้อความต่างๆ ภายในโปรแกรม
logger = logging.getLogger()

# สร้าง function read_csv_file โดยมี parameter file_path ใช้สำหรับอ่านไฟล์ CSV
def read_csv(file_path):
    try:
        data = pd.read_csv(file_path) # ใช้ pd.read_csv() ในการอ่านไฟล์ CSV
        logger.info(f"Read CSV file: {file_path}") # บันทึกข้อความว่าอ่านไฟล์ CSV สำเร็จ
        return data # คืนค่าข้อมูลที่ได้จากการอ่านไฟล์ CSV
    except Exception as e: # จัดการข้อผิดพลาดที่เกิดขึ้น
        logger.error(f"Error reading CSV file: {file_path}") # บันทึกข้อความว่าเกิดข้อผิดพลาดในการอ่านไฟล์ CSV
        return None # คืนค่า None หากเกิดข้อผิดพลาด

# สร้าง function read_excel_file โดยมี parameter file_path ใช้สำหรับอ่านไฟล์ Excel
def read_excel(file_path):
    try:
        data = pd.read_excel(file_path) # ใช้ pd.read_excel() ในการอ่านไฟล์ Excel
        logger.info(f"Read Excel file: {file_path}") # บันทึกข้อความว่าอ่านไฟล์ Excel สำเร็จ
        return data # คืนค่าข้อมูลที่ได้จากการอ่านไฟล์ Excel
    except Exception as e: # จัดการข้อผิดพลาดที่เกิดขึ้น
        logger.error(f"Error reading Excel file: {file_path}") # บันทึกข้อความว่าเกิดข้อผิดพลาดในการอ่านไฟล์ Excel
        return None
    
# สร้าง function read_json_file โดยมี parameter file_path ใช้สำหรับอ่านไฟล์ JSON
def read_json_file(file_path):
    try:
        data = pd.read_json(file_path) # ใช้ pd.read_json() ในการอ่านไฟล์ JSON
        logger.info(f"Read JSON file: {file_path}") # บันทึกข้อความว่าอ่านไฟล์ JSON สำเร็จ
        return data # คืนค่าข้อมูลที่ได้จากการอ่านไฟล์ JSON
    except Exception as e: # จัดการข้อผิดพลาดที่เกิดขึ้น
        logger.error(f"Error reading JSON file: {file_path}") # บันทึกข้อความว่าเกิดข้อผิดพลาดในการอ่านไฟล์ JSON
        return None

# สร้าง function consolidate_data โดยมี parameter data_list ใช้สำหรับรวมข้อมูลจากไฟล์ทั้งหมดเข้าด้วยกัน
def consolidate_data(file_paths):
    combined_data = [] # สร้าง list ว่างเพื่อเก็บข้อมูลที่รวมกัน
    for file_path in file_paths: # วนลูปเพื่ออ่านข้อมูลจากไฟล์ทั้งหมด
        if not os.path.exists(file_path): # ตรวจสอบว่าไฟล์นั้นมีอยู่จริงหรือไม่
            logger.error(f"File not found: {file_path}") # บันทึกข้อความว่าไม่พบไฟล์
            continue # ข้ามไฟล์นี้ไป
        exe = file_path.split('.')[-1].lower() # แยกชื่อไฟล์ออกจากนามสกุล และแปลงเป็นตัวพิมพ์เล็ก
        if exe == 'csv': # ถ้าเป็นไฟล์ CSV
            data = read_csv(file_path) # อ่านไฟล์ CSV
        elif exe == 'xlsx': # ถ้าเป็นไฟล์ Excel
            data = read_excel(file_path) # อ่านไฟล์ Excel
        elif exe == 'json': # ถ้าเป็นไฟล์ JSON
            data = read_json_file(file_path) # อ่านไฟล์ JSON
        else: # ถ้าเป็นไฟล์อื่นๆ
            logger.error(f"Unsupported file format: {file_path}") # บันทึกข้อความว่าไม่รองรับไฟล์นี้
            continue # ข้ามไฟล์นี้ไป
        if data is not None: # ถ้ามีข้อมูล
            combined_data.append(data) # เพิ่มข้อมูลที่ได้จากการอ่านไฟล์ลงใน list ที่เก็บข้อมูลที่รวมกัน
    if combined_data: # ถ้ามีข้อมูลที่รวมกัน
        combined_data = pd.concat(combined_data, ignore_index=True) # รวมข้อมูลที่ได้จากการอ่านไฟล์ทั้งหมดเข้าด้วยกัน
        return combined_data # คืนค่าข้อมูลที่รวมกัน
    else: # ถ้าไม่มีข้อมูลที่รวมกัน
        logger.error("No data to consolidate") # บันทึกข้อความว่าไม่มีข้อมูลที่รวมกัน
        return None # คืนค่า None หากไม่มีข้อมูลที่รวมกัน

# สร้าง function save_to_csv โดยมี parameter data, output_file ใช้สำหรับบันทึกข้อมูลที่รวมกันลงในไฟล์ CSV 
def save_to_csv(combined_data, output_file):
    try: # พยายามบันทึกข้อมูลลงในไฟล์ CSV
        if combined_data is not None: # ถ้ามีข้อมูลที่รวมกัน
            combined_data.to_csv(output_file, index=False) # บันทึกข้อมูลที่รวมกันลงในไฟล์ CSV โดยไม่รวม index 
            logger.info(f"Data saved to {output_file} successfully!!") # บันทึกข้อความว่าบันทึกข้อมูลสำเร็จ
        else: # ถ้าไม่มีข้อมูลที่รวมกัน
            logger.error("No data to save") # บันทึกข้อความว่าไม่มีข้อมูลที่ต้องการบันทึก
    except Exception as e: # จัดการข้อผิดพลาดที่เกิดขึ้น
        logger.error(f"Error saving data: {e}") # บันทึกข้อความว่าเกิดข้อผิดพลาดในการบันทึกข้อมูล

# สร้าง function get_input_files โดยไม่มีพารามิเตอร์ ใช้สำหรับรับ path ของไฟล์ที่ต้องการรวมกัน
def get_input_files(): # สร้าง function get_input_files โดยไม่มีพารามิเตอร์
    file_paths = [] # สร้าง list ว่างเพื่อเก็บ path ของไฟล์
    print("Please enter the paths of the files you want to combine (type 'done' when finished)") # แสดงข้อความให้ผู้ใช้กรอก path ของไฟล์ที่ต้องการรวมกัน
    while True: # วนลูปไปเรื่อยๆ
        file_path = input("Enter file path: ") # รับ path ของไฟล์จากผู้ใช้
        if file_path.lower() == 'done':  # ใช้ 'done' เพื่อหยุดการป้อนข้อมูล
            break # ออกจากลูป
        elif os.path.exists(file_path): # ตรวจสอบว่าไฟล์นั้นมีอยู่จริงหรือไม่
            file_paths.append(file_path) # เพิ่ม path ของไฟล์ลงใน list
        else: # ถ้าไฟล์ไม่มีอยู่จริง
            print(f"File {file_path} does not exist, please try again.") # แสดงข้อความว่าไฟล์ไม่มีอยู่จริง
    
    if len(file_paths) == 0: # ถ้าไม่มี path ของไฟล์ที่ถูกกรอก
        logger.error("No valid file paths provided.") # บันทึกข้อความว่าไม่มี path ของไฟล์ที่ถูกกรอก
        return None # คืนค่า None

# สร้าง function main ใช้สำหรับเรียกใช้งาน function อื่นๆ
def get_input_files(): # สร้าง function get_input_files โดยไม่มีพารามิเตอร์
    file_paths = [] # สร้าง list ว่างเพื่อเก็บ path ของไฟล์
    print("Please enter the paths of the files you want to combine (type 'done' when finished)") # แสดงข้อความให้ผู้ใช้กรอก path ของไฟล์ที่ต้องการรวมกัน
    while True: # วนลูปไปเรื่อยๆ
        file_path = input("Enter file path: ") # รับ path ของไฟล์จากผู้ใช้
        if file_path.lower() == 'done ' or file_path.lower() == 'finished' :  # ใช้ 'done' เพื่อหยุดการป้อนข้อมูล
            break # ออกจากลูป
        elif os.path.exists(file_path): # ตรวจสอบว่าไฟล์นั้นมีอยู่จริงหรือไม่
            file_paths.append(file_path) # เพิ่ม path ของไฟล์ลงใน list
        else: # ถ้าไฟล์ไม่มีอยู่จริง
            print(f"File {file_path} does not exist, please try again.") # แสดงข้อความว่าไฟล์ไม่มีอยู่จริง
    
    if len(file_path) == 0: # ถ้าไม่มี path ของไฟล์ที่ถูกกรอก
        logger.error("No valid file paths provided.") # บันทึกข้อความว่าไม่มี path ของไฟล์ที่ถูกกรอก
        return None # คืนค่า None หากไม่มี path ของไฟล์ที่ถูกกรอก
    
    return file_paths # คืนค่า path ของไฟล์ที่ถูกกรอก

# สร้าง function main ใช้สำหรับเรียกใช้งาน function อื่นๆ
def main(): # สร้าง function main โดยไม่มีพารามิเตอร์
    file_paths = get_input_files()  # รับข้อมูลจากผู้ใช้
    if not file_paths: # ถ้าไม่มีข้อมูลที่รับมา
        return # ออกจากโปรแกรม
    output_file = 'consolidated_output.csv' # กำหนดชื่อไฟล์ที่จะบันทึกข้อมูลที่รวมกัน
    consolidated_df = consolidate_data(file_paths) # รวมข้อมูลจากไฟล์ทั้งหมดเข้าด้วยกัน
    save_to_csv(consolidated_df, output_file) # บันทึกข้อมูลที่รวมกันลงในไฟล์ CSV

# เรียกใช้ function main
if __name__ == "__main__": # ใช้เพื่อตรวจสอบว่าโค้ดถูกเรียกใช้โดยตรงหรือไม่
    main() # เรียกใช้ function main




