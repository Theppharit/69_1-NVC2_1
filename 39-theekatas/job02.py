#ข้อมูลสินค้า1
name1 = input("ชื่อสินค้า: ")
price1 = float(input("ราคาต่อชิ้น: "))
qty1 = int(input("จำนวนที่ขาย: "))
#ข้อมูลสินค้า2
name2 = input("ชื่อสินค้า: ")
price2 = float(input("ราคาต่อชิ้น: "))
qty2 = int(input("จำนวนที่ขาย: "))
#คำนวณยอดขายทั้งหมด
total1 = price1 * qty1
total2 = price2 * qty2
grand_total = total1 + total2
#เเสดงผล
print(f"สินค้า: {name1}, ราคาต่อชิ้น: {price1}, จำนวน: {qty1}, ยอดขาย: {total1}")
print(f"สินค้า: {name2}, ราคาต่อชิ้น: {price2}, จำนวน: {qty2}, ยอดขาย: {total2}")
print(f"ยอดขายรวมทั้งหมด: {grand_total}")