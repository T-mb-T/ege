for x in "0123456789ABCDEFG":
    x1 = int(f"AB{x}12", 17)
    x2 = int(f"4E{x}3F", 17)
    x3 = x1 + x2
    if x3 % 16 == 0:
        print(x, x3 // 8)