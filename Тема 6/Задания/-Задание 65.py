# Решение
from turtle import *
tracer(False)
koef = 15
for _ in range(2):
    forward(koef * 23)
    right(90)
    forward(koef * 10)
    right(90)
forward(koef * 3)
left(90)
forward(koef * 12)
right(90)
for _ in range(2):
    forward(koef * 9)
    right(90)
    forward(koef * 32)
    right(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()




answer = 132

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 65, answer, '5f93f983524def3dca464469d2cf9f3e'))