import random
import time
import numpy as np
from matplotlib import pyplot as plt

etime = []

size = [10, 50, 100, 250, 500, 1000, 2500, 5000]

for s in size:
    data = np.random.random(s)

    start = time.time()

    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                t = data[j]
                data[j] = data[j + 1]
                data[j + 1] = t

    end = time.time()

    duration = end - start
    etime.append(duration * 10e5)

print(size)
print(etime)

plt.plot(size, etime, marker='o')
plt.xlabel("Input Size")
plt.ylabel("Execution time")
plt.title("Bubble sort time complexity")
plt.grid(True)
plt.show()