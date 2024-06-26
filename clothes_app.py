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


site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

from collections import defaultdict

validated_locations = defaultdict(lambda: 'TODO: Add to website')

validated_locations.update(site_locations)

for item in updated_products:
    site_locations[item] = validated_locations[item]

#print(site_locations)


from collections import ChainMap

year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

profit_map = ChainMap(*year_profit_data)

def get_profits(input_map):
    total_standard_profit = 0.0
    total_holiday_profit = 0.0

    for key in input_map.keys():
        if 'holiday' in key:
            total_holiday_profit += input_map[key]
        else:
            total_standard_profit += input_map[key]

    return total_standard_profit, total_holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

for item in new_months_data:
    profit_map = profit_map.new_child(item)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit

print(year_diff_standard_profit)
print(year_diff_holiday_profit)


from collections import Counter

opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

def find_amount_sold(opening, closing, item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)

  opening_count.subtract(closing_count)
  return opening_count[item]

tshirts_sold = find_amount_sold(opening_inventory, closing_inventory, 't-shirt')
print(tshirts_sold)


from collections import UserDict

data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

class OrderProcessingDict(UserDict):
  def clean_orders(self):
    to_del = []

    for key, val in self.data.items():
      if val['order_status'] == 'complete':
        to_del.append(key)

    for item in to_del:
      del self.data[item]

process_dict = OrderProcessingDict(data)

process_dict.clean_orders()
print(process_dict)


from collections import UserList
data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

class ListSorter(UserList):
  def append(self, item):
    self.data.append(item)
    self.data.sort()

sorted_list = ListSorter(data)
print(sorted_list)

sorted_list.append(2)
print(sorted_list)


from collections import UserString

str_name = 'python powered patterned products'
str_word = 'patterned '

class SubtractString(UserString):
  def __sub__(self, other):
    if other in self.data:
      self.data = self.data.replace(other, '')

subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)
