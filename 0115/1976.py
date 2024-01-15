t = int(input())

for i in range(t):
    t1, m1, t2, m2 = map(int, input().split())

    
    t3 = t1 + t2
    m3 = m1 + m2
    
    if t3 >= 24:
        t3 -= 24
    if t3 >= 13:
        t3 -=12
    if m3 >= 60:
        t3 += 1
        m3 -= 60
        if t3 >= 24:
            t3 -= 24
        elif t3 >= 13:
            t3 -=12 
    print(f"#{i+1} {t3} {m3}")
