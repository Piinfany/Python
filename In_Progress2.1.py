# Review and refactor a piece of Python code for readability and suggest improvements.
'''
# This script analyzes weather data

import math

def calc(data):
  total = 0
  for i in data:
    total += i
  mean = total/len(data)
  sum_sq = 0
  for i in data:
    sum_sq += (i - mean) ** 2
  std_dev = math.sqrt(sum_sq/len(data))
  return std_dev

class WeatherData:
    def __init__(this, t, h, r):
        this.temp = t
        this.humidity = h
        this.rainfall = r
    
    def temp_avg(data):
        total = 0
        for d in data:
            total += d.temp
        return total/len(data)

wd1 = WeatherData(30, 65, 5)
wd2 = WeatherData(32, 60, 10)
wd3 = WeatherData(28, 70, 15)

data = [wd1, wd2, wd3]
avg_temp = WeatherData.temp_avg(data)

print('The avg temp is: ' + str(avg_temp))
print('Standard deviation of temp:', calc([x.temp for x in data]))
'''
# นำเข้า library math >> ใช้สำหรับการคำนวณทางคณิตศาสตร์
import math

def calc_std(data):
    mean_data = sum(data) / len(data) # ใช้ sum และ len หา mean เพื่อหา std แทนการใช้ loop โดยไม่จำเป็น
    var_data = sum((i - mean_data) ** 2 for i in data) / len(data) # ลดรูป loop แล้วนำค่า mean มาคิดร่วม 
    return math.sqrt(var_data) # คืนค่าโดยใช้ sqrt ของ variance

# การสร้างคลาส WeatherData ซึ่งใช้เก็บข้อมูลเกี่ยวกับสภาพอากาศ ได้แก่ อุณหภูมิ (temp), ความชื้น (humidity), และปริมาณฝน (rainfall).
class WeatherData:
    def __init__(this, t, h, r):
        this.temp = t
        this.humidity = h
        this.rainfall = r
    
    def temp_avg(data):
        return sum(d.temp for d in data)/ len(data) # หา mean ของ temperature
    def humidity_avg(data):
        return sum(d.humidity for d in data) / len(data) # หา mean ของ humidity
    def rainfall_avg(data):
        return sum(d.rainfall for d in data) / len(data) # หา mean ของ rainfall
# Sample data
wd1 = WeatherData(30, 65, 5)
wd2 = WeatherData(32, 60, 10)
wd3 = WeatherData(28, 70, 15)

# สร้างลิสต์ data ซึ่งเก็บอ็อบเจ็กต์ WeatherData
data = [wd1, wd2, wd3]

# คำนวณค่าเฉลี่ยของอุณหภูมิ
avg_temp = WeatherData.temp_avg(data)
print(f'The avg temp is: {avg_temp:.1f} °C')

# คำนวณ Standard Deviation ของอุณหภูมิ
std_temp = calc_std([d.temp for d in data])
print(f'Standard deviation of temp: {std_temp:.2f} °C' )