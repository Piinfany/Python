#Write a Python program that calculates the factorial of a number using a loop.
# Validate input ก่อนเอาค่าไปใช้งาน
number = int(input("Enter your number : "))
fac = 1
for i in range(1,number+1): 
    fac = fac*i
print("Factoraial of", number, "is", fac)
