def info(detail):
    print("สวัสดีครับ ผมชื่อ", detail["name"])
    print("ชื่อเล่น", detail["nickname"])
    print("กำลังศึกษาอยู่ที่", detail["school"])
    print("ระดับชั้น", detail["level"])
    print("สาขา", detail["major"])
    print("งานอดิเรก", detail["hobby"])


my_detail = {
    "name": "ธนาพิพัฒน์ วังกชา",
    "nickname": "โตโร่",
    "school": "อาชีวศึกษานครราชสีมา",
    "level": "ปวช2 ทด1",
    "major": "เทคโนโลยีธุรกิจดิจิทัล",
    "hobby": "ฟุตซอล"
}

info(my_detail)

    