from turtle import *
from random import randint
speed(10)
penup()
goto(-140,140)
for step in range (6):
  write(step, align= 'center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
  ada = Turtle()
  ada.color('red')
  ada.shape('turtle')
  
  ada.penup()
  ada.goto(-160,100)
  ada.pendown()
  
  bob = Turtle()
  bob.color('blue')
  bob.shape('turtle')
  
  bob.penup()
  bob.goto(-160,70)
  bob.pendown()
  
  mac = Turtle()
  mac.color('orange')
  mac.shape('turtle')
  
  mac.penup()
  mac.goto(-160,40)
  mac.pendown()
  
  sam = Turtle()
  sam.color('green')
  sam.shape('turtle')
  
  sam.penup()
  sam.goto(-160,10)
  sam.pendown()
  
  mik = Turtle()
  mik.color('green')
  mik.shape('turtle')
  
  mik.penup()
  mik.goto(-160,-20)
  mik.pendown()
  
  
  for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    sam.forward(randint(1,5))
    mac.forward(randint(1,5))
    mik.forward(randint(1,5))


