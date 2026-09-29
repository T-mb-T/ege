from itertools import permutations, product

# Повторяющиеся символы в permutations
print(set(permutations('XXY')))

# Реализация чередования символов
odd = '13579'
even = '02468'
# 5-значные числа, где никакие две чётные или нечётные цифры не стоят рядом
for p in product(odd, even, odd, even, odd):
    print(''.join(p))