#Grocery Discount Calculator
'''
Write a program that:
1. Allows the user to input their shopping list. The program should:
    - Ask for the product category (e.g., Fruits, Vegetables, Dairy, Meat).
    - Ask for the product price.
    - Continue until the user types "done".
2. Calculates the total bill and applies discounts based on:
    - Fruits and Vegetables:
    - No discount for amounts below 300 THB.
    - 5% discount for amounts between 300 and 700 THB.
    - 10% discount for amounts above 700 THB.
    - Dairy and Meat:
    - No discount for amounts below 500 THB.
    - 7% discount for amounts between 500 and 1,000 THB.
    - 15% discount for amounts above 1,000 THB.
3. Provides an additional 5% loyalty discount if the total bill after category-based discounts exceeds 2,000 THB.
4. Prints:
    - Total amount for each category before and after discounts.
    - Total bill after all discounts.
    - A message about any free gifts if the final bill exceeds 3,000 THB.
'''
#สร้างตัวแปรมาเก็บ price 
fruits_veggies_total = 0
dairy_meat_total = 0
#loop ไม่รู้รอบใช้ while >> True(infinity)
while True:
    category = input("Enter product category (e.g., Fruits, Vegetables, Dairy, Meat) or 'Done' for finish : ").lower() #ป้อน category แล้วเปลี่ยนค่า str เป็นตัวพิมพ์เล็ก
    if category == 'done': 
        break # ถ้าป้อน category จะหยุดการทำงาน input ของ category
    if category not in ["fruits","vegetables","dairy","meat"]:
        print("Invalid category. Please enter product category again.")
        continue # ถ้าป้อน category ไม่ถูกจะให้ป้อนใหม่ 
    price = float(input("Enter the price for the product :")) #ป้อน price แล้วเปลี่ยนค่า str เป็น float
#เช็คเงื่อนไขของ fruits กับ Vegetables
    if category == "fruits" or category == "vegetables": 
        fruits_veggies_total = fruits_veggies_total + price # เก็บค่าไว้ในตัวแปรมาที่เก็บ price
    else:
        dairy_meat_total = dairy_meat_total + price # ถ้าไม่ใช่ผักกับผลไม้ให้เก็บที่ dairy_meat_total แทน

#เช็คเงื่อนไขราคาอละส่วนลดของผักและผลไม้
if fruits_veggies_total > 0 :
    if fruits_veggies_total >= 700:
        fruits_veggies_discount = 0.10
    elif fruits_veggies_total >= 300 and fruits_veggies_total < 700:
        fruits_veggies_discount = 0.05
    else:
        fruits_veggies_discount = 0.0
    fruits_veggies_discount_total = fruits_veggies_total * (1 - fruits_veggies_discount) #คำนวณราคาลดทั้งหมดของผักและผลไม้
    print("Fruits/Vegetables Total:", fruits_veggies_total ,"THB") # ราคาผักและผลไม้ทั้งหมด
    print("Discount for Fruits/Vegetables:", fruits_veggies_discount*100 , "%" ) # จะได้ส่วนลดกี่เปอร์เซ็นต์
    print("After Discount:",fruits_veggies_discount_total ,"THB") #ราคาหลังหักส่วนลดทั้งหมดของผักและผลไม้
else :
    fruits_veggies_discount_total = 0 #ถ้าไม่ใช่กรณีข้างต้นให้ราคาหลังหักส่วนลดทั้งหมดของผักและผลไม้เป็น 0

#เช็คเงื่อนไขราคาอละส่วนลดของผักและผลไม้
if dairy_meat_total > 0:
    if dairy_meat_total >= 1000:
        dairy_meat_discount = 0.15  
    elif dairy_meat_total >= 500 and dairy_meat_total < 1000:
        dairy_meat_discount = 0.07  
    else:
        dairy_meat_discount = 0.0 
    discounted_dairy_meat_total = dairy_meat_total * (1 - dairy_meat_discount) # คำนวณราคาลดทั้งหมดของเนื้อและนม
    print("Dairy/Meat Total:", dairy_meat_total, "THB") # ราคาเนื้อและนมทั้งหมด
    print("Discount for Dairy/Meat:", dairy_meat_discount * 100, "%") # จะได้ส่วนลดกี่เปอร์เซ็นต์
    print("After Discount:", discounted_dairy_meat_total, "THB") # ราคาหลังหักส่วนลดทั้งหมดของเนื้อและนม
else:
    discounted_dairy_meat_total = 0 # ถ้าไม่ใช่กรณีข้างต้นให้ราคาหลังหักส่วนลดทั้งหมดของเนื้อและนมเป็น 0

total_after_category_discounts =  fruits_veggies_discount_total + discounted_dairy_meat_total # ราคาทั้งหมดเมื่อได้รับส่วนลด
print("Total Bill After Category-Based Discounts:", total_after_category_discounts, "THB")

if total_after_category_discounts > 2000: # ตรวจสอบว่าถ้าราคาทั้งหมดเมื่อได้รับส่วนลด ถ้ามากกว่า 2000 จะได้ลดเพิ่มอีก 5%
    after_discount = 0.05  
    final_total = total_after_category_discounts * (1 - after_discount) # ราคาหลังได้ลดเพิ่มอีก 5% 
    print("Loyalty Discount Applied: 5%")
else:
    final_total = total_after_category_discounts # ถ้าไม่ใช่รับส่วนลดให้ค่าเป็น total_after_category_discounts

print("Final Total Bill After All Discounts:", final_total, "THB") # แสดงราคาหลังได้ลดเพิ่มอีก 5% 

if final_total > 3000: # เช็คว่าได้รับของขวัญหรือไม่
    print("Congratulations! You qualify for a free gift!") 

