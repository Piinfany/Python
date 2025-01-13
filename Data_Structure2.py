# Implementing Stacks and Queues
# Use lists to implement stack (LIFO) and queue (FIFO) behaviors.
'''
1. Create a Stack class with methods:
    - push(item)
    - pop()
    - peek()
    - is_empty()
2. Create a Queue class with methods:
    - enqueue(item)
    - dequeue()
    - is_empty()
3. Test the implementation with the following sequence:
    - Push [1, 2, 3] onto the stack, then pop and peek.
    - Enqueue [4, 5, 6] into the queue, then dequeue and check emptiness.
'''

'''
Stack >> จะมีรูปแบบกันจัดเก็บข้อมูลในรูปแบบข้อง Last In First Out (LIFO) หรือแปลเป็นไทยง่าย ๆ 
เข้าไปทีหลังออกมาก่อนหรือลองมองเป็นภาพกล่องใส่ของที่เราวางลองทับลงไปเรื่อย ๆ 
แล้วเวลาเอาของออกก็ต้องเอาของด้านบานออกก่อน
'''
# สร้าง class 
class Stack:
    def __init__(self): 
        self.items = [] # สร้างตัวแปรเป็น list เพื่อเก็บข้อมูลใน Stack
    def is_empty(self):
        return self.items == [] # ตรวจสอบว่า Stack ว่างหรือไม่
    def push(self, item):
        self.items.append(item) # เพิ่มข้อมูลเข้าไปใน Stack โดย parameter คือ item 
    def pop(self):
        if self.is_empty():  # ตรวจสอบว่า Stack ว่างหรือไม่
            print("Error: Stack is empty. Cannot pop.")
            return None  # ถ้า Stack ว่าง ให้คืนค่า None
        return self.items.pop()  # นำข้อมูลที่อยู่ในตำแหน่งสุดท้ายของ list ออกไป
    def peek(self):
        if self.is_empty():  # ตรวจสอบว่า Stack ว่างหรือไม่
            print("Error: Stack is empty. Cannot peek.")
            return None  # ถ้า Stack ว่าง ให้คืนค่า None
        return self.items[-1]  # คืนค่าข้อมูลที่อยู่ในตำแหน่งสุดท้ายของ list
    
# สร้าง object มาก่อนจึงจะใช้งานได้
# ดูข้อมูลใน stack
stack = Stack()
print("Stack ก่อนการ push:", stack.items)

# push() >> ใช้เพื่อเพิ่มข้อมูลใน Stack
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack หลังการ push :",stack.items)

# pop() >> ใช้เพื่อลบข้อมูลออกจาก Stack
print("Stack ที่ pop ออก:", stack.pop())
print("Stack หลังการ pop ออก:",stack.items)

# peek() >> ดูข้อมูลที่อยู่ด้านบนสุด
print("Stack ตำแหน่ง peek :", stack.peek())

'''
Queue จะมีรูปแบบกันจัดเก็บข้อมูลในรูปแบบข้อง First In First Out (FIFO) 
หรือมองเป็นท่อส่งของที่ปลายด้านนึงจะใช้ในการแทรกข้อมูล (Enqueue) 
และปลายอีกด้านนึงจะใช้เพื่อทำการนำข้อมูลออก หรือลบข้อมูล (Dequeue)
'''
# สร้าง class   
class Queue:
    def __init__(self):
        self.items = [] # สร้างตัวแปรเป็น list เพื่อเก็บข้อมูลใน Queue
    def is_empty(self):
        return self.items == [] # ตรวจสอบว่า Queue ว่างหรือไม่
    def enqueue(self, item):
        self.items.insert(0,item) # เพิ่มข้อมูลเข้าไปใน Queue จะะใช้ insert ที่ตำแหน่ง 0 เวลาที่เพิ่มข้อมูลใหม
    def dequeue(self):
        if self.is_empty():  # ตรวจสอบว่า Queue ว่างหรือไม่
            print("Error: Queue is empty. Cannot dequeue.")
            return None  # ถ้า Queue ว่าง ให้คืนค่า None
        return self.items.pop()  # นำข้อมูลที่อยู่ในตำแหน่งสุดท้าย (ซึ่งคือคิวแรกที่ถูกเพิ่มเข้ามา) ออกไป

# สร้าง object มาก่อนจึงจะใช้งานได้
# ดูข้อมูลใน queue
queue = Queue()
print("Queue ก่อนการ enqueue : ", queue.items)

# enqueue() >> ใช้เพื่อเพิ่มข้อมูลใน queue
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print("Queue หลังการ enqueue : ", queue.items)

# dequeue() >> ใช้เพื่อลบข้อมูลออกจาก queue
print("Queue ที่ dequeue ออก:", queue.dequeue())
print("Queue หลังการ dequeue ออก : ", queue.items)

# isEmpty() >> ใช้เพื่อตรวจสอบว่า Stack ว่างหรือไม่
print("is empty? : ", queue.is_empty())

