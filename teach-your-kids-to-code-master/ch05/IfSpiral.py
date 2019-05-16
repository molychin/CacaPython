#answer = input("Do you want to see a spiral? y/n:")
#if answer == 'y':
print("Working...")
import turtle
t = turtle.Pen()
turtle.Turtle().screen.delay(0)   #绘画没有延迟
t.width(2)
for x in range(100):
    t.forward(x*2)
    t.left(130)        #89/134
#print("Okay, we're done!")
