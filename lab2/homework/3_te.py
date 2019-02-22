from turtle import *

def draw_square (lenght, color):
    s = Turtle()
    s.color (color)
    for _ in range(4):
        s.forward(lenght)
        s.left(90)




mainloop()