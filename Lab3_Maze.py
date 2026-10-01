import turtle

screen = turtle.Screen()
screen.tracer(0)

mazeWidth=150

turtle.width(5)
turtle.hideturtle()

turtle.speed(0)

turtle.penup()
turtle.goto(-mazeWidth,190)


def drawMazeSection(color):
  turtle.color(color)
  turtle.pendown()
  turtle.forward(mazeWidth)
  turtle.penup()
  turtle.forward(40)
  turtle.pendown()
  turtle.forward(mazeWidth)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(mazeWidth)
  turtle.penup()
  turtle.forward(40)
  turtle.pendown()
  turtle.forward(mazeWidth)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  x,y = turtle.pos()
  turtle.penup()  
  turtle.goto(x, y-50)
  turtle.pendown()
  turtle.forward(30)
  turtle.penup()
  turtle.forward(40)
  turtle.pendown()
  turtle.forward(200)
  turtle.penup()
  turtle.forward(40)
  turtle.pendown()
  turtle.forward(30)
  turtle.penup()
  turtle.goto(x,y-110)

for color in ["#FF0000","#0000FF","#00FF00"]:
  drawMazeSection(color)

screen.tracer(1)    
