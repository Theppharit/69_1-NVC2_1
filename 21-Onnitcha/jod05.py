def info(**detail) :
    print("สวัสดี คุณ",detail["name"]) 
    print("ยินดีต้อนรับสู่ห้องเรียน",detail["room"])
    print("อายุ",detail["age"])
    print("เพศ",detail["sex"])
    
info(name = "อรณิชชา", room = "คอมพิวเตอร์", age = 16 , sex = "หญิง")   