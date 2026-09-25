from turtle import *
tracer(0)
koef = 20


up()
for x in range(-25, 25):
    for y in range(-25, 25):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()
answer = 288