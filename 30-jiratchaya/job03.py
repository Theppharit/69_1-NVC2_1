def WelcomeFamily(hello, *members):
    for mem in members:
        print(hello, mem)
        print("ยินดีต้อนรับสู่ความวุ่นวายของครอบครัวเรา")
        print("ขอให้มีความสุขกับครอบครัวเรานะ")
        print("------------------------")

WelcomeFamily("สวัสดีค่ะคุณ", "สมนึก", "สมใจ", "หมี", "โอเลี้ยง")