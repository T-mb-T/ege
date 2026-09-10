# Решение
from itertools import permutations

table = "15 51 16 61 26 62 27 72 29 92 35 53 37 73 38 83 48 84 49 94 58 85 67 76"
graph = "АБ БА АГ ГА АЕ ЕА ГЕ ЕГ ЕЖ ЖЕ ЖИ ИЖ ИК КИ КД ДК ДВ ВД ДГ ГД ВБ БВ КВ ВК"

for p in permutations("АБВГДЕЖИК"):
    new_graph = table
    for i in range(1, 10):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)

answer = 37
#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 105, answer, 'a5bfc9e07964f8dddeb95fc584cd965d'))