"""
Objective:
Write a Python script that fetches data from the REST Countries API, processes the data to generate insights, and saves these insights into a JSON file.

Steps to Complete the Assignment:
    1. Use the REST Countries API
        - The REST Countries API provides information about countries worldwide.
        - Base URL: https://restcountries.com/v3.1/all
        - No authentication is required, and the API returns data in JSON format.
    2. Fetch the Data
        - Use Python's requests library to make an HTTP GET request to the REST Countries API.
        - Handle potential errors (e.g., network issues, invalid responses).

Example Code:
import requests

url = "https://restcountries.com/v3.1/all"
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    countries = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    countries = []  # Set to an empty list in case of an error

    3. Process the Data
        - Generate two insights from the API data:
            1. The top 5 countries with the largest populations.
            2. The continent with the highest number of countries.
        - Use Python's sorted() function and dictionaries to extract the required data.

Example Code:

# Extract and sort countries by population
top_countries = sorted(countries, key=lambda x: x.get('population', 0), reverse=True)[:5]

# Count the number of countries per continent
continent_counts = {}
for country in countries:
    continent = country.get('region', 'Unknown')
    continent_counts[continent] = continent_counts.get(continent, 0) + 1

# Find the continent with the highest number of countries
most_countries_continent = max(continent_counts, key=continent_counts.get)


    4. Save Insights to a JSON File
    5. Save the processed insights into a .json file using Python's json library.

Example Code:

import json

insights = {
    "top_countries_by_population": [
        {"name": country['name']['common'], "population": country['population']}
        for country in top_countries
    ],
    "continent_with_most_countries": most_countries_continent
}

with open("country_insights.json", "w") as f:
    json.dump(insights, f, indent=4)


Deliverables:
    1. A Python script (country_data_processor.py) that:
        - Fetches data from the REST Countries API.
        - Processes the data to generate insights.
        - Saves the insights to a JSON file.
    2. A JSON file (country_insights.json) containing the processed insights.

Expected Outcome:
The program should generate a JSON file with content like this:
json
คัดลอกโค้ด
{
    "top_countries_by_population": [
        {"name": "China", "population": 1402112000},
        {"name": "India", "population": 1380004385},
        {"name": "United States", "population": 331002651},
        {"name": "Indonesia", "population": 273523615},
        {"name": "Pakistan", "population": 220892340}
    ],
    "continent_with_most_countries": "Africa"
}



Submission Requirements:
    1. Upload the Python script file and the generated JSON file.
    2. Include a README file with:
        - A brief description of the REST Countries API.
        - Instructions to run the script.
"""
# นำเข้า library requests >> เป็นไลบรารีที่ใช้สำหรับการเชื่อมต่อและส่งคำขอไปยังเว็บไซต์หรือ API
import requests

# นำเข้า library json >> เป็นไลบรารีที่ช่วยในการจัดการข้อมูลแบบ JSON
import json

# นำเข้า library collections >> เป็นไลบรารีที่ช่วยในการจัดการข้อมูลแบบ Collection ใช้สำหรับนับความถี่ของข้อมูล 
from collections import Counter

# สร้าง function fetch_country_data โดยมี parameter url ใช้สำหรับค้นหาข้อมูลจาก API โดยใช้ url ของ API เป็นพารามิเตอร์
def fetch_country_data(url):
    try:
        url = "https://restcountries.com/v3.1/all"
        request = requests.get(url) # สร้างตัวแปร request โดยใช้ requests.get() สำหรับการเชื่อมต่อ API
        request.raise_for_status() # ใช้ raise_for_status() เพื่อจัดการข้อผิดพลาดที่อาจเกิดขึ้น หากมีข้อผิดพลาดจะทำการ raise ข้อผิดพลาดนั้นออกมา
        return request.json() # คืนค่าข้อมูลที่ได้จาก API ในรูปแบบ JSON กลับไป
    except requests.exceptions.RequestException as e: # จัดการข้อผิดพลาดที่เกิดขึ้นเมื่อมีข้อผิดพลาดในการส่งคำขอไปยังเว็บไซต์หรือ API
        print(e)
        return None
    except requests.exceptions.HTTPError as err: # จัดการข้อผิดพลาดที่เกิดขึ้นเมื่อมีข้อผิดพลาดในการเชื่อมต่อ API 
        print(err)
        return None # คืนค่า None หากเกิดข้อผิดพลาด

