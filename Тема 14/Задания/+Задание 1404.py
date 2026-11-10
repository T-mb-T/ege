# Решение
lou = []
from itertools import product
for x, y in product(range(37), repeat=2):
    chis = 1 * 37 ** 7 + 2 * 37 ** 6 + x * 37 ** 5 + 6 * 37 ** 4 + 4 * 37 ** 3 + 3 * 37 ** 2 + y * 37 ** 1 + 7
    if chis % 36 == 0:
        print(chis, f"{y * 37 + x}", f"{y}{x}")
        lou += [y * 37 + x]
print(max(lou))



answer = 1345

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1404, answer, '86109d400f0ed29e840b47ed72777c84'))