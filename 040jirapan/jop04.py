def my_funtion(*num):
    print("สูตรหาพื้นที่สามเหลี่ยม")
    total = 0
    total = 0.5 * num[0] * num[1]  # สูตรพื้นที่สามเหลี่ยม = 1/2 x ฐาน x สูง
    print(total)

# เรียกใช้งานฟังก์ชัน โดยส่งค่า (ฐาน, สูง)
my_funtion(4, 10)