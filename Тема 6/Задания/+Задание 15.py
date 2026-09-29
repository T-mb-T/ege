# Решение
from turtle import *
tracer(False)
koef = 20
for _ in range(4):
    forward(koef * 14)
    right(90)
for _ in range(5):
    forward(koef * 5)
    right(45)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()




answer = 59

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 15, answer, '093f65e080a295f8076b1c5722a46aa2'))