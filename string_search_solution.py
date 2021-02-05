import time

# Get the index of the word in a list
def find_strs(search_for, search_in):
    inds = []
    for i in range(len(search_in)):
        if search_in[i] in search_for:
            inds.append(i)
    return inds

def find_str(search_for, search_in):
    for i in range(len(search_in)):
        if search_in[i] == search_for:
            return i

my_file = open("name_challenge.txt", "r")
search_string = my_file.read()
split_string = search_string.split(" ")

names = ["Herbert", "Weronika", "Kasia"]
tic = time.perf_counter()
print(find_str(names, split_string))
toc = time.perf_counter()
print(toc-tic)

tic = time.perf_counter()
for name in names:
    print(find_str(name, split_string))
toc = time.perf_counter()
print(toc-tic)