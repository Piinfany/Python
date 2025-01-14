# Sales Data Filtering
'''
You are tasked with creating a Python script to process a sales dataset in CSV format. Specifically,
you will filter records for a given month and save the results to a new CSV file.
'''
'''
1. Input File
    - A CSV file named sales_data.csv  sales_data.csv will be provided.
    - This file contains at least the following columns:
        - Date (format: YYYY-MM-DD)
        - Sales Amount
        - Customer ID
        - Product ID
2. Filtering Criteria
    - Extract all records corresponding to a specific month (e.g., January 2025).
    - The month will be provided as input in the format YYYY-MM (e.g., 2025-01).
3. Output File
    - Save the filtered records to a new CSV file named filtered_sales_<YYYY-MM>.csv.
    - Ensure the output file retains the same column structure as the input file.
4. Steps to Follow
    a. Read the Input File
        - Use the pandas library to read the sales_data.csv file.
        - Handle errors gracefully (e.g., if the file is missing or improperly formatted).
    b. Filter Data
        - Parse the Date column to filter records based on the provided month.
        - Ensure that invalid or improperly formatted dates are ignored.
    c. Save the Filtered Data
        - Write the filtered data to a new CSV file named filtered_sales_<YYYY-MM>.csv.
    d. Output Confirmation
        - Print a success message with the output file name and the total number of filtered records.
'''
# นำเข้า library pandas >> ใช้ในการจัดการข้อมูล
import pandas as pd 

# นำเข้า library os >> ตรวจสอบการมีอยู่ของไฟล์
import os

# สร้าง parameter 3 ตัว โดย 1. ชื่อไฟล์ CSV ที่จะอ่าน, 2. ปี/เดือนที่ต้องการกรอง, 3. ชื่อไฟล์ CSV ใหม่ที่บันทึกข้อมูล
def filter_saledata (n_input_File,year_month,n_output_file):
    try:
        sales_data = pd.read_csv(n_input_File) # นำข้อมูลจากไฟล์ csv >> DataFrame ชื่อ sales_data
        
        # ถ้าไฟล์ csv ไม่มีคอลัมน์ที่จำเป็น จะแสดงข้อความเตือนและหยุดการทำงานของฟังก์ชัน
        if not all(col in sales_data.columns for col in ['Date', 'Sales Amount','Customer ID','Product ID']):
            raise ValueError("ไฟล์ CSV ขาดคอลัมน์ที่จำเป็น")
        
        # แปลงคอลัมน์ 'Date' >> ชนิดข้อมูลวันที่ และ ใช้ errors='coerce' เพื่อให้ค่าที่ไม่สามารถแปลงเป็นวันที่ถูกแทนที่ด้วย NaT
        sales_data['Date'] = pd.to_datetime(sales_data['Date'], errors='coerce')

        # จากนั้นก็ตรวจสอบว่าแปลงสำเร็จไหม โดยใช้ isnull() เพื่อเช็คว่าแถวไหนมีค่า NaT และจะแสดงข้อความ
        if sales_data['Date'].isnull().any():
            print("บางแถวมีวันที่ไม่ถูกต้อง!!")
        
        # filter ให้ตรงกับเดือนที่ต้องการ โดยมีรูปแบบวันที่เป็น 'YYYY-MM' แล้วเปรียบเทียบกับตัวแปร year_month ที่ผู้ใช้ป้อนเข้ามา
        filtered_saledata = sales_data[sales_data['Date'].dt.strftime('%Y-%m') == year_month]

        # ตรวจสอบข้อมูลที่มีการกรองเรียบร้อยแล้ว ซึ่งถ้าผลลัพธ์จากการกรองไม่มีข้อมูล(DF ว่าง) จะแสดงข้อความ
        if filtered_saledata.empty:
            print("ไม่มีข้อมูล!!")
            filtered_saledata.to_csv(n_output_file, index = False) # บันทึก file ได้แม้ไม่มีข้อมูล
            return
        
        # บันทึกข้อมูลที่กรองแล้วลงเป็นไฟล์ใหม่ และตั้งค่า index=False เพื่อไม่ให้บันทึกคอลัมน์ index ลงในไฟล์ csv
        filtered_saledata.to_csv(n_output_file, index = False)

        # แสดงผล
        print("ข้อมูลถูกกรองสำเร็จแล้วและถูกบันทึกในไฟล์ :", n_output_file)
        print("จำนวนที่กรองได้ทั้งหมด (รายการ):", len(filtered_saledata))

    except FileNotFoundError: # ถ้าไม่พบไฟล์ที่ระบุ
        print("ไม่พบไฟล์กรุณาตรวจสอบชื่อไฟล์และตำแหน่งไฟล์ :",n_input_File)
    except ValueError as e: # ถ้ามีข้อผิดพลาดในการแปลงข้อมูล (เช่น ค่าที่ไม่สามารถแปลงเป็นวันที่ได้)
        print(f"เกิดข้อผิดพลาดในการแปลงค่า: {e}")
    except Exception as e: # จัดการข้อผิดพลาดอื่นๆ
        print(f"เกิดข้อผิดพลาดอื่นๆ: {e}")
    

# เรียกใช้ function
filter_saledata('/Users/piinfany/Downloads/sales_data.csv', '2025-08', 'filtered_sales_2025-01.csv')



    




