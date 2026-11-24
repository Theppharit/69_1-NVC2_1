def info(**dataii) :
    print("ดีค้าบ คุณ", dataii["name"], "นามสกุล", dataii["lastname"],  dataii["age"], "อายุ", dataii["age"],"ยินดีต้อนรับเข้าสู่ห้องเรียน",dataii["room"],"ส่วนสูง",dataii["Tall"],"น้ำหนัก",dataii["weight"])
    
info(name = "pongphiphat", lastname = "Jurarom", age = 17, room = "วิทยะ", Tall = 182, weight = 68)