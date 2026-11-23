def info(**detail) :
    print("สวัสดี คุณ" ,detail["name"])
    print("ยินดีต้อนรับสู่ห้องเรียน" ,detail["room"])
    print("อายุ", detail["age"])
    print("อีเมล", detail["email"])
    print("ส่วนสูง", detail["height"])

info(name="มิ้น", room= "คอมพิวเตอร์", age=16, email="ketsiree.1604@gmail.com", height= "158",