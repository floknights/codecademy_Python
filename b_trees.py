class BTreeNode():
  def __init__(self, t):
    self.keys = []
    self.children = []
    self.leaf = True
    self.t = t

  def split(self, parent, value):
    new_node = BTreeNode(self.t)
    
    split_key = self.keys[self._size // 2]
    parent.add_key(split_key)

    new_node.children = self.children[self._size // 2 + 1:]
    new_node.keys = self.keys[self._size // 2 + 1:]

    self.children = self.children[:self._size // 2 + 1]
    self.keys = self.keys[:self._size // 2]

    parent.children = parent.add_child(new_node)

    if value < split_key:
      return self
      
    return new_node

  @property
  def _is_leaf(self):
    return len(self.children) == 0

  @property
  def _is_full(self):
    return self._size == 2 * self.t - 1

  @property
  def _size(self):
    return len(self.keys)

  def add_key(self, value):
    for i in range(len(self.keys)):
      if value < self.keys[i]:
        self.keys.insert(i, value)
        
    else:
      self.keys.append(value)

  def add_child(self, new_node):
    new_node_first_key = new_node.keys[0]
    
    for i in range(len(self.children)):
      if new_node_first_key < self.children[i].keys[0]:
        return self.children[:i] + [new_node] + self.children[i:]

    return self.children + [new_node] 

class BTree:
  def __init__(self, t):
    self.t = t
    self.root = BTreeNode(t)

  def find_correct_child_node(self, node, value):
    i = 0
    
    while i < node._size and value > node.keys[i]:
      i += 1
      
    return node.children[i]

  def insert(self, value):
    node = self.root

    if node._is_full:
      new_root = BTreeNode(self.t)
      new_root.children.append(node)
      node = node.split(new_root, value) 
      self.root = new_root

    while node._is_leaf is False:
      child_node = self.find_correct_child_node(node, value)
      
      if child_node._is_full:
        node = child_node.split(node, value)
        
      else:
        node = child_node
        
    node.add_key(value)

  def search(self, value, node=None):
    if node is None:
      node = self.root
        
    if value in node.keys:
      return True
      
    elif node._is_leaf is True:
      return False
      
    else:
      child_node = self.find_correct_child_node(node, value)
      
    return self.search(value, child_node)

test1 = BTree(5)
test1.root.keys = [1, 2]

test1.insert(4)
print(test1.root.keys)
