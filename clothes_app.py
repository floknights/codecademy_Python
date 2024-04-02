from helper_functions import process_csv_supplies
from collections import deque

csv_data = process_csv_supplies()[1:]

supplies_deque = deque()

for item in csv_data:
  if item[2] == 'important':
    supplies_deque.appendleft(tuple(item))
  else:
    supplies_deque.append(tuple(item))

ordered_important_supplies = deque()
for _ in range(25):
  ordered_important_supplies.append(supplies_deque.popleft())

ordered_unimportant_supplies = deque()
for _ in range(10):
  ordered_unimportant_supplies.append(supplies_deque.pop())


clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

from collections import namedtuple

ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

new_coat = ClothingItem('coat', 'black', 'small', 14.99)

coat_cost = new_coat.price

updated_clothes_data = []
for item in clothes:
  updated_clothes_data.append(ClothingItem(*item))
#print(updated_clothes_data)
