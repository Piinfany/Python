# Review and refactor a piece of Python code for readability and suggest improvements.
'''
# This script reads a file and prints its content line by line

def readfile(filename):
  file = open(filename, "r")
  lines = file.readlines() # readlines() ที่จะเก็บทุกบรรทัดไว้ในลิสต์
  for l in lines:
      print(l)
  file.close()

readfile("sample.txt")
'''
# This script reads a file and prints its content line by line

def readfile(filename):
  with open(filename,'r') as file: # ใช้ with เพื่อเปิดไฟล์และจะปิดไฟล์อัตโนมัติเมื่อเสร็จสิ้น
     for l in file: # การวนลูปโดยตรงผ่าน file ทีละบรรทัด
        print(l, end="") # พิมพ์แต่ละบรรทัดโดยไม่เพิ่ม newline

readfile("/Users/piinfany/Desktop/Note/Note/สรุปการ Query เบื้องต้นพร้อมตัวอย่าง.txt")