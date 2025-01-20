'''
Assignment Title:
    Develop a Script to Retrieve Cryptocurrency Data from CoinGecko and Save It to a CSV File

Objective:
    The goal of this assignment is to challenge your skills in API data retrieval, data transformation, and CSV manipulation. You will use the CoinGecko API, which is a free public API that provides cryptocurrency data and does not require sign-up.

Task Overview:
    Write a Python script that performs the following actions:
        1. Access the CoinGecko API:
            - Use the CoinGecko API to retrieve cryptocurrency market data.
        2. Retrieve Market Data for Multiple Cryptocurrencies:
            - Fetch market data for the top 10 cryptocurrencies by market capitalization.
        3. Process and Transform the Retrieved Data:
            - Extract the following fields for each cryptocurrency:
            - Cryptocurrency Name
            - Symbol
            - Current Price (in USD)
            - 24h Price Change Percentage
            - Market Capitalization
        4. Save the Transformed Data to a CSV File:
            - Save the extracted and transformed data to a file named crypto_data.csv.
            - Include appropriate headers in the CSV file.
        5. Bonus Task (Optional):
            - Calculate the average, minimum, and maximum of the Current Price and 24h Price Change Percentage for the top 10 
              cryptocurrencies and append this summary data at the bottom of the CSV file.


Key Deliverables:
    1. Python Script:
A .py file containing the complete script.
    2. Output File:
A CSV file named crypto_data.csv that contains the processed data, with optional summary statistics if completed.

Detailed Requirements:
    Step 1: API Details
    API Endpoint:
    Use the "Top 10 Cryptocurrencies" endpoint from CoinGecko:

https://api.coingecko.com/api/v3/coins/markets
    Query Parameters:
    - vs_currency=usd (to get prices in USD)
    - order=market_cap_desc (to sort by market cap)
    - per_page=10 (to limit results to the top 10 cryptocurrencies)
    - page=1 (first page of results)

Example URL:
https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1

    Step 2: Retrieve Data
    - Use Python’s requests library to make the API call.
    - Handle response cases:
        - Success (HTTP 200): Parse and process the response.
        - Failure (e.g., HTTP 404 or connection issues): Print appropriate error messages.
    Step 3: Extract and Transform Data
    - Parse the JSON response using Python’s json module.
    - Extract the following fields for each cryptocurrency:
        - name: Full name of the cryptocurrency.
        - symbol: Symbol of the cryptocurrency (e.g., BTC, ETH).
        - current_price: Current market price in USD.
        - price_change_percentage_24h: Percentage price change over the last 24 hours.
        - market_cap: Total market capitalization in USD.
    Step 4: Save Data to CSV
    - Use Python’s csv module to save the data in a file named crypto_data.csv.
    Include the following headers in the CSV file:

Name, Symbol, Current Price (USD), 24h Price Change (%), Market Capitalization (USD)

Bonus Task (Optional):
    - Calculate the following statistics for the Current Price and 24h Price Change Percentage:
        - Average: Mean value.
        - Minimum: Lowest value.
        - Maximum: Highest value.
    - Append these statistics as a new row in the CSV file with the header "Summary Statistics."

    Step 5: Clean Code Practices
    - Use functions for specific tasks (e.g., API call, data processing, CSV writing, and calculating statistics).
    - Add comments to explain each section of the script.
    - Use meaningful variable and function names.

Submission Guidelines:
    1. Script File: Submit the .py file containing the script.
    2. Output CSV: Include the crypto_data.csv file to demonstrate successful data processing.

Evaluation Criteria:
    1. Functionality (50%):
        - Does the script retrieve data for the top 10 cryptocurrencies?
        - Is the data correctly extracted, transformed, and saved to the CSV file?
        - (Bonus) Are summary statistics calculated and appended correctly?
    2. Code Quality (30%):
        - Is the code organized and readable?
        - Are functions and comments used effectively?
    3. Error Handling (10%):
        - Does the script handle errors (e.g., API failures, file I/O issues)?
    4. Adherence to Requirements (10%):
        - Does the script meet all specified requirements?
'''
# นำเข้า library json >> เป็นไลบรารีที่ใช้ในการจัดการข้อมูลในรูปแบบ JSON
import json as js

# นำเข้า library csv >> เป็นไลบรารีที่ใช้ในการอ่านและเขียนไฟล์ CSV
import csv 

# นำเข้า library requests >> เป็นไลบรารีที่ใช้ในการส่งคำขอ HTTP (ในที่นี้เราจะใช้มันเพื่อดึงข้อมูลจาก API)
import requests as req

