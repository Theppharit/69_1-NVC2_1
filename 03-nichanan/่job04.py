def trapezoid_area(*num):
    print("พื้นที่สี่เหลี่ยมคางหมูคือ")
    area = 0.5 * (num[0] + num[1]) * num[2]
    print(area)

# ตัวอย่าง: ด้านขนานยาว 4 และ 6, สูง 5 -> 0.5 * (4 + 6) * 5 = 25.0
trapezoid_area(4, 6, 5)
