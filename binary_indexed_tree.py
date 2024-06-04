arr = [1, 8, -13, 4, 7, -6, 12, 14, 2, -8, 16, 3]
binary_indexed_tree = [1, 8, -13, 4, 7, -6, 12, 14, 2, -8, 16, 3]

for i in range(1, len(binary_indexed_tree) + 1):
  next = i + (i & -i)
  
  if next - 1 >= len(binary_indexed_tree):
    continue
    
  binary_indexed_tree[next - 1] += binary_indexed_tree[i - 1]

print(binary_indexed_tree) 
