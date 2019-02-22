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
    
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)



mainloop()