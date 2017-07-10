from turtle import * 
# This is a function that draws a shape
def drawshape(self, sides, angle):
    self.color("yellow")
    self.begin_fill()
    while sides > 0:
        self.pencolor("coral")
        self.forward(100)
        self.right(angle)
        sides = sides - 1
    self.end_fill()

win = Screen()
win.bgcolor("white")
sides = int(input('Enter # of sides:'))
t = Turtle()
#setup(500,300)
angle = 360/sides
print ("angle %d" %angle)
drawshape(t, sides, angle)
win.exitonclick()
