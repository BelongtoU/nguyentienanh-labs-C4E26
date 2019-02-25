def is_inside (point, retangle):
    width = 100
    height = 200
    if 2 <= len(retangle) < 4:
        if (retangle[0] + width >= point[0] >= retangle[0]) and (retangle[1] + height >= point[1] >= retangle[1]):
            return True
        else:
            return False

    if len(retangle) == 4:
        if (retangle[0] + retangle[2] >= point[0] >= retangle[0]) and (retangle[1] + retangle[3] >= point[1] >= retangle[1]):
            return True
        else:
            return False
        
