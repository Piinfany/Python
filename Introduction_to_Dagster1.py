# Build a simple Dagster pipeline with one op that multiplies two numbers and logs the result.

# นำเข้า op, job, logger จาก dagster โดย op คือ operation หรือ function ที่เราต้องการให้ Dagster ทำงาน 
# และ job คือ การรวม operation หลาย ๆ ตัวเข้าด้วยกัน และ logger คือ การเขียน log ของ operation ที่เราต้องการ
from dagster import op, job

@op
def multiply_numbers(x:int,y:int):
    result = x * y
    return  result

@job
def my_job():
    multiply_numbers(3,4)


# ทดสอบการทำงานของ my_job โดยการใช้ execute_in_process() เพื่อให้ทำงานใน process ที่แยกออกจาก process หลัก
my_job.execute_in_process()






