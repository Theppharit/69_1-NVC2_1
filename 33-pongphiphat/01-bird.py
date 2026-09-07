score =float(input("กรุณากรอกคะเเนนของนักเรียน:"))

if score >= 80:
    grade ="A"
elif score >=70:
    grade ="B"
elif score >=60:
    grade ="C"
elif score >=50:
    grade ="D"
else:
    grade ="A"
print(f"คะเเนนที่คุณได้{score} เกรดที่คุณได้{grade}")