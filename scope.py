h = 300

def multiply(x, y):
    global h
    h = 100
    def add(x1, y1):
        # local scope value for h will be used
        return x1 + y1 + h
    print(add(x, y))
    return (x*y)

# Global scope value
print(h)

print(multiply(5,3))

print(h)
