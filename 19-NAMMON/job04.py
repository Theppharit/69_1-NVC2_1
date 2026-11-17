def calculate_triangle(*num):
    print("คำตอบของคุณคือ")
    total = 0
    # สูตรหาพื้นที่สามเหลี่ยม = (ฐาน * สูง) / 2
    total = (num[0] * num[1]) / 2
    print(total)

# คำนวณพื้นที่สามเหลี่ยม
calculate_triangle(60, 40)