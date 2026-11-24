def info(**song):
    print("สวัสดี คุณ" ,song["name"])
    print("ยินดีต้อนรับสู่ห้องเรียน" ,song["room"])
    print("อายุ" ,song["age"])
    print("สีที่ชอบ" ,song["color"])
    print("จังหวัด" ,song["province"])

info(
    name = "สอง" ,
    room = "อาชีวะ" ,
    age = 17 ,
    color = "ชมพูพาสเทล" ,
    province = "นครราชสีมา"
)