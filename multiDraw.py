'''
Author: Jon Angle

Draw with multiple turtles
'''
import turtle

def multiDrawCircle(turtles,circleSize):
  for i in range(361):
    for pen in turtles:
      pen.forward(0.1*circleSize)
      pen.left(1)

# initialize the turtles you want to draw with
fred = turtle.Turtle()
fred.color('black')
fred.speed(0)
sally = turtle.Turtle()
sally.color('blue')
sally.speed(0)
sally.right(90)
joe = turtle.Turtle()
joe.color('red')
joe.speed(0)
joe.left(90)
andy = turtle.Turtle()
andy.color('green')
andy.speed(0)
andy.right(180)

# initialize the array and parameters
turtles = (fred, sally, joe, andy)
circleSize = 10
spiralSize = 2

# function calls
for i in range(7):
  multiDrawCircle(turtles,circleSize)
  for pen in turtles:
    pen.left(50)

for i in range(22):
  multiDrawCircle(turtles,spiralSize*(i+1))
  for pen in turtles:
    pen.left(i)
