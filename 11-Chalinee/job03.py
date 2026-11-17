def WelcomeFriends(hello, *members):
    for mem in members:
        print(hello, mem)

    print("ดีใจที่ได้เจอเพื่อน ๆ ทุกคนนะ")
    print("ขอให้วันนี้เป็นวันที่ดีของทุกคน")

WelcomeFriends("สวัสดีครับคุณ", "อิ๋ง", "ติม", "วิว", "กันยา" ,"เก้า")