# --- รายการที่ 1 ---
product1 = input("ใส่ชื่อสินค้าที่ 1: ")
price1 = float(input("ใส่ราคาต่อชิ้น: "))
quantity1 = int(input("ใส่จำนวนที่ขาย: "))
total1 = price1 * quantity1

# --- รายการที่ 2 ---
product2 = input("ใส่ชื่อสินค้าที่ 2: ")
price2 = float(input("ใส่ราคาต่อชิ้น: "))
quantity2 = int(input("ใส่จำนวนที่ขาย: "))
total2 = price2 * quantity2

# --- คำนวณยอดรวมของทั้ง 2 รายการ ---
grand_total = total1 + total2

# --- แสดงผลลัพธ์ ---
print("\n--- สรุปข้อมูลยอดขาย ---")
print("สินค้าที่ 1:", product1, "| ราคา:", price1, "| จำนวน:", quantity1, "| ยอดขาย:", total1)
print("สินค้าที่ 2:", product2, "| ราคา:", price2, "| จำนวน:", quantity2, "| ยอดขาย:", total2)
print("ยอดรวมทั้งหมด:", grand_total)
