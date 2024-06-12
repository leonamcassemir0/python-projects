# Exercício polygon
import turtle

bob = turtle.Turtle()


def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


polygon(bob, 4, 360)

turtle.mainloop()