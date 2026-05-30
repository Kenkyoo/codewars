def last_digit(lst):
    if not lst:
        return 1
    result = 1
    for x in reversed(lst):
        result = x ** (n if n < 4 else n % 4 + 4)
    return n % 10

last_digit([3, 4, 2])