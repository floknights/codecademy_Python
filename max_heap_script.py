from random import randrange
from max_heap import MaxHeap 

max_heap = MaxHeap()

random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
  max_heap.add(el)

print(max_heap.heap_list)
