# รายการที่ 1
print("--- รายการที่ 1 ---")
name1 = input("กรอกชื่อสินค้าที่ 1: ")
price1 = float(input("กรอกราคาต่อชิ้น: "))
quantity1 = int(input("กรอกจำนวนที่ขาย: "))
total1 = price1 * quantity1

# รายการที่ 2
print("\n--- รายการที่ 2 ---")
name2 = input("กรอกชื่อสินค้าที่ 2: ")
price2 = float(input("กรอกราคาต่อชิ้น: "))
quantity2 = int(input("กรอกจำนวนที่ขาย: "))
total2 = price2 * quantity2

# คำนวณยอดขายรวมทั้งหมด
grand_total = total1 + total2

# แสดงผลลัพธ์
print("\n================ รายงานสรุปยอดขาย ================")
print(f"สินค้าที่ 1: {name1} | ราคา: {price1:,.2f} บาท | จำนวน: {quantity1} ชิ้น | รวม: {total1:,.2f} บาท")
print(f"สินค้าที่ 2: {name2} | ราคา: {price2:,.2f} บาท | จำนวน: {quantity2} ชิ้น | รวม: {total2:,.2f} บาท")
print("-" * 50)
print(f"ยอดขายรวมทั้งหมด: {grand_total:,.2f} บาท")