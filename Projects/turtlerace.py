from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
userip = screen.textinput(title="Enter your guess", prompt="Enter which turtle can win the race")
print(userip)
colors = ["red", "green", "yellow", "purple", "blue", "orange"]
y_cor = [-150, -90, -30, 30, 90, 150]
turtle_list = []

if userip:
    game_is_on = True
else:
    game_is_on = False

for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-230, y=y_cor[i])
    turtle_list.append(t)  

while game_is_on:
    for each_turtle in turtle_list:
        dist = random.randint(0, 21)
        each_turtle.forward(dist)
        if each_turtle.xcor() > 230:
            winner_color = each_turtle.pencolor()
            if winner_color == userip:
                print(f"YOU WIN THE GUESS!! and the colour is {each_turtle.pencolor()}")
            else:
                print(f"YOU LOSE!!! WINNER TURTLE IS {each_turtle.pencolor()}")
            game_is_on = False
            break

screen.exitonclick()
