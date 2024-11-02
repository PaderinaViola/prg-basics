import turtle

def draw_square(length):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
    pen.hideturtle()
    pen.penup()
    pen.goto(-250, 200)
    pen.pendown()
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(3):
        pen.forward(length)
        pen.right(120)
    pen.hideturtle()
    pen.penup()
    pen.goto(-100, 200)
    pen.pendown()
    for _ in range(3):
        pen.forward(length)
        pen.right(120)

def draw_rectangle(length_a, lenght_b):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)
    pen.hideturtle()
    pen.penup()
    pen.goto(50, 300)
    pen.pendown()
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)
