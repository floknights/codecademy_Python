class Deque:
  def __init__(self):
    self.elements = []
  def add_first(self, item):
    self.elements.append(item)
    
  def add_last(self, item):
    self.elements.insert(0, item)
    
  def remove_first(self):
    return self.elements.pop()
    
  def remove_last(self):
    return self.elements.pop(0)
    
  def is_empty(self):
    if len(self.elements) > 0:
      return False
    return True
    
  def size(self):
    return len(self.elements)
    
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

popped_front = deque.remove_first()
print(popped_front)

popped_rear = deque.remove_last()
print(popped_rear)

print(deque.is_empty())

print(deque.size())

deque.display_deque()
