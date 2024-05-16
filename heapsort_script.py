from heapsort import MaxHeap 

def heapsort(lst):
  sort = []
  max_heap = MaxHeap()
  
  for idx in lst:
    max_heap.add(idx)
    
  print(max_heap.retrieve_max())

my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
