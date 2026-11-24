def info(**detail) :
    print(" สวัสดี คุณ " ,detail ["name"])
    print("ยินดีต้อนรับสู่ห้องเรียน" ,detail ["room"])
    print("อายุ", detail ["age"])
    print("น้ำหนัก", detail ["weight"])
    print("ส่วนสูง",detail ["height"])
    print("เพศ",detail ["sex"])
    print("งานอดิเรก",detail ["hobby"])

info(name = "พิมพ์ลภัส", room = "คอมพิวเตอร์",age = 17 , weight =46,height =159,sex ="หญิง",hobby = "นอน")