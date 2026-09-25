# Решение
from itertools import permutations

table = "15 18 51 81 23 25 32 52 35 36 53 63 45 47 54 74 56 57 58 65 75 85 78 87"
graph = "AB BA BC CB AC CA DC CD DA AD EA AE EF FE FA AF FG GF GA AG GH HG AH HA"

for p in permutations("ABCDEFGH"):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
        if set(new_graph.split()) == set(graph.split()):
            print(p)





answer = 48

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 107, answer, '642e92efb79421734881b53e1e1b18b6'))