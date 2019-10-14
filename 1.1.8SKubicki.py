import turtle as trtl 
drawer = trtl.Turtle()
drawer.speed(0)
drawer.pensize(5)
drawer.penup()
drawer.hideturtle()

#house body
drawer.goto(-200,-250)
drawer.pendown()
drawer.fillcolor("black")
count = 0
drawer.begin_fill()
while (count < 2):
    drawer.forward(400)
    drawer.left(90)
    drawer.forward(300)
    drawer.left(90)
    count += 1
drawer.end_fill()

'''drawer.penup()
drawer.goto(0,0)
drawer.pendown()
drawer.left(90)
drawer.forward(500)
drawer.right(90)'''
#house roof
drawer.penup()
drawer.goto(-210,50)
drawer.pendown()
drawer.pencolor("red")
drawer.fillcolor("red")
drawer.begin_fill()
drawer.forward(420)
drawer.left(140)
drawer.forward(274)
drawer.left(80)
drawer.forward(274)
drawer.end_fill()

#door
drawer.penup()
drawer.goto(-40,-250)
drawer.pendown()
drawer.pencolor("brown")
drawer.fillcolor("brown")
drawer.setheading(0)
count = 0
drawer.begin_fill()
while (count < 2):
    drawer.forward(80)
    drawer.left(90)
    drawer.forward(150)
    drawer.left(90)
    count += 1
drawer.end_fill()

#window
drawer.penup()
drawer.goto(90,-170)
drawer.setheading(-45)
drawer.pendown()
drawer.pencolor("blue")
drawer.fillcolor("blue")
drawer.begin_fill()
drawer.circle(50,360,4)
drawer.end_fill()

#chimney
drawer.penup()
drawer.goto(90,155)
drawer.pendown()
drawer.setheading(-40)
drawer.pencolor("black")
drawer.fillcolor("black")
drawer.begin_fill()
drawer.forward(40)
drawer.left(130)
drawer.forward(50)
drawer.left(90)
drawer.forward(31)
drawer.left(90)
drawer.forward(24)
drawer.end_fill()


#smoke

count = 1
while (count < 3):
    drawer.speed(0.75)
    drawer.penup()
    drawer.goto(90, 210)
    drawer.pendown()
    drawer.pencolor("grey")
    drawer.circle(20)

    drawer.penup()
    drawer.goto(110, 250)
    drawer.pendown()
    drawer.circle(20)

    drawer.penup()
    drawer.goto(100, 300)
    drawer.pendown()
    drawer.circle(20)

    drawer.penup()
    drawer.goto(90, 210)
    drawer.pendown()

    drawer.speed(0)
    drawer.penup()
    drawer.goto(90, 210)
    drawer.pendown()
    drawer.pencolor("white")
    drawer.circle(20)

    drawer.penup()
    drawer.goto(110, 250)
    drawer.pendown()
    drawer.circle(20)

    drawer.penup()
    drawer.goto(100, 300)
    drawer.pendown()
    drawer.circle(20)

    drawer.penup()
    drawer.goto(90, 210)
    drawer.pendown()

    '''count += 1'''




wn = trtl.Screen()
wn.mainloop()