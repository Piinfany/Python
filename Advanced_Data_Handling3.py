'''
Assignment Title:
Connecting to a MySQL Database, Executing Queries, and Visualizing Results
Objective:
The purpose of this assignment is to develop a Python script that connects to a MySQL database, retrieves data using a SQL query, and visualizes the results using Matplotlib. This exercise will improve your skills in database handling, data extraction, and visualization.

Guidelines and Instructions:
Setup:
    1. Ensure MySQL is installed and running on your system.
        - Use the provided SQL file (employees_data.sql) employees_data.sql to create the table and populate it with 2000 sample records. 
    2. Database Information:
        - Database Name: sample_database
        - Table Name: employees

Table Structure:

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);

        - Sample Data: 2000 records will be provided in the employees_data.sql file.

    3. Requirements:
        - Connect to a MySQL database using the mysql-connector-python library.
        - Write a SQL query to retrieve data from the employees table.
        - Use Matplotlib to visualize the data. The type of visualization should be appropriate for the data retrieved (e.g., bar chart, line graph, or scatter plot).
    4. Steps to Complete the Assignment:
        - Install necessary Python libraries:
            - mysql-connector-python
            - matplotlib
        - Write a Python script that:
            - Connects to the MySQL database using credentials.
            - Executes a query to fetch data from the employees table.
            - Parses the query result into a suitable format for visualization.
            - Generates a visualization using Matplotlib.
        - Ensure your script is modular:
            - Define functions for each task (e.g., connect_to_database, execute_query, visualize_data).
            - Include error handling for database connection and query execution.

Example Query:

SELECT department, COUNT(*) AS employee_count 
FROM employees 
GROUP BY department;


    5. This query retrieves the number of employees in each department.
    6. Visualization Example:
        - Create a bar chart where:
            - X-axis: Department names
            - Y-axis: Number of employees

Expected Output:
Example Data (retrieved from the database):
Department
Employee Count
HR
10
IT
25
Marketing
15
Sales
20

Example Visualization:
A bar chart with departments on the X-axis and employee counts on the Y-axis.

Deliverables:
    1. Python script (mysql_visualization.py) with clear comments and modular functions.
    2. A screenshot or image of the generated visualization.
    3. A README file explaining how to run the script, including any dependencies.
    4. SQL file (employees_data.sql) containing:
        - The table structure.
        - Insert statements to populate the table with 2000 records.

Additional Notes:
    - Test your script with the provided sample database.
    - Ensure that your visualization is clear, with labeled axes and a title.
    - Add any customizations that make your chart more visually appealing.

Evaluation Criteria:
Criteria
Weight (%)
Database Connection Setup
20%
Query Execution
20%
Data Parsing
20%
Visualization Quality
30%
Code Modularity & Comments
10%
'''
# นำเข้า library mysql.connector >> เป็นไลบรารีที่เป็นเครื่องมือที่ช่วยให้ Python สามารถเชื่อมต่อและทำงานกับฐานข้อมูล MySQL ได้
import mysql.connector

# นำเข้า >> เป็นไลบรารีสำหรับการนำเข้า Error จาก mysql.connector เพื่อให้สามารถจัดการกับข้อผิดพลาดที่เกิดขึ้นระหว่างการเชื่อมต่อกับฐานข้อมูลได้
from mysql.connector import Error

# สร้าง function connect_db() เพื่อเชื่อมต่อกับฐานข้อมูล
def connect_db():
    try: # พยายามเชื่อมต่อฐานข้อมูล โดยมี host,database,user,password ในการเข้าถึง
        connection = mysql.connector.connect(
            host = 'localhost',
            database = 'sample_database',
            user = 'root',
            password = 'Pinut251157'
        )
        if connection.is_connected(): # ถ้าเชื่อมต่อสำเร็จ จะแสดงข้อความ
            print("Connected to MySQL database!!")
            return connection # คืนค่าการเชื่อมต่อไปใน function
    # ถ้ามีข้อผิดพลาดจะจับข้อผิดพลาด
    except Error as e: 
        print(f"Error: {e}")
        return None # ถ้าเกิดข้อผิดพลาดจะคืนค่า None ซึ่งหมายความว่าการเชื่อมต่อล้มเหลว

