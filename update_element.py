binary_indexed_tree = [12, 22, -5, 24, 3, 19, 1, 42, -15, -16, -5, -10, 4, 10, 9]

i = 1
diff = 14 - 12

while i <= len(binary_indexed_tree):
  binary_indexed_tree[i-1] += diff
  i = i + i&-i 
  
print(binary_indexed_tree)

i = 4
diff = 3 - 7

while i <= len(binary_indexed_tree):
  binary_indexed_tree[i-1] += diff
  i = i + i&-i 
  
print(binary_indexed_tree)
