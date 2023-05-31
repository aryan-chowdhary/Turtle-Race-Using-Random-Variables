import turtle
import random

scr = turtle.Screen()
scr.title("Turtle Race")
t = turtle.Turtle()
t.speed(36)
t.pu()
t.goto(-500,280)
t.pd()
t.write("Turtle Race", font=("Arial Black", 36, "normal"))
t.pu()
t.goto(-500,250)
a = 0
t.right(90)
for i in range(15):
    t.write(a)
    for j in range(8):
        t.forward(12)
        t.pd()
        t.forward(12)
        t.pu()
    t.backward(192)
    t.left(90)
    t.forward(36)
    t.right(90)
    a+=1
t.hideturtle()

r = turtle.Turtle()
r.color("black")
r.shape("turtle")
b = turtle.Turtle()
b.color("violet")
b.shape("turtle")
g = turtle.Turtle()
g.color("lime")
g.shape("turtle")
y = turtle.Turtle()
y.color("cyan")
y.shape("turtle")
p = turtle.Turtle()
p.color("crimson")
p.shape("turtle")

axis = 200
flag = 0

star = turtle.Turtle()
star.speed(12)
star.hideturtle()

for k in (r,b,g,y,p):
    k.pu()
    k.goto(-524,axis)
    for k2 in range(5):
        k.right(72)
    axis-=24
t.pu()
t.goto(-500,0)
t.pd()
while flag == 0:
    for l in (r,b,g,y,p):
        if l.xcor() >= -14:
            l.forward(40)
            xw = l.xcor()
            yw = l.ycor()
            star.pu()
            star.goto(xw,yw)
            star.pd
            flag = 1
            t.left(90)
            zzz = l.color()[0]
            star.fillcolor(zzz)
            star.color(zzz)
            star.right(90)
            star.forward(18)
            star.left(90)
            star.forward(14)
            star.right(180)
            for op in range(6):
                star.showturtle()
                star.pu()
                star.forward(24)
                star.pd()
                star.right(60)
                star.begin_fill()
                for op2 in range(5):
                    star.forward(8)
                    star.right(144)
                star.end_fill()
            star.hideturtle()
            t.showturtle()
            t.write((str(zzz)).upper(), font=("Arial Black", 24, "normal"))
            t.right(90)
            t.pu()
            t.forward(36)
            t.pd()
            t.left(90)
            t.write("WINS!", font=("Arial", 24, "normal"))
            t.hideturtle()
            break
        else:
            l.pd()
            speed = random.randint(4,10)
            l.speed(12)
            l.forward(speed)

scr.exitonclick()