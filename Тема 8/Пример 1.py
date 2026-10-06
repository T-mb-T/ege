from itertools import product

count = 0
print(list(product("ТИМОФЕЙ", repeat=5)))
'''
for s in product("ТИМОФЕЙ", repeat=5):
    s = "".join(s)
    if s.count("Й") < 2 and "ЙИ" not in s and "ИЙ" not in s and s[0] != "Й" and s[-1] != "Й":
        count += 1
        print(s)
'''
print(count)