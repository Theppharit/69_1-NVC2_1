def HappyMeeting(hello, *members):
    for mem in members:
        print(hello, mem)

    print("ขอต้อนรับทุกคนเข้าสู่กลุ่มของเรา")
    print("หวังว่าเราจะได้แบ่งปันเสียงหัวเราะร่วมกัน")

HappyMeeting("สวัสดีครับคุณ", "แอฟ", "กาย", "วิว", "กันยา", "เก้า")