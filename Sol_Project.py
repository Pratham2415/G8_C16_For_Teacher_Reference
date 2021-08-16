import turtle

turtle.shape("turtle")
turtle.width(4)
turtle.penup()
turtle.goto(0,60)
turtle.pendown()
colors=["red","green","blue","yellow","purple"]

for i in range(5):
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(130)
    turtle.right(120)
    turtle.forward(130)
    turtle.right(120)
    turtle.forward(130)
    turtle.right(72)
    turtle.end_fill()
turtle.ht()