# สร้าง function process_country_data โดยมี parameter data ใช้เพื่อทำการแปรรูปข้อมูลที่ได้จาก API ให้อยู่ในรูปแบบที่ต้องการ
def process_country_data(data):
    countries = [] # สร้าง list ว่าง ชื่อ country เพื่อเก็บข้อมูลที่ได้จาก API
    for item in data: # วนลูปเพื่อดึงข้อมูลที่ต้องการจาก data ที่ได้จาก API
        name = item.get('name', 'N/A') # ดึงชื่อประเทศ ถ้าไม่พบก็ใช้ "N/A" เป็นค่าเริ่มต้น.
        population = item.get('population', 'N/A') # ดึงจำนวนประชากร ถ้าไม่พบก็ใช้ "N/A" เป็นค่าเริ่มต้น.
        countries.append({'name': name, 'population': population}) # เพิ่มข้อมูลที่ดึงมาจาก API ลงใน list country
    return countries # คืนค่า list ที่เก็บข้อมูลที่ดึงมาจาก API ส่งคืนลิสต์ของประเทศ

# สร้าง function top_country(data) โดยมี parameter data ใช้เพื่อคำนวณข้อมูลเชิงลึกจากข้อมูลของประเทศ จาก API
def top_country(data):
    top_countries = sorted(data, key=lambda x: x.get('population', 0), reverse=True)[:5] # คำนวณหาประเทศที่มีจำนวนประชากรมากที่สุด 5 ประเทศ
    top_countries_by_population = [ # สร้าง list ของประเทศที่มีจำนวนประชากรมากที่สุด 5 ประเทศ
        {"name": country['name'], "population": country['population']} for country in top_countries
    ]
    continent_counts = Counter(country['region'] for country in data) # นับจำนวนประเทศในแต่ละทวีป
    most_countries_continent = continent_counts.most_common(1)[0][0] # หาทวีปที่มีประเทศมากที่สุด
    return top_countries_by_population, most_countries_continent # คืนค่าข้อมูลที่คำนวณได้

# สร้าง function save_to_json โดยมี parameter filename,data ใช้เพื่อบันทึกข้อมูลที่ได้จาก API ลงในไฟล์ JSON
def save_to_json(filename,data):
    try:
        with open(filename, 'w',encoding='utf-8') as file:  # สร้างไฟล์ JSON ชื่อ country_insights.json โดยใช้โหมด w สำหรับการเขียนไฟล์ และใช้ utf-8 สำหรับการเขียนภาษาไทย
            json.dump(data, file,ensure_ascii=False, indent=4)
            print(f"Data saved to {filename} successfully!!")
    except Exception as e: # จัดการข้อผิดพลาดที่เกิดขึ้น
        print(f"Error saving data: {e}")

# สร้าง function main ที่ใช้เรียกใช้งาน function ทั้งหมด
def main():
    url = "https://restcountries.com/v3.1/all" # กำหนด url ของ API
    data = fetch_country_data(url) # เรียกใช้ function fetch_country_data โดยใช้ url ของ API ในพารามิเตอร์
    if data: # ถ้ามีข้อมูลจาก API
        countries = process_country_data(data)  # เรียกใช้ function process_country_data โดยใช้ข้อมูลที่ได้จาก API ในพารามิเตอร์
        top_countries, continent = top_country(countries)  # เรียกใช้ function top_country โดยใช้ข้อมูลที่ได้จาก API ในพารามิเตอร์ และเก็บข้อมูลที่ได้ ในตัวแปร top_countries, continent
        insights = { # สร้าง dictionary ชื่อ insights เพื่อเก็บข้อมูลที่คำนวณได้
            "top_countries_by_population": top_countries, # ประเทศที่มีจำนวนประชากรมากที่สุด 5 ประเทศ
            "continent_with_most_countries": continent # ทวีปที่มีประเทศมากที่สุด
        }
        save_to_json("country_insights.json", insights) # เรียกใช้ function save_to_json โดยใช้ข้อมูลที่ได้จาก API ในพารามิเตอร์
    else: # ถ้าไม่มีข้อมูลจาก API
        print("No data fetched from the API!!")

# เรียกใช้ function main
if __name__ == "__main__": # ใช้เพื่อตรวจสอบว่าโค้ดถูกเรียกใช้โดยตรงหรือไม่
    main() # เรียกใช้ function main