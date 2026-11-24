def info(**details):
    print("สวัสดี คุณ" , details["name"])
    print("ยินดีต้อนรับสู่" , details["room"])
    print("คุณอายุ" , details["age"] , "ปี")
    print("คุณมีน้ำหนัก" , details["weight"] , "กิโลกรัม")
    print("คุณสูง" , details["height"] , "เซนติเมตร")
    print("คุณมีเพศ" , details["gender"])
    print("ขอบคุณที่ใช้บริการของเรา")

info(name="ฟิล์ม", room="ห้อง 1", age=20, weight=70, height=180, gender="ชาย")