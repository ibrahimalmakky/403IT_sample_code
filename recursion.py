def count(current, max):
    print(current)
    # Recursion Termination condition
    if current < max:
        count(current+1, max)

def fibonacci(a, b, max):
    c = a + b
    print(b)
    if c < max:
        fibonacci(b, c, max)        

print(0)
fibonacci(0, 1, 100)
