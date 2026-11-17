def calculate_bmi(*num):
    print("คำตอบของคุณคือ")
    total = 0
    # สูตร: น้ำหนัก (กก.) / (ส่วนสูง (เมตร) ยกกำลัง 2)
    total = num[0] / (num[1] ** 2)
    print(total)

# บังกัส bmi 100
calculate_bmi(60, 1.40)