# สร้าง function Fetch_data() เพื่อดึงข้อมูลจาก API มาเป็น JSON
def fetch_data():
    url_data = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1" # ส่งคำขอไปยัง API ของ CoinGecko.
    # พารามิเตอร์ที่ส่งไปพร้อมกับคำขอ API
    parameter = {
        'vs_currency': 'usd', # กำหนดสกุลเงินที่ใช้ในการแสดงผล
        'order': 'market_cap_desc', # เรียงลำดับตามมูลค่าตลาดจากมากไปน้อย
        'per_page': 10, # จำนวนเหรียญที่จะแสดงในแต่ละหน้า
        'page': 1} # กำหนดหน้าที่ 1 
    try:
        url = req.get(url_data,params=parameter) # ส่งคำขอ GET ไปยัง API พร้อมพารามิเตอร์ที่กำหนด
        url.raise_for_status() # ตรวจสอบเซิร์ฟเวอร์ส่งสถานะ HTTP ที่ไม่ผิดพลาด (เช่น 404, 500)
        print("Data Fetch successfully!! ")
        return url.json() # คืนค่าผลลัพธ์เป็น data ที่ดึงมาในรูปแบบของ json
    # ถ้ามีข้อผิดพลาดจะจับข้อผิดพลาด
    except req.exceptions.RequestException as e:
        print(f"Error Fetch data: {e}")
        return None
    
# สร้าง function dic_data(data) >> เพื่อทำการดึงข้อมูลสำคัญจากข้อมูล JSON ที่ได้จาก API มาเก็บเป็นรูปแบบของ dictionary
def dic_data(data):
    # สร้าง list เพื่อเก็บข้อมูลที่เกี่ยวข้อง
    dict_data = []
    # สำหรับแต่ละเหรียญใน data ดึงข้อมูลที่เกี่ยวข้องและเก็บไว้ใน c_data
    for c in data:
        c_data = {
            'Name': c.get('name', 'N/A'),
            'Symbol': c.get('symbol', 'N/A'),
            'Current Price (USD)': c.get('current_price', 0),
            '24h Price Change (%)': c.get('price_change_percentage_24h', 0),
            'Market Capitalization (USD)': c.get('market_cap', 0)
        }
        dict_data.append(c_data) # เพิ่มข้อมูลเหรียญแต่ละตัวลงใน dict_data
    return dict_data # ข้อมูลของเหรียญแต่ละตัวในรูปแบบของ list.

# สร้าง function save_csv(data, filename='crypto_data.csv') >> บันทึกข้อมูลที่ได้ (ในรูปแบบ dictionary) ลงในไฟล์ CSV
def save_csv(data, filename='crypto_data.csv'):
    col = ['Name', 'Symbol', 'Current Price (USD)', '24h Price Change (%)', 'Market Capitalization (USD)']  # ชื่อคอลัมน์ในไฟล์ CSV
    try:
        # เปิดไฟล์ที่ต้องการบันทึกข้อมูล
        # mode='w': เปิดไฟล์ในโหมด write ถ้าไฟล์ไม่มีอยู่ โปรแกรมจะสร้างไฟล์ใหม่ขึ้นมา ถ้าไฟล์มีอยู่แล้ว จะเขียนทับไฟล์เดิม
        # newline='': เพื่อหลีกเลี่ยงการเพิ่มบรรทัดว่าง (empty lines)
        with open(filename, mode='w', newline='') as file:
            file_w = csv.DictWriter(file, fieldnames=col)  # ใช้สำหรับการเขียนข้อมูลที่เป็น dictionary ลงในไฟล์ CSV
            file_w.writeheader()  # เขียนชื่อคอลัมน์ลงในไฟล์
            # สร้าง loops เพื่อเดินผ่านข้อมูลทุกแถวใน data นั่นคือ list ของ dictionary ที่มีข้อมูลเหรียญคริปโต
            for row in data:
                file_w.writerow(row)  # เขียนข้อมูลแต่ละแถวจาก data (ซึ่งแต่ละแถวเป็น dictionary) ลงในไฟล์ CSV
            print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# สร้าง function
def calculate_statistics(data):
    current_prices = [c['Current Price (USD)'] for c in data]
    price_changes = [c['24h Price Change (%)'] for c in data]
    
    avg_price = sum(current_prices) / len(current_prices)
    min_price = min(current_prices)
    max_price = max(current_prices)
    
    avg_change = sum(price_changes) / len(price_changes)
    min_change = min(price_changes)
    max_change = max(price_changes)
    
    statistics = {
        'Name': 'Summary Statistics',
        'Symbol': '',
        'Current Price (USD)': f'Average: {avg_price:.2f}, Min: {min_price:.2f}, Max: {max_price:.2f}',
        '24h Price Change (%)': f'Average: {avg_change:.2f}%, Min: {min_change:.2f}%, Max: {max_change:.2f}%',
        'Market Capitalization (USD)': ''
    }
    
    return statistics

# สร้าง function main() >> เชื่อมโยงทุกอย่างเข้าด้วยกัน
def main():
    crypto_data = fetch_data() # ดึงข้อมูลจาก API มาเป็น JSON
    if not crypto_data: # ถ้าไม่สามารถดึงข้อมูลได้ให้หยุดการทำงาน
        return
    
    dict_data = dic_data(crypto_data) # แปลงข้อมูลจาก JSON เป็น dictionary
    statistics = calculate_statistics(dict_data) # คำนวณสถิติ
    dict_data.append(statistics)  # เพิ่มข้อมูลสถิติไปยัง list
    
    save_csv(dict_data) # บันทึกข้อมูลทั้งหมด (รวมทั้งสถิติ) ลงในไฟล์ CSV

# เรียกใช้งานฟังก์ชันหลัก
if __name__ == "__main__":
    main()