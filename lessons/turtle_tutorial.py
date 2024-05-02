from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(45,60)
leo.pendown()
colormode(255)
leo.color(99, 204, 250)

leo.begin_fill()
i: int = 0
while (i<3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()

bob.speed(20)
bob.color(0, 0, 0)
bob.pencolor("black")
leo.penup()
leo.goto(45,60)
leo.pendown()

k: int = 0
while (k<3):
    leo.forward(300)
    leo.left(120)
    k += 1

done()