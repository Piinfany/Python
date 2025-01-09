#Write a Python script to find the largest number in a list provided by the user.
li = []
size = int(input("Enter size : "))
for i in range(0,size):
    number = int(input("Enter your number : "))
    li.append(number)
print("largest in", li , "is", max(li))
