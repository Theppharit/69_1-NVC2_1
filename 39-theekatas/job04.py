def my_funtion(*num):
    print("ผลการคำนวนระยะของการเบรกรถยนต์")
    total = num[0] * num[0] / (2 * num[1])
    print(total)
    
my_funtion(100, 5)