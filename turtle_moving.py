import turtle
turtle.shape("turtle")

def move_w():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)

def move_a():
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50)

def move_s():
    turtle.setheading(-90)
    turtle.stamp()
    turtle.forward(50)

def move_d():
    turtle.setheading(360)
    turtle.stamp()
    turtle.forward(50)

def end_escape():
    turtle.reset()

turtle.onkey(move_w, 'w')
turtle.onkey(move_a, 'a')
turtle.onkey(move_s, 's')
turtle.onkey(move_d, 'd')

turtle.onkey(end_escape, 'Escape')
turtle.listen()
    
