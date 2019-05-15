# Rosette4.py
import turtle
t = turtle.Pen()
turtle.Turtle().screen.delay(0)   #绘画没有延迟
edges=16
for x in range(edges):    #4/6
    t.circle(100)
    t.left(360/edges)
