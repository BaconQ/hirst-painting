import turtle as t 
import random

tom = t.Turtle()
tom.shape("turtle")
tom.color("green")
screen = t.Screen()
t.colormode(255)


color_list = [ (211, 154, 98), (53, 107, 131), (235, 240, 244), (177, 78, 33), (198, 142, 35), 
        (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), 
        (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), 
        (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), 
        (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210), 
        (61, 60, 72), (183, 190, 204), (78, 66, 42), (23, 99, 96) ]


pos_y = -200
tom.penup()
for _ in range(10):
    pos_y += 60
    tom.setposition(-260, pos_y)
    for _ in range(10):
        random_color = random.choice(color_list)
        tom.dot(30, random_color)
        tom.forward(60)

screen.exitonclick()
