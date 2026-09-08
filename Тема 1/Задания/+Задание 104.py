# Решение
from itertools import permutations
table = "16 61 17 71 23 32 25 52 26 62 34 43 37 73 45 54 56 65"
graph = "AC CA AE EA CF FC CG GC BG GB GF FG BD DB DE ED EF FE"

for p in permutations("ABCDEFG"):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)

answer = 14

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 104, answer, 'aab3238922bcc25a6f606eb525ffdc56'))