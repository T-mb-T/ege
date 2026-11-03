def f(x, y, k1):
    if x == y:
        return k1 == 1
    if x > y:
        return 0
    return f(x + 1, y, k1) + f(x + 2, y, k1) + f(x * 2, y, k1 + 1) + f(x * 3, y, k1 + 1)

print(f(1, 10, 0))