from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def is_inside(point):
    if (20 <= point[0] <= 120) and (60 <= point[1] <= 160):
        a = {
        'text': 'blue',
        'color': '#3F51B5',
        }
        return a
    if (140 <= point[0] <= 240) and (60 <= point[1] <= 160):
        a = {
        'text': 'red',
        'color': '#C62828',
        }
        return a
    if (20 <= point[0] <= 120) and (180 <= point[1] <= 280):
        a = {
        'text': 'yellow',
        'color': '#FFD600',
        }
        return a
    if (140 <= point[0] <= 240) and (180 <= point[1] <= 280):
        a = {
        'text': 'green',
        'color': '#4CAF50',
        }
        return a

def get_shapes():
    return shapes

def generate_quiz():
    text = choice(['green', 'blue', 'yellow', 'red'])
    color = choice(['#3F51B5', '#4CAF50', '#FFD600', '#C62828'])
    quiz_type = randint(0, 1)
    return [
        text, 
        color, 
        quiz_type
    ]

def mouse_press(x, y, text, color, quiz_type):
    
    if quiz_type == 0:
        if is_inside([x, y])['text'] == text:
            return True
        else:
            return False
    else:
        if is_inside([x, y])['color'] == color:
            return True
        else:
            return False 
