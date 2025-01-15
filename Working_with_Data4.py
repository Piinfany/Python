# Sort and Save CSV Data
'''
The purpose of this assignment is to practice sorting data from a CSV file and writing the sorted data to a new file. 
This task will help you learn how to manipulate data efficiently and work with file operations in Python.
'''
'''
Assignment Details
You are provided with a CSV file named employees.csv  employees.csv that contains information about employees. Your task is to:
    1. Read the employees.csv file.
    2. Sort the employee data by:
        - Primary: DepartmentID (in ascending order).
        - Secondary: Name (alphabetically, in ascending order).
    3. Write the sorted data to a new file called sorted_employees.csv.
'''
'''
Steps to Complete the Assignment
    1. Set up the project:
        - Ensure you have Python installed.
        - Install any necessary libraries if required (e.g., pandas):
            - Use the command: pip install pandas (optional).
    2. Read the file:
        - Open the employees.csv file in Python.
        - Read the file contents and store them in a suitable data structure (e.g., list of dictionaries or DataFrame).
    3. Sort the data:
        - Sort the data first by DepartmentID (ascending) and then by Name (alphabetically).
    4. Write the sorted data:
        - Save the sorted data into a new file called sorted_employees.csv.
        - Ensure the output file maintains the same structure as the input file.
    5. Add error handling:
        - Handle errors such as missing or invalid files gracefully.
'''
'''
Input File: employees.csv
The input file has the following structure:
EmployeeID,Name,DepartmentID
101,Alice,2
102,Bob,1
103,Charlie,3
104,Diana,2
105,Eve,1
106,Frank,3

Expected Output File: sorted_employees.csv
After sorting, the output file should look like this:
EmployeeID,Name,DepartmentID
102,Bob,1
105,Eve,1
101,Alice,2
104,Diana,2
103,Charlie,3
106,Frank,3
'''

# นำเข้า library pandas >> ใช้ในการจัดการข้อมูลเป็น dataframe
import pandas as pd

try: # พยายามอ่านไฟล์ใน path
    employee_data = pd.read_csv('/Users/piinfany/Downloads/employees.csv') # อ่าน file แล้วเก็บไว้ใน employee_data

# ถ้าไฟล์ที่ต้องการอ่านไม่พบหรือไม่สามารถเปิดได้ จะแสดงข้อความแล้วจบการทำงาน
except FileNotFoundError:
    print("Error: The file does not exist or cannot be opened.")
    exit(1)

# ถ้าไฟล์ csv ที่เปิดมีข้อมูลว่าง(ไม่มีข้อมูลในไฟล์) จะแสดงข้อความแล้วจบการทำงาน
except pd.errors.EmptyDataError:
    print("Error: One of the CSV files is empty.")
    exit(1)

# ถ้าไฟล์มีปัญหากับรูปแบบของไฟล์ CSV ที่ไม่สามารถอ่านได้ จะแสดงข้อความแล้วจบการทำงาน
except pd.errors.ParserError:
    print("Error: There was an issue with the CSV file format.")
    exit(1)

# เรียงลำดับข้อมูลตาม DepartmentID และ Name จากน้อยไปมาก
employee_data_sorted = employee_data.sort_values(by = ['DepartmentID','Name'], ascending=[True, True])
print("Data has been sorted.")

try:
    employee_data_sorted.to_csv('sorted_employees.csv', index = False) # index=False: จะไม่บันทึกค่า index ที่ pandas ใช้ในการจัดการแถวต่างๆ ของ Dataframe ลงในไฟล์ csv
    print("Sorted data has been saved to 'sorted_employees.csv'.")

# ถ้ามีข้อผิดพลาดในการบันทึกไฟล์ (เช่น ไม่มีสิทธิ์ในการเขียนไฟล์) จะจับข้อผิดพลาดนี้และแสดงข้อความผิดพลาดที่เกิดขึ้น
except Exception as e:
    print(f"An error occurred: {e}")