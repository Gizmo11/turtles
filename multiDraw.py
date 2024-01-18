'''
Author: Jon Angle

Draw with multiple turtles
'''
import turtle

# initialize the turtles you will draw with
def initializeTurtles():
  # fred = turtle.Turtle()
  fred = turtle.Pen()
  fred.color('yellow')
  # sally = turtle.Turtle()
  sally = turtle.Pen()
  sally.color('blue')
  # joe = turtle.Turtle()
  joe = turtle.Pen()
  joe.color('red')
  # andy = turtle.Turtle()
  andy = turtle.Pen()
  andy.color('green')
  # initialize the arrays and parameters
  turtles = (fred, sally, joe, andy)
  for mph in turtles:
    mph.speed(200)
    mph.width(2)
    # mph.shape('turtle')  # Possible turtle shapes arrow, circle, classic, square, triangle, turtle, blank
  # initialize starting angles
  sally.right(90)
  joe.left(90)
  andy.right(180)
  return turtles

def multiDrawCircle(turtles,circleSize):
  for i in range(361):
    for pen in turtles:
      pen.forward(0.1*circleSize)
      pen.left(1)

def toroid(speed):
  turtles = initializeTurtles()
  circleSize = 50
  for i in range(7):
     if speed == 0:
       multiDrawCircle(turtles,circleSize)
     for pen in turtles:
      if speed == 1:
        pen.circle(circleSize)
      pen.left(50)
  turtle.exitonclick()

def spiral(speed):
  turtles = initializeTurtles()
  spiralSize = 5
  for i in range(22):
    if speed == 0:
      multiDrawCircle(turtles,spiralSize*(i+1))
    for pen in turtles:
      if speed == 1:
        pen.circle(spiralSize * i)
      pen.left(i)
  turtle.exitonclick()

def angularHelix():
  colors = ["red", "purple", "blue", "green", "orange", "yellow"]
  t = turtle.Pen()
  turtle.bgcolor("black")
  t.speed(200)
  for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
  turtle.exitonclick()

def main():
  # User Input
  shape = int(input("Pick a shape: (0= Spiral, 1 = Toroid, 2 = Helix): "))
  if shape == 0 or shape == 1:
    speed = int(input("Pick how fast the turtle will draw: (0 = Slow, 1 = Fast): "))
  if shape == 1:
    toroid(speed)
  elif shape == 0:
    spiral(speed)
  elif shape == 2:
    angularHelix()
  else:
    print("You didn't enter the shape parameter correctly.")

main()