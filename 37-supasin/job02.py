# คนหล่อ
name1 = input("กรอกชื่อสินค้าชิ้นที่ 1: ")
price1 = float(input("กรอกราคาสินค้าชิ้นที่ 1: "))
qty1 = int(input("กรอกจำนวนสินค้าชิ้นที่ 1: "))
total1 = price1 * qty1

# ศุภสิน  กิจเจ
name2 = input("กรอกชื่อสินค้าชิ้นที่ 2: ")
price2 = float(input("กรอกราคาสินค้าชิ้นที่ 2: "))
qty2 = int(input("กรอกจำนวนสินค้าชิ้นที่ 2: "))
total2 = price2 * qty2

# บังกัส
print("\n=== สรุปรายการขาย ===")
print("สินค้า 1:", name1, "| ราคา:", price1, "| จำนวน:", qty1, "| ยอดรวม:", total1)
print("สินค้า 2:", name2, "| ราคา:", price2, "| จำนวน:", qty2, "| ยอดรวม:", total2)
print("ยอดรวมทั้งหมด:", total1 + total2, "บาท")