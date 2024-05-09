from find_max_linkedlist import LinkedList

def find_max(linked_list):
  print("--------------------------")
  print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))
  current = linked_list.get_head_node()
  maximum = current.get_value()
  while current.get_next_node() != None:
    current = current.get_next_node()
    if current.get_value() > maximum:
      maximum = current.get_value()
  return maximum
  
ll = LinkedList(6)
ll.insert_beginning(32)
ll.insert_beginning(-12)
ll.insert_beginning(48)
ll.insert_beginning(2)
ll.insert_beginning(1)
print("The maximum value in this linked list is {0}\n".format(find_max(ll)))

ll_2 = LinkedList(60)
ll_2.insert_beginning(12)
ll_2.insert_beginning(22)
ll_2.insert_beginning(-10)
print("The maximum value in this linked list is {0}\n".format(find_max(ll_2)))

ll_3 = LinkedList("A")
ll_3.insert_beginning("X")
ll_3.insert_beginning("V")
ll_3.insert_beginning("L")
ll_3.insert_beginning("D")
ll_3.insert_beginning("Q")
print("The maximum value in this linked list is {0}\n".format(find_max(ll_3)))

runtime = "N"
print("The runtime of find_max is O({0})".format(runtime))


def sort_linked_list(linked_list):
  print("\n---------------------------")
  print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
  new_linked_list = LinkedList()
  while linked_list.get_head_node() != None:
    maximum = find_max(linked_list)
    new_linked_list.insert_beginning(maximum)
    linked_list.remove_node(maximum)
  return new_linked_list

ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_3).stringify_list()))

runtime = "N^2"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))
