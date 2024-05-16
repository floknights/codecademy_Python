from tree import TreeNode
from collections import deque

def bfs(root_node, goal_value):
  path_queue = deque()
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  while path_queue:
    current_path = path_queue.pop()
    current_node = current_path[-1]
    print(f"Searching node with value: {current_node.value}")
    if current_node.value == goal_value:
      return current_path
    
    for child in current_node.children:
      new_path = current_path.copy()
      new_path.append(child)
      path_queue.appendleft(new_path)
    
  return None

sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

print(sample_root_node)

goal_path = bfs(sample_root_node, "Fluffy.jpg")
if goal_path is None:
  print("No path found")
else:
  print("Path found")
  for node in goal_path:
    print(node.value)
