# Решение
from turtle import *
'''
tracer(1)
koef = 5
x = 20

forward((x + 2) * koef)
for _ in range(4):
    forward(x * koef)
    right(90)
    forward((x + 2) * koef)
right(90)
forward(2 * x * koef)
for _ in range(4):
    right(90)
    forward((3 * x - 1) * koef)
tracer(False)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()
'''
for x in range(1,100):
    if ((11 * x) ** 2) - (2 * x) + 5 > 2000:
        print(x)
        break
answer = 14
#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 61, answer, 'aab3238922bcc25a6f606eb525ffdc56'))