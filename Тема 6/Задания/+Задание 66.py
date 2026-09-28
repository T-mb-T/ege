# Решение
from turtle import *
tracer(0)
koef = 25
for _ in range(4):
    forward(koef * 9)
    right(90)
for _ in range(3):
    forward(koef * 9)
    right(120)
up()
for x in range(-15, 15):
    for y in range(-15, 15):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()

answer = 34

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 66, answer, 'e369853df766fa44e1ed0ff613f563bd'))