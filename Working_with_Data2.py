'''
Write a Python script that reads a JSON file containing student grades, 
calculates the average score for each subject, and displays the results. 
The program must include robust error handling to manage unexpected scenarios.
'''
'''
Requirements
1. Input File:
    - The input file is named student_grades.json. student_grades.json
    - The file contains an array of student records where:
        - Each record includes the student's name (string) and their grades (a dictionary of subjects and scores).
Example structure:

[
    {
        "name": "Alice",
        "grades": {
            "Math": 85,
            "English": 90,
            "Science": 78
        }
    },
    {
        "name": "Bob",
        "grades": {
            "Math": 75,
            "English": 88,
            "Science": 82
        }
    }
]
2. Expected Output:
    - Calculate and print the average score for each subject across all students.
Example output:
    Subject Averages:
        - Math: 80.0
        - English: 89.0
        - Science: 80.0
'''
'''
Steps and Error Handling
1. File Handling:
    - Attempt to open and read the file student_grades.json.
        - If the file is missing or inaccessible, display a clear error message and terminate the program:

            Error: The file 'student_grades.json' does not exist or cannot be opened.


2. JSON Parsing:
    - Parse the contents of the JSON file.
        -If the file content is invalid or cannot be parsed, display an error message and terminate:
            Error: Invalid JSON format in 'student_grades.json'.


3. Data Validation:
    - Verify that the JSON structure matches the expected format:
        - Each student record must have:
            - A name field (string).
            - A grades field (dictionary of subject-score pairs).
    - If any record is invalid, skip it and display a warning:
        Warning: Skipping invalid student record: {"name": "Alice"}.


4. Processing:
    - Calculate the total score and count for each subject.
    - If a subject is missing for a student, assume a score of 0 for that subject and proceed without errors.
    - Compute the average score for each subject.

5. Output:
    - Print the calculated averages in a clean format.
    - If no valid records are found, display a message:
        No valid student data found to process.
'''
'''
Code Structure
1. Main Script:
    - Use a main() function to organize the program flow.
2. Functions:
    - load_json_file(file_path): Handles file reading and JSON parsing.
    - validate_data(data): Ensures the data structure is correct and logs warnings for invalid records.
    - calculate_averages(data): Calculates total and average scores for each subject.
    - display_summary(averages): Prints the averages in a formatted manner.
3. Error Handling:
    - Use try-except blocks for file handling and JSON parsing.
    - Validate data before processing and handle unexpected structures gracefully.
'''
'''
Deliverables
1. A Python script file named process_grades.py.
2. Example console output when run with the provided sample JSON data.
'''
'''
Evaluation Criteria
1. Correctness:
    - The program correctly calculates and outputs the subject averages.
2. Error Handling:
    - The program gracefully handles:
        - Missing or invalid files.
        - Invalid JSON content.
        - Missing or incorrect student record fields.
3. Code Clarity:
    - Code is modular, well-commented, and adheres to Python conventions.
4. Output Quality:
    - The output is clear and easy to understand.
'''
# นำเข้า library json >> ใช้ในการจัดการข้อมูล JSON
import json as js

# สร้าง Function load_json_file โดยรับ พารามิเตอร์คือ file_path(ที่มาของไฟล์)
def load_json_file(file_path):
    # ตรวจสอบความผิดพลาดของการรับไฟล์
    try: 
        # with open >> เปิดไฟล์โดยใช้โหมด read only แล้วก็ปิด file auto เพื่อช่วยป้องกันการเกิดข้อผิดพลาดที่อาจเกิดจากการลืมปิดไฟล์
        with open(file_path,'r') as file: 
            data = js.load(file) # ใช้สำหรับอ่านข้อมูล JSON จากไฟล์และแปลงข้อมูล JSON >> Python
        return data # ส่งผลเป็น data ที่ทำการแปลงแล้ว
    except FileNotFoundError: # เมื่อหา file ไม่เจอ จะแสดงข้อความผิดพลาดและหยุดการทำงาน
        print(f"Error: The file '{file_path}' does not exist or cannot be opened.")
        exit(1)
    except js.JSONDecodeError: # เมื่อ json file ไม่ถูกต้อง จะแสดงข้อความผิดพลาดและหยุดการทำงาน
        print(f"Error: Invalid JSON format in '{file_path}'.")
        exit(1)

# สร้าง Function validate_data เพื่อตรวจสอบความถูกต้องของข้อมูลที่ได้รับมาจาก parameter : data 
def validate_data(data):
    valid_data = [] # สร้าง list เปล่าเพื่อเก็บข้อมูลที่ถูกต้องเมื่อตรวจสอบผ่าน
    for d in data: # สร้าง loop เพื่อเช็คค่าใน data ซึ่งก็คือ list ที่มีข้อมูลทั้งหมดที่โหลดจาก json file
        # ถ้า d เป็น dict และ name ต้องอยู่ใน d และ d เป็น str และ grades ต้องอยู่ใน d 
        # และ grades จะต้องเป็น dict เนื่องจาก grades ควรจะเป็น dict {'math': 85, 'english': 90}
        if isinstance(d,dict) and 'name' in d and isinstance(d['name'],str) and 'grades' in d and isinstance(d['grades'],dict):
            valid_data.append(d) # เมื่อผ่านการตรวจสอบแล้วจะให้เพิ่ม d ใน valid_data
        else: # ถ้าไม่ผ่านการตรวจสอบแล้วจะให้แสดงข้อความ
            print(f"Warning: Skipping invalid student record: {d}")
    return valid_data # จากนั้นให้เก็บค่าไว้ใน valid_data

