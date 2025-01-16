# Refactor a provided poorly written script to adhere to Python best practices.
'''
# Issue: Poor naming conventions
def addnumlist(a):
    s = 0
    for n in a:
        s += n
    return s
'''
# หาผลรวมของผลบวก
def sum_of_numbers(a):
    s = 0
    for n in range(a):
        s += n
    return s
sum_of_numbers = sum_of_numbers(5) # 0 + 1 + 2 + 3 + 4
print(sum_of_numbers)

'''
# Issue: Poor naming conventions
def bigsmall(lst):
    big = lst[0]
    small = lst[0]
    for n in lst:
        if n > big:
            big = n
        if n < small:
            small = n
    return big, small
'''
# หาค่าสูงสุด ต่ำสุด
def find_max_min(lst):
    max = lst[0]
    min = lst[0]
    for n in lst:
        if n > max:
            max = n
        if n < min:
            min = n
    return max, min
find_max_min = find_max_min([1,4,78,9,-1])
print(find_max_min)

'''
# Issue: Lack of comments or documentation
def calcsum(lst):
    total = 0
    for num in lst:
        total += num
    return total
'''
# สร้าง function เพื่อหาผลรวมของ list
def sum_of_numbers(lst):
    total = 0
    for num in lst: # สร้าง loop เพื่อนำตัวเลขใน list ทุกตัว
        total += num # มาบวกเพิ่มจาก total = 0 ทีละตัว
    return total # คืนค่าผลบวกรวมของ list
sum_of_numbers = sum_of_numbers([1,4,78,9,-1])
print(sum_of_numbers) # (78, -1)

'''
# Issue: Lack of comments or documentation
def checkposneg(lst):
    pos = 0
    neg = 0
    for num in lst:
        if num >= 0:
            pos += 1
        else:
            neg += 1
    return pos, neg
'''
# สร้าง function เพื่อจำนวนที่เป็นบวก และจำนวนที่เป็นลบ ใน list
def count_pos_neg(lst):
    pos = 0 # pos ตั้งต้นเป็น 0 เพื่อไว้นับค่า
    neg = 0 # neg ตั้งต้นเป็น 0 เพื่อไว้นับค่า
    for num in lst: # ใช้ loop เพื่อนำตัวเลขใน list ทั้งหมดมาวน loop
        if num >= 0: # โดยที่ถ้า num มากกว่าหรือเท่ากับ 0 
            pos += 1 # จะบวก 1 ไปในตัวแปร pos ทีละตัวเลขใน list
        else: # โดยที่ถ้า num น้อยกว่า 0 
            neg += 1 # จะบวก 1 ไปในตัวแปร neg ทีละตัวเลขใน list
    return pos, neg # คืนค่าเป็น pos,neg ที่นับมา
count_pos_neg = count_pos_neg([1,4,78,9,-1]) 
print(count_pos_neg) # (4, 1)

'''
# Issue: Hard-to-read or unnecessarily complex code
def findevenodd(lst):
    even = []
    odd = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even.append(lst[i])
        else:
            odd.append(lst[i])
    return even, odd
'''
# หาชุดเลขคู่และเลขคี่
def find_even_odd(lst):
    even = [num for num in lst if num % 2 == 0]
    odd = [num for num in lst if num % 2 != 0]
    return even, odd
find_even_odd = find_even_odd([1,2,3,4,5,6,7,8,9,10])
print(find_even_odd)

'''
def reverselist(lst):
    rlist = []
    for i in range(len(lst) - 1, -1, -1):
        rlist.append(lst[i])
    return rlist
'''
# ย้อนกลับเลขใน list
def reverse_list(lst):
    return lst[::-1]
reverse_list = reverse_list([1,2,3,4,5])
print(reverse_list)

'''
# Issue: Repeated or redundant code
def sumofpositives(lst):
    total = 0
    for num in lst:
        if num > 0:
            total += num
    return total
'''
# หาผลรวมของค่าบวก
def sum_of_positives(lst):
    return sum(num for num in lst if num >= 0)
sum_of_positives = sum_of_positives([1,2,3,4,5,-4,-5])
print(sum_of_positives)

'''
# Issue: Repeated or redundant code
def sumofnegatives(lst):
    total = 0
    for num in lst:
        if num < 0:
            total += num
    return total
'''
# หาผลรวมของค่าลบ
def sum_of_negatives(lst):
    return sum(num for num in lst if num < 0)
sum_of_negatives = sum_of_negatives([1,2,3,4,5,-4,-5])
print(sum_of_negatives)

'''
# Issue: Non-standard practices
def listsize(lst):
    size = 0
    for _ in lst:
        size += 1
    return size
'''
# หาขนาดของ list
def list_size(lst):
    return len(lst)
list_size = list_size([1,2,3,4,5,-4,-5])
print(list_size)

'''
# Issue: Non-standard practices
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
'''
# หาเลขจำนวนเฉพาะ
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1): 
        # 2 ถึง sqrt(11) ≈ 3.32 ดังนั้น 11 หารลงตัวด้วย 2, 3, หรือไม่? ไม่เลย ดังนั้นผลลัพธ์คือ True (11 เป็นจำนวนเฉพาะ)
        # 2 ถึง sqrt(12) ≈ 3.46 ดังนั้น 12 หารลงตัวด้วย 2 (12 % 2 == 0) ดังนั้นผลลัพธ์คือ False (12 ไม่เป็นจำนวนเฉพาะ)
        if n % i == 0:
            return False
    return True
is_prime = is_prime(12)
print(is_prime)