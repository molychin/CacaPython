```
Created on Sat May 11 2019.05.13.20:42
@author: molychin@qq.com  
Teach Your Kids to Code  
```  

---
## **Teach Your Kids to Code 005**
### Conditions (What If?)

![](res/2019-5-16-19-26-27.png)

```python
answer = input("Do you want to see a spiral? y/n:")
if answer == 'y':
    print("Working...")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
print("Okay, we're done!")

```

|left=71|left=72|left=72.5|
|:---:|:---:|:---:|
|![](res/2019-5-16-20-31-22.png)|![](res/2019-5-16-20-32-26.png)|![](res/2019-5-16-20-36-01.png)|
|left=73|left=74|left=79|
|![](res/2019-5-16-20-33-24.png)|![](res/2019-5-16-20-28-55.png)|![](res/2019-5-16-20-44-48.png)|
|left=80|left=81|left=85|
|![](res/2019-5-16-20-43-19.png)|![](res/2019-5-16-20-46-38.png)|![](res/2019-5-16-22-22-03.png)|
|left=88|left=89|left=90|
|![](res/2019-5-16-22-24-22.png)|![](res/2019-5-16-19-29-07.png)|![](res/2019-5-16-19-52-04.png)|
|left=90.1|left=90.2|left=90.3|
|![](res/2019-5-16-19-55-54.png)|![](res/2019-5-16-20-00-16.png)|![](res/2019-5-16-20-00-16.png)|
|left=90.5|left=91|left=92|
|![](res/2019-5-16-19-54-23.png)|![](res/2019-5-16-19-40-13.png)|![](res/2019-5-16-19-50-14.png)|
|left=93|left=95|left=100|
|![](res/2019-5-16-20-04-33.png)|![](res/2019-5-16-19-45-31.png)|![](res/2019-5-16-20-07-23.png)|
|left=110|left=115|left=117|
|![](res/2019-5-16-20-14-47.png)|![](res/2019-5-16-20-17-58.png)|![](res/2019-5-16-20-19-26.png)|
|left=118|left=119|left=119.5|
|![](res/2019-5-16-20-25-10.png)|![](res/2019-5-16-20-20-55.png)|![](res/2019-5-16-20-26-33.png)|
|left=120|left=121|left=130|
|![](res/2019-5-16-20-16-43.png)|![](res/2019-5-16-22-33-03.png)|![](res/2019-5-16-22-42-00.png)|

最初的几步：  
left=89  
![](res/2019-5-16-22-46-52.png)


```python
# PolygonOrRosette.py
import turtle
t = turtle.Pen()
# Ask the user for the number of sides or circles, default to 6
number = int(turtle.numinput("Number of sides or circles",
             "How many sides or circles in your shape?", 6))
# Ask the user whether they want a polygon or rosette
shape = turtle.textinput("Which shape do you want?",
                         "Enter 'p' for polygon or 'r' for rosette:")
for x in range(number):
    if shape == 'r':        # User selected rosette
        t.circle(100)
    else:                   # Default to polygon
        t.forward (150)
    t.left(360/number)

```


```python
# RosettesAndPolygons.py - a spiral of polygons AND rosettes!
import turtle
t = turtle.Pen()
# Ask the user for the number of sides, default to 4
sides = int(turtle.numinput("Number of sides",
            "How many sides in your spiral?", 4))
# Our outer spiral loop for polygons and rosettes, from size 5 to 75
for m in range(5,75):   
    t.left(360/sides + 2)
    t.width(m//25+1)
    t.penup()        # Don't draw lines on spiral
    t.forward(m*4)   # Move to next corner
    t.pendown()      # Get ready to draw
    # Draw a little rosette at each EVEN corner of the spiral
    if (m % 2 == 0):
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    # OR, draw a little polygon at each ODD corner of the spiral
    else:
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)

```

![](res/2019-05-17-11-23-10.png)

![](res/2019-05-17-11-24-49.png)












>continue...  - p55
