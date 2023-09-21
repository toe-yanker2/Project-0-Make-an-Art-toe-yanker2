import turtle
import math

## All three variables can take any value! ##

# At what angle the arms are:
armAngle = 20

# Length of the nose:
noseLength = 30

# The higher the first number is, the faster the program goes (0 is instantaneous though):
turtle.tracer(1, 0)

'turtle.bgcolor("#131862")'


# Move the turtle without that nasty pen getting in the way
def turtleMove(x, y):
  turtle.up()
  turtle.goto(turtle.xcor()+x, turtle.ycor()+y)
  turtle.down()

# Draws a circle
# degrees: how much of the circle it draws, from 0 to 360
# dir: 1 for turning right, -1 for turning left
def drawCircle(degrees, size, dir):
  if (degrees > 100):
    turtle.begin_fill()
  for i in range(int(degrees/4)):
    turtle.forward(size*2)
    turtle.right(dir*4)
  turtle.end_fill()

# Draws a rectangle
# middle: allows for drawing from the middle of the first side
def drawRectangle(side1, side2, middle, dir):
  turtle.begin_fill()
  turtle.forward(side1-middle)
  turtle.right(dir*90)
  turtle.forward(side2)
  turtle.right(dir*90)
  turtle.forward(side1)
  turtle.right(dir*90)
  turtle.forward(side2)
  turtle.right(dir*90)
  turtle.forward(middle)
  turtle.end_fill()

def drawArm(x, y, dir):
  turtle.begin_fill()
  turtle.right(90*dir)
  turtle.forward(5)
  turtle.left(90*dir)
  turtle.forward(30)
  turtle.right(40*dir)
  for i in range(2):
    turtle.forward(20)
    turtle.left(170*dir)
    turtle.forward(20)
    turtle.right(125*dir)
  turtle.forward(20)
  turtle.left(170*dir)
  turtle.forward(20)
  turtle.right(40*dir)
  turtle.forward(30)
  turtle.end_fill()
  turtle.goto(x, y)

# First circle
turtle.fillcolor("#FFFFFF")
turtleMove(0, -30)
drawCircle(360, 1.3, 1)
# Arms
'turtle.fillcolor("#964B00")'
turtleMove(20, 20)
turtle.left(armAngle)
drawArm(turtle.xcor(), turtle.ycor(), 1)
turtleMove(-40, 0)
turtle.right(armAngle*2)
drawArm(turtle.xcor(), turtle.ycor(), -1)
turtleMove(20, -20)
turtle.left(armAngle)
# Second Circle
'turtle.fillcolor("#AAAAAA")'
turtleMove(0, -7)
drawCircle(360, 1, -1)
drawCircle(180, 1, -1)
# Third Circle
turtleMove(0, -7)
drawCircle(360, .8, 1)
drawCircle(180, .8, 1)
# Hat
turtleMove(0, -6)
'turtle.fillcolor("#303030")'
drawRectangle(50, 10, 25, -1)
turtleMove(0, 10)
drawRectangle(30, 35, 15, -1)
# Buttons
turtleMove(0, -25)
drawCircle(360, .1, -1)
turtleMove(13, 0)
drawCircle(360, .1, -1)
turtleMove(-8, -40)
drawCircle(360, .1, -1)
turtleMove(0, -12.5)
drawCircle(360, .1, -1)
turtleMove(0, -12.5)
drawCircle(360, .1, -1)
turtleMove(8, 65)
# Carrot nose
noseSideLength = math.sqrt(25+(noseLength**2))
noseAngle = 90-math.degrees(math.atan(noseLength/5))
turtleMove(-7, -2)
'turtle.fillcolor("#FF5733")'
turtle.begin_fill()
turtle.right(noseAngle)
turtle.forward(noseSideLength)
turtle.right(180-noseAngle*2)
turtle.forward(noseSideLength)
turtle.end_fill()
turtle.left(140-noseAngle)
# Smile
turtleMove(-15, 2)
drawCircle(55, .7, -1)
turtleMove(100, 0)

turtle.update()