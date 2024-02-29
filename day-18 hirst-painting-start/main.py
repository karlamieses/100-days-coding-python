import turtle as t
from random import choice


color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]


painting = t.Turtle()
t.colormode(255)
painting.hideturtle()
painting.penup()

#sample

def draw_painting(vertical):
    painting.goto(-225, vertical)
    for _ in range(10):
        painting.dot(20, choice(color_list))
        painting.penup()
        painting.forward(50)
        painting.pendown()
        painting.penup()


move_up = -225

for _ in range(10):
    draw_painting(move_up)
    move_up += 50


t.mainloop()



