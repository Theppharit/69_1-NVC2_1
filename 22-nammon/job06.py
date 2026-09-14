
number = int(input("กรุณากรอกตัวเลขแม่สูตรคูณ: "))


count = 1


while count <= 12:
    result = number * count
    print(number, "x", count, "=", result * count)
    count += 1