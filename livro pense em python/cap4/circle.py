# Exercício circle
import turtle
import math

bob = turtle.Turtle()


def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    circunference = 2*math.pi*r
    n = 50
    length = circunference / n
    polygon(t, length, n)


circle(bob, 10)
turtle.mainloop()
