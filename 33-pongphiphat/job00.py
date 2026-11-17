price = float(input("ป้อนราคาสินค้า: "))
vat_rate = float(input("ป้อนอัตราภาษี VAT (เป็นเปอร์เซ็นต์ เช่น 7): "))

vat_amount = price * (vat_rate / 100)
total_price = price + vat_amount

print("-" * 30)
print("ราคาสินค้าตั้งต้น:", round(price, 2), "บาท")
print("มูลค่าภาษี VAT (", vat_rate, "%):", round(vat_amount, 2), "บาท")
print("ราคารวมสุทธิ (ราคารวมภาษี):", round(total_price, 2), "บาท")
print("-" * 30)