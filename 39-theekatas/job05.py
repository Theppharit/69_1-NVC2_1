def info(**detail) :
    print("สวัสดี คุณ" ,detail["name"])
    print("คุณมีอายุ" ,detail["age"] , "ปี")
    print("คุณเรียนอยู่ที่" ,detail["school"])
    print("คุณมีความสามารถด้าน" ,detail["skill"])
    print("คุณเรียนอยู่ห้องเรียน" ,detail["room"])
info(name = "ทีฆทัศน์ ประทีปะเสน", age = 17, school = "อาชีวะศึกษานครราชสีมา", skill = "computer", room = "ช.2 ทด.1")