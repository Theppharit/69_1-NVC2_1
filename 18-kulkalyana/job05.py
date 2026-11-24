def info(**detail) :
    print("สวัสดี คุณ" , detail["name"])
    print("ยินดีต้อนรับสู่ห้องเรียน", detail["room"])
    print("อายุ", detail ["age"])
    print("เพศ",detail["sex"])
    print("งานอดิเรก",detail ["make dessert"])
    
info(name = "กุลกัลยาณ์" , room = "คอมพิวเตอร์" ,age = 17 ,sex = "หญิง" , makedessert = "ทำขนม" )