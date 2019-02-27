from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    a = randint(1, 20)
    b = randint(1, 20)
    error = randint(-1, 1)
    op = choice(["+", "-", "*", ":"])
    if op == "+":        
        result = a + b + error
        return a, b, op, result
    if op == "-":
        result = a - b + error
        return a, b, op, result
    if op == "*":
        result = a * b + error
        return a, b, op, result
    if op == ":":
        result = a / b + error
        return a, b, op, result


def check_answer(x, y, op, result, user_choice):
    
    if user_choice == True:
        if op == "+":
            if result == x + y:        
                return True
            else:
                return False
        if op == "-":
            if result == x - y:
                return True
            else:
                return False
        if op == "*":
            if result == x * y:
                return True
            else:
                return False
        if op == ":":
            if result == x / y:
                return True
            else:
                return False

    if user_choice == False:
        if op == "+":        
            if result != x + y:
                return True
            else:
                return False
        if op == "-":        
            if result != x - y:
                return True
            else:
                return False
        if op == "*":        
            if result != x * y:
                return True
            else:
                return False
        if op == ":":        
            if result != x / y:
                return True
            else:
                return False
        
            