# สร้าง Function calculate_averages เพื่อคำนวณคะแนนรวมและค่าเฉลี่ยสำหรับแต่ละวิชา
def calculate_averages(data):
    calculates_total = {} # สร้าง dict ที่จะเก็บคะแนนรวมของแต่ละวิชา
    subject_counts = {} # สร้าง dict ที่เก็บจำนวนครั้งที่มีการคำนวณคะแนนสำหรับแต่ละวิชา

    # สร้าง loop สำหรับการดู student ใน data
    for student in data:
        grades = student['grades'] # เข้าถึงข้อมูลคะแนนของนักเรียนจาก key : 'grades'
        for subject, score in grades.items(): # สร้าง loop สำหรับการคืนค่าทั้งชื่อวิชา(subject) และคะแนน(score) สำหรับแต่ละวิชาใน grades จะทำให้เราสามารถลูปผ่านทุกวิชาและคะแนน
            # ตรวจสอบว่า subject อยูใน calculates_total ไหม? 
            # ถ้ายังไม่มีวิชานี้ใน calculates_total จะเพิ่มเข้าไปใน calculates_total และ subject_counts โดยกำหนดค่าเริ่มต้นเป็น 0
            if subject not in calculates_total: 
                calculates_total[subject] = 0 
                subject_counts[subject] = 0 
            calculates_total[subject] += score # เพิ่มคะแนน(score) ที่พบในวิชานั้นๆ ไปยังคะแนนรวมของวิชานั้นใน calculates_total
            subject_counts[subject] += 1 # เพิ่มจำนวนการนับวิชานั้นๆ ใน subject_counts เพื่อให้เราทราบจำนวนคะแนนที่นับในวิชานี้
    # จะคำนวณค่าเฉลี่ยสำหรับแต่ละวิชา โดยใช้คะแนนรวม (calculates_total[subject]) หารด้วยจำนวนการนับ (subject_counts[subject])        
    subject_averages = {subject: calculates_total[subject] / subject_counts[subject] for subject in calculates_total}
    return subject_averages # คืนค่าผลลัพธ์ที่เป็น dictionary  ซึ่งมีค่าเฉลี่ยของคะแนนในแต่ละวิชา

# สร้าง Function display_summary เพื่อแสดงผลลัพธ์ค่าเฉลี่ยของแต่ละวิชา
def display_summary(averages):
    if averages: # ถ้ามีค่าเฉลี่ยจะแสดงข้อความ และทำงานถัดไป
        print("Subject Averages:")
        # สร้าง loop เพื่อคืนค่าทุกคู่ของ keys และ value ใน averages ซึ่ง subject จะเป็นชื่อวิชา และ average จะเป็นค่าเฉลี่ยของคะแนนในวิชานั้น
        # เช่น ถ้า aver{'Math': 85.2, 'Science': 92.3} 
        # output : 
        # Subject Averages:
        # - Math: 85.2
        # - Science: 92.3
        for subject, average in averages.items(): 
            print(f"  - {subject}: {average:.1f}")
    else: # ถ้าไม่มีจะแสดงข้อความเตือน
        print("No valid student data found to process.")

# สร้าง Function เพื่อวบคุมลำดับการทำงานของโปรแกรมทั้งหมด
def main():
    # ใช้ตัวแปร file_path(ที่มาของ file)
    # ไฟล์นี้จะต้องเก็บข้อมูลในรูปแบบ JSON ของนักเรียนและคะแนนของแต่ละวิชา
    # ใส่ path ที่ถูกต้อง
    file_path = input("Enter your file path :")
   # '/Users/piinfany/Downloads/student_grades.json'
    
    # เรียกใช้ function load_json_file(file_path) เพื่อเปิดไฟล์ JSON ที่ file_path และทำการอ่านและแปลงข้อมูลจากไฟล์ JSON เป็น Python dictionary
    # ผลลัพธ์จาก function จะเก็บในตัวแปร data
    data = load_json_file(file_path)
    
    # เรียกใช้ function validate_data(data) ตรวจสอบว่าแต่ละ d ใน data มีโครงสร้างที่ถูกไหม?
    # function ส่งกลับลิสต์ valid_data ซึ่งเก็บข้อมูลของนักเรียนที่มีโครงสร้างถูกต้องเท่านั้น ถ้าไม่ถูกต้องจะแสดงข้อความเตือน
    valid_data = validate_data(data)
    
    # ถ้า valid_data มีข้อมูล
    if valid_data:
        # จะเรียกใช้ function calculate_averages(valid_data)
        # ซึ่งจะคำนวณค่าเฉลี่ยของคะแนนในแต่ละวิชาและส่งผลลัพธ์กลับมาเป็น dictionary ที่ชื่อว่า averages
        averages = calculate_averages(valid_data)
        # และเรียกใช้ function display_summary(averages) เพื่อแสดงผลค่าเฉลี่ย
        display_summary(averages)
    else: # ถ้า valid_data ไม่มีข้อมูล จะเรียกใช้ function display_summary([]) >> ลิสต์ว่าง 
          # นั่นคือจะแสดงข้อความ No valid student data found to process.
        display_summary([])

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


        









