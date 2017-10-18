while True:
    e = int(input())
    if e == 0:
        break

    m= e

    for z in range(e):
        k = e-z**3
        if k < 0:
            break
        y = int(k**(1.0/2.0))
        x= k-y**2
        m = min(m,x+y+z)
    print(m)
