```
Created on Sat May 11 23:17:01 2019  
@author: molychin@qq.com  
Teach Your Kids to Code  
```  

---  
## **Teach Your Kids to Code 002**
### Turtle Graphics:Drawing with Python

![](res/2019-5-12-21-59-14.png)

In this chapter, we’ll write short, simple programs to create beautifully complex visuals. To do this, we’ll use turtle graphics. In turtle graphics, you write instructions that tell a virtual, or imaginary, turtle to move around the screen. The turtle carries a pen, and you can instruct the turtle to use its pen to draw lines wherever it goes. By writing code to move the turtle around in cool patterns, you can make it draw amazing pictures.

在这一章中，我们将编写简短、简单的程序来创建漂亮、复杂的视觉图形。为此，我们将使用乌龟图形。在乌龟图形中，你写指令告诉一只虚拟的或虚构的乌龟在屏幕上移动。乌龟带着一支钢笔，你可以指示乌龟用它的钢笔在任何地方画线。通过编写代码以酷的模式移动乌龟，你可以让它画出令人惊叹的图片。

Using turtle graphics, not only can you create impressive visuals with a few lines of code, but you can also follow along with the turtle and see how each line of code affects its movement. This will help you understand the logic of your code.

使用Turtle图形，不仅可以用几行代码创建令人印象深刻的视觉图形，而且还可以跟随Turtle，查看每一行代码如何影响其移动。这将帮助您理解代码的逻辑。  

![](res/2019-5-12-22-18-52.png)  

##### 绘制方形螺旋
```python
# SquareSpiral1.py - Draws a square spiral
import turtle
t = turtle.Pen()
for x in range(100):
    t.forward(x)
    t.left(90)
```
![](res/2019-5-12-22-10-20.png)

>背景知识：Logo语言  
The Logo programming language was created in 1967 as an educational programming language, and five decades later, it’s still useful for learning the basics of coding. Cool, huh?  
![](res/2019-5-12-22-16-45.png)  
logo编程语言`【也称为海龟绘图】`创建于1967年，是一种教育性编程语言，五十年后，它仍然有助于学习编码的基础知识。很酷，是吧？  
python语言的内置类库包turtle正是模仿logo语言的绘图工具包，用法几乎和logo一样。

#### 绘制方形扭曲螺旋
```python
#SquareSpiral2.py
import turtle
t=turtle.Pen()
turtle.bgcolor('black')
colors=['red', 'yellow', 'blue', 'green']
for x in range(200):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
```
![](res/2019-5-12-22-59-00.png)

This is also a nice visual to help you understand how being off by just one number can drastically change the result of your program.  
这也是一个很好的视觉帮助你理解一个数字的微小改变是如何大幅度影响你程序的结果。

|left(87)|left(91)|
|:---:|:---:|
|![](res/2019-5-12-23-23-06.png)|![](res/2019-5-12-22-59-00.png)|
|left(93)|left(97)|
|![](res/2019-5-12-23-16-57.png)|![](res/2019-5-12-23-19-59.png)|

>大胆的猜想：我们真的很难预料这些简单的代码最终会绘制出如此美丽、协调的图形。更进一步，我们可以对比自然界中有不少类似的生物形态出现。很容易推测，这些神奇的自然形态是否也是由这些简单的生成规则来支配的。













>continue
