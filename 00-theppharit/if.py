price = int(input("กรุณากรอกจำนวนเงิน : "))

if price >= 899 :
    print("เมนูพรีเมียม")
elif price >= 499 :
    print("เมนูชั้นดี")
elif price >= 199 :
    print("เมนูทั่วไป")
else :
    print("กรุณากลับมาใหม่ภายหลัง")
