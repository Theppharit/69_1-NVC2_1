def info(**detail):
    print("สวัสดี คุณ", detail["name"])
    print("นามสกุล", detail["lastname"])
    print("ชื่อเล่น", detail["nickname"])
    print("อายุ", detail["age"])
    print("ยินดีต้อนรับคร้าบบบ", detail["room"])

info(name="จิราพรรณ", room="วิทยะ3.1", nickname="ทอรุ้ง", lastname="จั่นช้อย", age="19")