# def MyFamily(hello,*members) :
#     for mem in members :
#         print(hello, mem)
#         print("ยินดีต้อนรับสู่ครอบครัวของเรา")
#         print("ขอให้มีความสุขมาก ๆ นะ")
#         print("--------------------")
    
# MyFamily("สวัสดีครับคุณ ", "บ๊อบ" ,"เบิร์ด","โบ๊ท", "เบส", "บาส")

# def my_funtion(*numbers) :
#     total = 0
#     for num in numbers :
#         total += num
#     return total

# print(my_funtion(5,8,7))

def my_funtion(*num) :
    print("คำตอบของคุณคือ")
    total = 0
    total = (num[0]+num[1]-num[2])*num[3]
    print(total)
    
my_funtion(2,3,1,5)