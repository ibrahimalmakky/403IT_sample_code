def count(current, max):
    print(current)
    # Recursion Termination condition
    if current < max:
        count(current+1, max)

# a and b are the starting values
# max is the max value to reach with the sequence
def fibonacci(a, b, max, lst=[]):
    c = a + b
    lst.append(b)
    if c < max:
        return fibonacci(b, c, max, lst)    
    else:
        return lst 

