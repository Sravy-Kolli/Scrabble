import turtle
t = turtle.Turtle()
def box(ln):
    for i in range(4):
        t.forward(ln)
        t.rt(90)
t.speed(0)
x = 0
y = 0
while True:
    t.goto(x,y)
    t.pendown()
    x += 20
    box(20)
    if x >= 20*15:
        x = 0
        y += 20
        t.penup()
    if y>= 20 * 15:
        break
turtle.done()


