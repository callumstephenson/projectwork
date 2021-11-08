def euler2(limit):
    sum, x, y = 0, 1, 1
    while x+y <= limit:
        x,y = y, x+y
        if y % 2 == 0:
            sum += y
    return sum