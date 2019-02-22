from turtle import*

def draw_star (x, y, lenght):
    penup()
    setpos(x, y)
    pendown()
    left(144)
    forward(lenght)
    for _ in range(4):
        right(144)
        forward(lenght)
    

mainloop()