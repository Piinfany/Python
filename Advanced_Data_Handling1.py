'''
Objective:
Write a Python script that:
    1. Connects to a SQLite database.
    2. Fetches data from a specific table.
    3. Processes the data using Pandas.

Task Overview:
Your goal is to demonstrate your ability to work with SQLite for database operations and Pandas for data analysis. The script you create should connect to a SQLite database, retrieve data from a table, and perform basic data processing tasks.

Deliverables:
    1. Python Script: A .py file containing the code.
    2. ReadMe File (optional but encouraged): A .md file explaining how to run your script and the results it produces.

Assignment Details:
    1. Setting Up the SQLite Database
        - Create a SQLite database file (e.g., example.db) if it doesn’t already exist.
        - Add a table to the database (e.g., sales_data) with the following schema:
CREATE TABLE sales_data (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    quantity_sold INTEGER,
    sale_date TEXT,
    revenue REAL
);
        - Populate the table with this script : insert_sales_data.sql
    2. Writing the Script
        Your script should:
        1. Import Required Libraries: Ensure the use of sqlite3 and pandas.
        2. Connect to the SQLite Database:
            - Use Python’s sqlite3 library to establish a connection to the database.
            - Include error handling for connection failures.
        3. Fetch Data from the Table:
            - Write an SQL query to retrieve all rows from the sales_data table.
            - Store the results in a Pandas DataFrame.
        4. Process the Data:
            - Perform at least two basic data processing tasks using Pandas. Examples:
                - Calculate the total revenue for all products.
                - Find the product with the highest quantity sold.
                - Filter data for sales made after a specific date.
        5. Display Results:
            - Print the processed data in a readable format.
    3. Example Output
       Your script should output results similar to the following:
       Total Revenue: $10,500.50
       Product with Highest Sales: iPhone (Quantity Sold: 150)
       Filtered Data (Sales After 2023-01-01):
   id     product_name  quantity_sold   sale_date   revenue
   0   3     MacBook Pro             40   2023-02-15   500.00
  1   5     Nintendo Switch         25   2023-03-10   300.00

Instructions for Submission:
    1. Save your Python script as fetch_and_process_data.py.
    2. Ensure your script is well-documented with comments explaining each step.
    3. If applicable, include your SQLite database file (example.db) and a ReadMe file.
    4. Submit all files in a compressed .zip folder.

Tips:
Test your script with different data to ensure it handles edge cases.
Use Pandas’ built-in functions for calculations and data filtering.
Follow Python best practices for code readability and organization.

Evaluation Criteria:
    1. Correctness: Does the script connect to the database, fetch data, and process it correctly?
    2. Code Quality: Is the code readable, well-structured, and documented?
    3. Creativity: Are the data processing tasks meaningful and insightful?
    4. Completeness: Are all required deliverables included and functional?
'''
# นำเข้า library sqlite3 >> เป็นไลบรารีที่ใช้ในการทำงานกับฐานข้อมูล
import sqlite3 as sq

# นำเข้า library pandas >> ใช้ในการจัดการข้อมูล
import pandas as pd 

# สร้าง function connect_db(db_name) เพื่อ connect db โดยรับ parameter : db_name
def connect_db(db_name):
    # พยายามรับ db มาเก็บไว้ใน python แล้วนำไปใส่ไว้ในตัวแปร connect
    try: 
        connect = sq.connect(db_name)
        print(f"Connected to {db_name} DB")
        return connect
    # ถ้ามีข้อผิดพลาดจะจับข้อผิดพลาด
    except sq.Error as e:
        print(f"Error connecting to DB: {e}")
        return None

 # สร้าง function  pull_data(connect) เพื่อดึงข้อมูลจาก database มาเป็น dataframe
def pull_data(connect):
    try:
        query = "SELECT * FROM sales_data" # ดึง data โดยใช้ query ดึงข้อมูลทั้งหมดจากตาราง sales_data
        data = pd.read_sql(query,connect) # ดึง data มาเป็น dataframe
        print("Data Pull successfully!!")
        return data # คืนค่าผลลัพธ์เป็น data ที่ดึงมา
    # ถ้ามีข้อผิดพลาดจะจับข้อผิดพลาด
    except sq.Error as e:
        print(f"Error pull data: {e}")
        return None

# สร้าง function calc_data(data) เพื่อคำนวณค่าต่างๆ และแสดง
def calc_data(data):

    # คำนวณรายได้รวม 
    total_revenue = data['revenue'].sum()

    # ค้นหาผลิตภัณฑ์ที่มียอดขายสูงสุด โดยใช้ idxmax()
    max_saleprod = data.loc[data['quantity_sold'].idxmax()]

    # กรองข้อมูล สำหรับยอดขายที่เกิดขึ้นหลังจากวันที่ 2023-01-01
    filtered_data = data[data['sale_date'] > '2023-01-01']

    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Product with Highest Sales: {max_saleprod['product_name']} (Quantity Sold: {max_saleprod['quantity_sold']})")
    print(f"Filtered Data (Sales After 2023-01-01):")
    print(filtered_data)

# สร้าง function main() 
def main():
    db_name = '/Users/piinfany/Downloads/SQLife' # ชื่อของไฟล์ฐานข้อมูล SQLite
    connect = connect_db(db_name) # ถ้าเชื่อมต่อสำเร็จ ตัวแปร connect จะเก็บค่าการเชื่อมต่อนั้นไว้
    # ถ้าเชื่อมต่อสำเร็จ จะนำฟังก์ชัน pull_data(connect) 
    if connect:
        data = pull_data(connect)
        # ถ้า pull_data(connect) ดึงเสร็จแล้วจะตรวจสอบว่า data ไม่ว่างมั้ย
        if data is not None:
            calc_data(data) # ถ้ามีข้อมูลจะนำฟังก์ชัน calc_data(data) 
        connect.close() #  ปิดการเชื่อมต่อฐานข้อมูล

'''
ทำไมต้องใช้? : เป็นการตรวจสอบว่าไฟล์ Python ถูกรันโดยตรงหรือถูกนำเข้าเป็นโมดูล
สามารถรันได้ทั้งเป็นโปรแกรมหลัก (โดยการรันไฟล์นั้นโดยตรง) และ
สามารถนำไปใช้เป็นโมดูลในโปรแกรมอื่น (โดยการนำเข้าในไฟล์อื่น) โดยไม่ทำให้ฟังก์ชัน main() หรือฟังก์ชันใด ๆ ที่อยู่ในไฟล์นั้นถูกเรียกใช้อัตโนมัติ
'''
# __name__ เป็นตัวแปรพิเศษใน Python ซึ่งจะเก็บค่าแตกต่างกันตามสถานการณ์ที่ไฟล์ Python ถูกเรียกใช้
# ถ้าไฟล์ Python ถูก เรียกใช้โดยตรง __name__ >> '__main__'
if __name__ == "__main__": 
# ตรวจสอบว่าไฟล์นี้ถูกเรียกใช้โดยตรงหรือไม่ หาก __name__ เป็น '__main__' (แสดงว่าไฟล์นี้ถูกรันโดยตรง)
# โปรแกรมจะทำการเรียกใช้ฟังก์ชัน main() ซึ่งเป็นจุดเริ่มต้นของการทำงานของโปรแกรม
# ถ้าไฟล์นี้ถูกนำเข้าเป็นโมดูล (เช่น import script), คำสั่ง main() จะไม่ถูกเรียกใช้ และจะไม่มีการทำงานใดๆ เกิดขึ้น
    main()

    
