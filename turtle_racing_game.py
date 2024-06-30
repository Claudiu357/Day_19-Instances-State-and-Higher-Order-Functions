from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Witch turtle will win the race?Enter color: ")
colors = ["red", 'blue', 'yellow', 'green', 'purple', 'orange']
is_race_on = False
y_pos = -100
all_turtles = []
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y= y_pos)
    y_pos += 30
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_input:
                print(f"You won! The winner color is {winner}")
            else:
                print(f"You lose the inner color is {winner}")

screen.exitonclick()