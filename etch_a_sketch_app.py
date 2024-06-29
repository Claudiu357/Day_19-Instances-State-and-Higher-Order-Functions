from turtle import Turtle, Screen


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_right():
    t.setheading(t.heading() + 10)


def move_left():
    t.setheading(t.heading() - 10)


t = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="d", fun=move_left)
screen.exitonclick()