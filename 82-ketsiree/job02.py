# รับข้อมูลสินค้าชิ้นที่ 1
print("--- สินค้ารายการที่ 1 ---")
name1 = input("กรอกชื่อสินค้าที่ 1: ")
price1 = float(input("กรอกราคาต่อชิ้น: "))
quantity1 = int(input("กรอกจำนวนที่ขายได้: "))
total1 = price1 * quantity1

# รับข้อมูลสินค้าชิ้นที่ 2
print("\n--- สินค้ารายการที่ 2 ---")
name2 = input("กรอกชื่อสินค้าที่ 2: ")
price2 = float(input("กรอกราคาต่อชิ้น: "))
quantity2 = int(input("กรอกจำนวนที่ขายได้: "))
total2 = price2 * quantity2

# คำนวณยอดขายรวมของสินค้าทั้ง 2 รายการ
grand_total = total1 + total2

# แสดงผลลัพธ์ทางหน้าจอ
print("\n[ สรุปรายงานยอดขายสินค้า ]")
print(f"สินค้า: {name1} | ราคา: {price1} บาท | จำนวน: {quantity1} ชิ้น | ยอดรวม: {total1} บาท")
print(f"สินค้า: {name2} | ราคา: {price2} บาท | จำนวน: {quantity2} ชิ้น | ยอดรวม: {total2} บาท")
print(f"ยอดขายทั้งหมดรวมทั้งสิ้น: {grand_total} บาท")
