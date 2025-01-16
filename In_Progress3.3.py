# Review and refactor a piece of Python code for readability and suggest improvements.
'''
# This script manages a simple shopping cart

class Cart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, qty, price):
        if name in self.items:
            self.items[name]["qty"] += qty
        else:
            self.items[name] = {"qty": qty, "price": price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def total_cost(self):
        cost = 0
        for item in self.items:
            cost += self.items[item]["qty"] * self.items[item]["price"]
        return cost

cart = Cart()
cart.add_item("Apple", 3, 10)
cart.add_item("Banana", 2, 5)
cart.add_item("Apple", 1, 10)

cart.remove_item("Banana")
print("Total cost: ", cart.total_cost())
'''
# This script manages a simple shopping cart

class Cart:
    def __init__(self):
        self.items = {} # สร้างไว้ใส่สินค้าเหมือนตะกร้า รถเข็น ซึ่งยังว่างอยู่
    
    # เพิ่มสินค้าในตะกร้า
    def add_item(self, name, qty, price):
        if name in self.items: # ถ้าสินค้านี้มีอยู่แล้ว
            self.items[name]["qty"] += qty # จะอัปเดรตจำนวนสินค้า
        else: # ถ้าสินค้านี้ไม่มีอยู่
            self.items[name] = {"qty": qty, "price": price} # จะเพิ่มสินค้านี้ลงไป พร้อมกับ จำนวนสินค้า และราคา
    
    # ลบสินค้าในตะกร้า
    def remove_item(self, name):
        if name in self.items: # ถ้าสินค้านี้มีอยู่แล้ว
            del self.items[name] # จะทำการลบสินค้านี้ออกไป

    # คำนวณราคาทั้งหมดของสินค้าทั้งหมดในตะกร้า
    def total_cost(self):
        return sum(item['qty'] * item['price'] for item in self.items.values())
    
    # แสดงรายงานสอนค้า
    def __str__(self):
        # ตรวจสอบว่ามีสินค้าหรือไม่
        if not self.items:
            return "ตะกร้าสินค้าเปล่า" # ถ้าไม่มีจะแสดงข้อความ
        # สร้างสตริงรายการสินค้า
        items_str = "\n".join([f"{name}: {info['qty']} ชิ้น ราคา {info['price']:.2f} บาท" 
                               for name, info in self.items.items()])
        total = self.total_cost() # การคำนวณราคาทั้งหมด
        return f"ตะกร้าสินค้า:\n{items_str}\nTotal cost: {total:.2f} บาท"

cart = Cart()
cart.add_item("Apple", 3, 10)
cart.add_item("Banana", 2, 5)
cart.add_item("Apple", 1, 10)
cart.add_item("Tomato", 10, 5)
cart.remove_item("Banana")
print(cart)