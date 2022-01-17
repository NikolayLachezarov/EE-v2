from testing_algorthims import Algorithms

import time
import sys


hello = Algorithms()
lst = []
memory = 0
sum = 0


for i in range(100):
    start = time.time()
    hello.heapSort([3, 5, 6, 2, 1])
    end = time.time()
    lst.append(end-start)
    memory += sys.getsizeof(hello.heapSort([3, 5, 6, 2, 1]))

    sum += end-start

print(sum / len(lst))
# measures this in bites
print(memory / len(lst))
