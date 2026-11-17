def Myfriend(hello,*members) :
    for mem in members :
        print(hello, mem)
        print("วันนี้เป็นวันที่สดใส")
        print("ขอให้มีแต่เรื่องดีๆนะ")
        print("--------------------")
    
Myfriend("สวัสดีครับคุณ ", "นํ้ามนต์" ,"เบิร์ด","เก้า", "ติม", "ทอรุ้ง","สอง","วิว","ทศ","กาย","ฟลิม์")
def my_funtion (*numbers):
    total =0
    for num in numbers :
        total +  num
        return total 
    print (my_funtion)(5,6,7,8)
    def my_funtion(*num):
        print ("คําตอบของคุณ")
        total =0 
        total = ("num{0}+num{1}-num {2} * num {3}")
        print(total)
        my_funtion(2, 3, 4,5,6,7,8,9)