# สร้าง function run_query(connection,query) เพื่อ run คำสั่ง sql(query) บนฐานข้อมูล mysql
def run_query(connection,query):
    try: # พยายาม
        run = connection.cursor(dictionary=True) # สร้าง run เพื่อชี้ไปที่ฐานข้อมูล โดยใช้ parameter dict >> ผลลัพธ์ที่ได้จากการรันคำสั่ง SQL จะถูกจัดเก็บเป็น dictionary (เข้าถึงข้อมูลง่ายขึ้น)
        run.execute(query) # รันคำสั่ง SQL ที่ได้รับมาในพารามิเตอร์ query โดยจะทำการส่งคำสั่ง SQL ไปยังฐานข้อมูล
        result = run.fetchall() # ใช้ในการดึงข้อมูลทั้งหมดจากผลลัพธ์ของคำสั่ง SQL ที่รันไป โดยจะคืนค่าผลลัพธ์เป็นรายการ (list) ของ dictionary
        run.close() # ปิด run หรือการชี้ไปที่ฐานข้อมูล หลังจากที่เราใช้เสร็จ
        return result # คืนค่าผลลัพธ์
    # ถ้ามีข้อผิดพลาดจะจับข้อผิดพลาด (เช่น การรันคำสั่ง SQL ไม่สำเร็จ) จะแสดงข้อความ
    except Error as e:
        print(f"Error run query: {e}")
        return None # คืนค่า None ซึ่งหมายความว่าไม่สามารถดำเนินการกับคำสั่ง SQL ได้ และไม่สามารถส่งผลลัพธ์กลับมา

#สร้าง function 
def display_table(data):
    # ใช้ pandas เพื่อแสดงข้อมูลในรูปแบบตาราง
    df = pd.DataFrame(data)
    print("\nข้อมูลที่ดึงมาแสดงผล:")
    print(df)
# นำเข้า library matplotlib.pyplot >> ในการสร้างกราฟแท่ง (bar chart)
import matplotlib.pyplot as plt

# สร้าง function visualize_data เพื่อสร้างกราฟ โดยมี parameter เป็น data >> ข้อมูลที่ต้องการสร้างกราฟ
def visualize_data(data):
    # ตรวจสอบว่ามี data ไหม?
    if data: # ถ้ามี data
        departments = [row['department'] for row in data] # สร้าง list ของแผนก
        count_employee = [row['employee_count'] for row in data] # สร้าง list ของจำนวนพนักงาน
        plt.figure(figsize=(10, 6)) # กำหนดขนาดของกราฟ
        plt.bar(departments, count_employee, color='skyblue') # สร้างกราฟแท่ง โดยกำหนดแกน X เป็นแผนก และแกน Y เป็นจำนวนพนักงาน
        plt.xlabel('Department') # กำหนดชื่อแกน X
        plt.ylabel('Employee Count') # กำหนดชื่อแกน Y
        plt.title('Number of Employees per Department') # กำหนดชื่อกราฟ
        plt.xticks(rotation=45, ha='right') # หมุนชื่อแผนก 45 องศา และจัดตำแหน่งชื่อแผนกให้ชิดขวา
        plt.tight_layout() # ปรับขนาดกราฟให้พอดี
        plt.show() # แสดงกราฟ

# สร้าง function main() เพื่อรันโปรแกรม
def main():
    # query ที่ต้องการใช้
    query = """
    SELECT department, COUNT(*) AS employee_count
    FROM employees
    GROUP BY department;
    """

    # เชื่อมต่อกับฐานข้อมูล โดยใช้ function connect_db()
    connection = connect_db()

    # ตรวจสอบว่าเชื่อมต่อสำเร็จมั้ย? ถ้าสำเร็จจะทำการดึงข้อมูล
    if connection:
        # ดึงข้อมูลจากฐานข้อมูล โดยใช้ function run_query(connection,query)
        data = run_query(connection, query)
        
        # ตรวจสอบว่ามีข้อมูลไหม? ถ้ามีจะทำการสร้างกราฟ
        visualize_data(data)

        # ปิดการเชื่อมต่อกับฐานข้อมูล
        connection.close()
        print("Connection closed!!")

# รันโปรแกรม
if __name__ == "__main__": # ถ้าโปรแกรมถูกเรียกใช้โดยตรงจะทำการรันโปรแกรม
    main() # รัน function main()
    

