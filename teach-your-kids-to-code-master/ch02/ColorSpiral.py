# ColorSpiral.py
import turtle
t = turtle.Pen()
turtle.Turtle().screen.delay(0)   #绘画没有延迟 
turtle.bgcolor("black")

# You can choose between 2 and 6 sides for some cool shapes!
sides = 6
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(300):
    t.pencolor(colors[x%sides])
    t.forward(x * 2/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)

