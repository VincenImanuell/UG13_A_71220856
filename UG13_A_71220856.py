import turtle

t = turtle.Turtle()
t.pensize(12)
turtle.bgcolor('black')

def angka8():
    t.circle(23)
    t.penup()
    t.goto(0, -48)
    t.pendown()
    t.circle(25)
t.color('red')
angka8()

t.penup()
t.goto(0, 0)
t.forward(50)
t.pendown()

#angka5
t.color('yellow')
t.penup()
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.pendown()

t.left(180)
t.forward(40)
t.left(90)
t.forward(40)

t.penup()
t.forward(50)
t.pendown()

t.left(90)
t.forward(20)
t.circle(25, 180)
t.forward(20)

#angka6
t.color('green')
t.penup()
t.right(180)
t.forward(70)
t.pendown()

t.penup()
t.left(60)
t.forward(50)
t.pendown()

t.right(180)
t.forward(60)

t.circle(30)

#hurufI
t.color('blue')
t.penup()
t.left(120)
t.forward(80)
t.left(90)
t.forward(55)
t.left(90)
t.forward(10)
t.left(180)
t.pendown()
t.forward(20)

t.left(180)
t.forward(10)
t.left(90)
t.forward(100)

t.right(90)
t.forward(10)
t.right(180)
t.forward(20)

t.penup()
t.left(90)
t.forward(100)
t.left(90)
t.forward(293)
t.pendown()

#huruf v
t.right(180)
t.right(75)
t.forward(90)
t.left(150)
t.forward(90)

turtle.done()