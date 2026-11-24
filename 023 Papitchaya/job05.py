def info(**detail):
    print("สวัสดี คุณ" ,detail["name"])
    print("ยินดีต้อนรับสู่ห้องเรียน" ,detail["room"])
    print("อายุ" ,detail["age"])
    print("สีที่ชอบ" ,detail["color"])
    print("จังหวัด" ,detail["province"])

info(
    name = "น้ำน่าน" ,
    room = "วิทยะ 3.1" ,
    age = 17 ,
    color = "ชมพู" ,
    province = "นครราชสีมา"
)