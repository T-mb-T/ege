# Решение
from itertools import permutations
table = "15 51 16 61 24 42 25 52 26 62 28 82 37 73 38 83 45 54 47 74 48 84 56 65 78 87"
graph = "АБ БА АГ ГА АЕ ЕА ГЕ ЕГ ГБ БГ ГЖ ЖГ ЖБ БЖ ДЖ ЖД ДИ ИД ЖИ ИЖ ИВ ВИ ВД ДВ БД ДБ"

for p in permutations("АБВГДЕЖИ"):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)



answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 106, answer, '1f0e3dad99908345f7439f8ffabdffc4'))