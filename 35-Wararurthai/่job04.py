def calculate_triangle_area(*num):
    print("คำตอบพื้นที่สามเหลี่ยมของคุณคือ")
    # สูตร: 0.5 * ฐาน * สูง
    total = 0.5 * num[0] * num[1]
    print(total)

# เรียกใช้งาน: ส่งค่าฐาน = 5 และ สูง = 10
calculate_triangle_area(5, 10)