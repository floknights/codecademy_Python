binary_indexed_tree = [8, 13, 1, 4, 7, 23, -7, -7, 3, 17, 2, 23, 9]

prefix_sum10 = 0
prefix_sum4 = 0
range_sum = 0

i = 10
while i > 0:
  prefix_sum10 += binary_indexed_tree[i-1]
  i -= i&-i

i = 4
while i > 0:
  prefix_sum4 += binary_indexed_tree[i-1]
  i -= i&-i

range_sum = prefix_sum10 - prefix_sum4
