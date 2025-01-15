# Merging CSV Files
'''
The goal of this assignment is to practice working with CSV files in Python by merging two data files 
and writing the combined data into a new file. This will help you understand file handling, 
data manipulation, and basic problem-solving skills in Python.
'''
'''
Assignment Details
You are provided with two CSV files:
1. Employee Data (employees.csv): employees.csv
    - Contains information about employees.
    - Example columns:
        - EmployeeID: A unique identifier for each employee.
        - Name: The employee's name.
        - DepartmentID: The ID of the department the employee belongs to.
2. Department Data (departments.csv): departments.csv
    - Contains information about departments.
    - Example columns:
        - DepartmentID: A unique identifier for each department.
        - DepartmentName: The name of the department.

Your task is to:
    1. Read the two CSV files (employees.csv and departments.csv).
    2. Merge the files based on the DepartmentID column.
    3. Write the merged data to a new CSV file (merged_data.csv).
'''
'''
Steps to Complete
    1. Set up the project:
        - Ensure you have Python installed.
        - Install any necessary libraries (e.g., pandas) if you choose to use external libraries:
            - Use the command: pip install pandas (if needed).
    2. Read the files:
        - Load the two CSV files into Python.
        - Check if the files are loaded correctly by printing a few rows.
    3. Merge the data:
        - Use the DepartmentID column as the key to combine the two datasets.
        - The merged data should include columns from both datasets: EmployeeID, Name, DepartmentID, and DepartmentName.
    4. Write the merged data:
        - Save the merged dataset into a new CSV file named merged_data.csv.
        - Ensure the file is correctly written by inspecting its contents.
    5. Add error handling:
        - Handle potential errors such as missing files, invalid data formats, or merge conflicts.
'''
'''
Sample Data
1. employees.csv
EmployeeID,Name,DepartmentID
101,Alice,1
102,Bob,2
103,Charlie,3
104,Diana,4
105,Eve,1

2. departments.csv
DepartmentID,DepartmentName
1,Human Resources
2,IT
3,Marketing
4,Finance
5,Sales

Expected Output
The final merged_data.csv file should look like this:
EmployeeID,Name,DepartmentID,DepartmentName
101,Alice,1,Human Resources
102,Bob,2,IT
103,Charlie,3,Marketing
104,Diana,4,Finance
105,Eve,1,Human Resources
'''
# นำเข้า library pandas >> ใช้ในการจัดการข้อมูลเป็น dataframe
import pandas as pd

try: # พยายามอ่านไฟล์ใน path
    employee_data = pd.read_csv('/Users/piinfany/Downloads/employees.csv') # อ่าน file แล้วเก็บไว้ใน employee_data
    department_data = pd.read_csv('/Users/piinfany/Downloads/departments.csv') # อ่าน file แล้วเก็บไว้ใน department_data

    # แสดงผลลัพธ์บางส่วนจากการอ่านไฟล์ ซึ่งในที่นี้จะเป็น Dataframe
    print("Employee Data : ")
    print(employee_data.head())
    print("Department Data :")
    print(department_data.head())

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

# การรวมข้อมูล (Merge)
'''
ใช้คอลัมน์ DepartmentID เป็นคีย์ในการรวมข้อมูล และใช้การรวมแบบ left join 
นั่นคือ เราจะเอาข้อมูลทั้งหมดจาก employee_data 
และข้อมูลที่ตรงกันใน department_data (ตาม DepartmentID) ก็จะถูกนำมารวมกัน 
ถ้าไม่ตรงก็จะใส่ค่า NaT ในคอลัมน์ที่ไม่ตรง
'''
merge_data = pd.merge(employee_data,department_data, on = 'DepartmentID', how = 'left')

# แสดงผลลัพธ์บางส่วนจากการ Merge data แล้ว
print("\nMerge Data :")
print(merge_data)

# ทำการบันทึกข้อมูลที่รวมแล้วลงในไฟล์ใหม่ชื่อ 'merged_data.csv'
try:
    merge_data.to_csv('merged_data.csv', index = False) # index=False: จะไม่บันทึกค่า index ที่ pandas ใช้ในการจัดการแถวต่างๆ ของ Dataframe ลงในไฟล์ csv
    print("\nMerged data has been written to 'merged_data.csv'")

# ถ้ามีข้อผิดพลาดในการบันทึกไฟล์ (เช่น ไม่มีสิทธิ์ในการเขียนไฟล์) จะจับข้อผิดพลาดนี้และแสดงข้อความผิดพลาดที่เกิดขึ้น
except Exception as e:
    print(f"An error occurred: {e}")

