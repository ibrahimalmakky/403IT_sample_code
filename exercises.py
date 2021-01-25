# Arithmetic Order
x = 5
y = 8
z = 15
a = x * (y + z)
print(a)
# ----------------
print(x**5)
# ----------------
my_list = [x for x in range(0,10)]
print(my_list)
x = 0
my_list = []
while x < 10:
    my_list.append(x)
    x += 1
print(my_list)
# ----------------
my_tuple_list = [(x, y) for x in range(0,10) for y in range(0, 5) if x%2 == 0]
print(my_tuple_list)
my_tuple_list = []
for x in range(0,10):
    for y in range(0,5):
        if x%2 == 0:
            my_tuple_list.append((x, y))
print(my_tuple_list)
# ----------------
another_list = [x*y for x in range(1,5) for y in range(5,1,-1) if (x*y)%2 == 0]
print(another_list)
# ----------------
yet_another_list = [[x,y,x**2,y**2] for x in range(1,5) for y in range(1,5)]
print(type(yet_another_list[0]))
# ----------------