# รับค่าคะแนนจากผู้ใช้ และแปลงเป็นทศนิยม (float) เพื่อรองรับคะแนนที่เป็นเศษส่วน
score = float(input("กรุณากรอกคะแนนของนักเรียน: "))

# ตรวจสอบเงื่อนไขเพื่อให้เกรด
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

# แสดงผลลัพธ์
print(f"คะแนนของคุณคือ {score} คะแนน ได้รับเกรด: {grade}")