def last_digit(n1, n2):
    if n2 == 0:
        return 1
    x = n1 % 10
    y = n2 % 4
    if y == 0:
        y = 4
    r = x ** y % 10
    return r
    
last_digit(9, 7)