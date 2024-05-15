def linear_search(search_list, target_value):
  for index in range(len(search_list)):
    print(search_list[index])
    if search_list[index] == target_value:
      return index
  raise ValueError("{} not in list".format(target_value))

values = [54, 22, 46, 99]
print(linear_search(values, 22))
