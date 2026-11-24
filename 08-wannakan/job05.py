def info(**detail) :
    print(" สวัสดี คุณ " ,detail ["name"])
    print("ยินดีต้อนรับสู่ห้องเรียน" ,detail ["room"])
    print("อายุ", detail ["age"])
    print("น้ำหนัก", detail ["weight"])
    print("ส่วนสูง",detail ["height"])
    print("เพศ",detail ["sex"])
    print("งานอดิเรก",detail ["hobby"])

info(name = "วรรณกานต์", room = "คอมพิวเตอร์",age = 16 , weight =53,height =158,sex ="หญิง",hobby = "เล่นเกม")