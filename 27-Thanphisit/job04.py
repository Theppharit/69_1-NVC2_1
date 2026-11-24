def สูตรคำนวณฟิสิกส์วิถีปืนใหญ่(*num):
    print("คำตอบของคุณคือ")
    
    g = 9.81
    v0 = num[0]
    angle_degrees = num[1]
    
    pi = 3.141592653589793
    theta_rad = angle_degrees * (pi / 180.0)
    
    x = 2 * theta_rad
    x = x - (2 * pi) * int((x + pi) / (2 * pi))
    
    term = x
    sin_val = term
    n = 1
    while n < 10:
        term = -term * x * x / ((2 * n) * (2 * n + 1))
        sin_val += term
        n += 1
        
    total = (v0**2 * sin_val) / g
    print(round(total, 2))

สูตรคำนวณฟิสิกส์วิถีปืนใหญ่(100, 45)