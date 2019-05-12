import turtle
t=turtle.Pen()
turtle.bgcolor('black')
colors=['red', 'yellow', 'blue', 'green']
for x in range(200):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(147)    #87/91/93/97   /46/61/121/147



