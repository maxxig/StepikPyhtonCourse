import turtle
import time
def rectangle(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
def triangle(side):
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
def square(side):
    for j in range(3):
        turtle.left(90)
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)
#14.1-5
# def square2(side):
#     for j in range(4):
#         turtle.left(90)
#         for i in range(4):
#             turtle.forward(side)
#             turtle.left(90)
# square2(100)
# turtle.left(45)
# square2(100)


#14.16
# def hexagon(side):
#     for i in range(6):
#         turtle.forward(side)
#         turtle.left(60)
# hexagon(100)
#square(100)
#triangle(120)
time.sleep(3)
#rectangle(200,100)