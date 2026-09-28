# Решение
from turtle import *
tracer(0)
koef = 15
for _ in range(7):
    forward(koef * 17)
    right(90)
    forward(koef * 26)
    right(90)
forward(koef * 4)
right(90)
forward(koef * 6)
left(90)
for _ in range(7):
    forward(koef * 30)
    right(90)
    forward(koef * 30)
    right(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * koef, y * koef)
        dot(3)

goto(0, 0)
exitonclick()





answer = 214

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 63, answer, '35495f83adcdab84ab446b313a3e0cb4'))