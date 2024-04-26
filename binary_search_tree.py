def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"

  middle_index = len(my_list) // 2
  middle_value = my_list[middle_index]

  print("Middle index: {}".format(middle_index))
  print("Middle value: {}".format(middle_value))

  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[:middle_index])
  tree_node["right_child"] = build_bst(my_list[middle_index + 1:])

  return tree_node

sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)
