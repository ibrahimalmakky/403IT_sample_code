import time

# Time Complexity for nesting loops
counter = 0
for i in range(0, 100):
    tic = time.perf_counter()
    for j in range(0, 100):
        for z in range(0, 100):
            for x in range(0, 100):
                for l in range(1, 100):
                    counter += 1
    toc = time.perf_counter()
    print(toc-tic)
print(counter)