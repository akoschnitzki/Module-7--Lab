#Name- Alexander Koschnitzki
#Date- 11-11-21

#Problem 5

#In this problem, it is able to use a function to be able to
#use turtle to be able to create 5 squares that are in
#each square. It is able to create a smaller square each time and
#in that square.

import turtle

def drawSquare(t, sz):
    """Get Turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("Green")

alex = turtle.Turtle()
alex.color("Blue")
alex.penup()
alex.backward(5)
alex.pendown()

def fiveSquares(t, initial_size):
    for i in range(5):
        drawSquare(t, initial_size)
        initial_size+=20
        t.right(90)
        t.penup()
        t.forward(10)
        t.left(90)
        t.backward(10)
        t.pendown()


fiveSquares(alex, 20)

wn.exitonclick()

