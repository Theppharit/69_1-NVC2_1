def info(**detail) :
    print("สวัสดี คุณ" ,detail["name"])
    print("คุณมีอายุ" ,detail["age"] , "ปี")
    print("คุณเรียนอยู่ที่" ,detail["school"])
    print("คุณเรียนอยู่ห้องเรียน" ,detail["room"])
info(name = "สรัลพร นวลมะเริง", age = 16, school = "อาชีวะศึกษานครราชสีมา", room = "ช.2 ทด.1")