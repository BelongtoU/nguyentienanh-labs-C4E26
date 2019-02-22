from turtle import*

def draw_square (lenght, color):
    s = Turtle()
    s.color(color)
    for _ in range(4):
        s.forward(lenght)
        s.left(90)

speed(0)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()


mainloop()