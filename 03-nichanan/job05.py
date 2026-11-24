def info(**detail):
    print("สวัสดี คุณ" ,detail["name"])
    print("ยินดีต้อนรับสู่ห้องเรียน" ,detail["room"])
    print("อายุ" ,detail["age"])
    print("สีที่ชอบ" ,detail["color"])
    print("จังหวัด" ,detail["province"])

info(
    name = "เพลง" ,
    room = "อาชีวะ" ,
    age = 17 ,
    color = "ชมพูพาสเทล" ,
    province = "นครราชสีมา"
)

