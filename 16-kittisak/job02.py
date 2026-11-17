# รายการที่ 1
name1 = input("กรอกชื่อสินค้าที่ 1 : ")
price1 = float(input("ราคา : "))
qty1 = int(input("จำนวน : "))
total1 = price1 * qty1

# รายการที่ 2
name2 = input("กรอกชื่อสินค้าที่ 2 : ")
price2 = float(input("ราคา : "))
qty2 = int(input("จำนวน : "))
total2 = price2 * qty2

# แสดงผล
print("\n=== สรุปรายการขาย ===")
print("สินค้า 1:", name1, "| ราคา:", price1, "| จำนวน:", qty1, "| ยอดรวม:", total1)
print("สินค้า 2:", name2, "| ราคา:", price2, "| จำนวน:", qty2, "| ยอดรวม:", total2)
print("ยอดรวมทั้งหมด:", total1 + total2, "บาท")