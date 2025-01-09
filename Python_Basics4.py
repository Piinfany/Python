#Write a Python script to find the largest number in a list provided by the user.
# สร้างตัวแปรให้มีค่าชนิดเป็น list
li = []
size = int(input("Enter size : ")) # ให้กำหนดว่าจะกรอกตัวเลขกี่ค่า
for i in range(0,size): # กำหนดให้นับตั้งแต่ index[0] แล้วเก็บที่ i จนถึง size
    number = int(input("Enter your number : "))
    li.append(number) # เพิ่ม number ที่กรอกแล้วไปเก็บใน li
print("largest in", li , "is", max(li)) # แสดงผลค่า Max 
