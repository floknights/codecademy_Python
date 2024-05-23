from functools import reduce

nums = (16, 2, 19, 22, 10, 23, 16, 2, 27, 29, 19, 26, 12, 20, 16, 29, 6, 2, 12, 20)

filtered_numbers = filter(lambda x: x % 2 == 0, nums)
print(tuple(filtered_numbers))

mapped_numbers = map(lambda x: x * 3, nums)
print(tuple(mapped_numbers))

sum = reduce(lambda x, y: x + y, nums)
print(sum)

nums2 = (2, 12, 5, 8, 9, 3, 16, 7, 13, 19, 21, 1, 15, 4, 22, 20, 11)

greater_than_10_doubled = map(lambda x: x * 2, filter(lambda y: y > 10, nums2))
print(tuple(greater_than_10_doubled))

functional_way = map(lambda x: x * 3, filter(lambda y: y % 3 == 0, nums2))
print(tuple(functional_way))
