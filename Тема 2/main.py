from itertools import product
"""
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # Важный момент! Т.к. функция возвращает 0 в условии задачи, то всё выражение помещаем под not
                if not((not(z) == y) <= ((w and not(x)) == (y and x))):
                    print(x, y, z, w)
"""
print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if not((not(z) == y) <= ((w and not(x)) == (y and x))):
        print(x, y, z, w)