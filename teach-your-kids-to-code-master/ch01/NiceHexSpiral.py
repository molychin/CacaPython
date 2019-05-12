#NiceHexSpiral.py
import turtle   

colors=['red', 'purple', 'blue',
        'green', 'yellow', 'orange']
t=turtle.Pen()
turtle.bgcolor('black')
#turtle.speed(0)
#turtle.Turtle().screen.delay(0)   #绘画没有延迟   

for x in range(300):
    t.pencolor(colors[x%6])
#    t.width(x/100+1)
#   t.forward(x)        
    t.forward(300)
    t.left(182)    #59/43/50/100/68/123/144

#turtle.done()
turtle.mainloop() 