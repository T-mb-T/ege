# Решение
from turtle import *
tracer(0)
koef = 15
def main():
    for _ in range(2):
        forward(15 * koef)
        right(90)
        forward(8 * koef)
        right(90)
left(90)
main()
right(90)
up()
goto(-koef * 0.5, 8 * koef - 1)
down()
main()
up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()


answer = 56

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 64, answer, '9f61408e3afb633e50cdf1b20de6f466'))