# Working with Lists and Tuples
# Understand the differences between lists and tuples and learn how to perform basic operations.
'''
1. Create a list of 10 integers and a tuple of 10 strings.
2. Perform the following operations:
    - Append an integer to the list.
    - Remove an integer from the list.
    - Sort the list in ascending order.
    - Count how many times a specific integer appears in the list.
    - Access the 3rd element from the tuple.
3. Attempt to modify the tuple and explain the error (if any).
'''
# สร้าง list กับ tuple
lis = [5,3,7,1,8,5,2,6,4,9]
tup = ('apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'nectarine')
print("Original List :",lis)
print("Original Tuple :",tup)

# เพิ่ม 10 ลงใน lis เพื่อเป็นสมาชิกใหม่
lis.append(10)
print("List after appending 10: ", lis)

#  ลบ 7 ใน lis เพื่อลบสมาชิก
lis.remove(7)
print("List after removing 7: ", lis)

# เรียง lis จากน้อยไปมาก
lis.sort()
print("Sorted List :", lis)

# สร้างตัวแปรเพื่อเก็บค่าจำนวนนับของสมาชิกที่เป็น 5
lis1 = lis.count(5)
print("Count of 5 in List :", lis1)

# สมาชิกลำดับที่ 3 ของ tup
print("3rd element in Tuple :", tup[2])

# แก้ไขสมาชิกใน tuple (ซึ่งแก้ไขไม่ได้)
# TypeError: 'tuple' object does not support item assignment
tup[0] = "avocado" 