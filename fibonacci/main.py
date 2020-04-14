def fibonacci(maximum):
    """
    Get max paramertized Fibonacci
    """
    fib = []
    a = 1
    b = 0
    c = None
    d = 1
    while a < maximum:
        c = a
        a = b + a 
        b = c 
        if a % 2 != 0:
            d += a
    fib.append(d)
    return fib
print(fibonacci(22))