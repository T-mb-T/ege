# Решение
from turtle import *
tracer(10)
koef = 15
for _ in range(2):
    forward(3 * koef)
    left(90)
    backward(12 * koef)
    left(90)
up()
backward(10 * koef)
right(90)
forward(8 * koef)
left(90)
down()
for _ in range(2):
    forward(16 * koef)
    right(90)
    forward(8 * koef)
    right(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * koef, y * koef)
        dot(3)

exitonclick()




answer = 185

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 6, answer, 'eecca5b6365d9607ee5a9d336962c534'))