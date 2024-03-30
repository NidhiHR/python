#press w to move turtle to forward by 10 steps,z to move backward,a to turn left,s to turn right and c to clear screen

from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move():
    tim.forward(40)

def back():
    tim.backward(40)

def anticlock():
    tim.right(15)

def clock():
    tim.left(15)


def clear():
    tim.reset()

screen.listen()
screen.onkey(key="w",fun=move)
screen.onkey(key="z",fun=back)
screen.onkey(key="s",fun=anticlock)
screen.onkey(key="a",fun=clock)
screen.onkey(key="c",fun=clear)
screen.exitonclick()