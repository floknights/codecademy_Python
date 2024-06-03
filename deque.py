class Deque:
  def __init__(self):
    self.elements = []
  def add_first(self, item):
    self.elements.append(item)
    
  def add_last(self, item):
    self.elements.insert(0, item)
    
  def remove_first(self):
    pass
    
  def remove_last(self):
    pass
    
  def is_empty(self):
    pass
    
  def size(self):
    pass
    
  def peek_first(self):
    return self.elements[-1]
    
  def peek_last(self):
    return self.elements[0]
    
  def display_deque(self):
    print('\t | \t'.join(str(item) for item in self.elements))

deque = Deque()

deque.add_first(5)
deque.add_first(20)

deque.add_last(42)

deque.display_deque()
