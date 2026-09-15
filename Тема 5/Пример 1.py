for i in range(3, 170):
    r = bin(i)[2:]
    sumr = str(r.count('1') % 2)
    r = r + sumr
    sumr = str(r.count('1') % 2)
    r = r + sumr
    if int(r, 2) > 170:
        print(i)
        break