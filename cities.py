import json
from collections import namedtuple
from functools import reduce

city = namedtuple("city", ["name", "country", "coordinates", "continent"])

with open('cities.json') as json_file:
  data = json.load(json_file) 

cities = map(lambda x: city(x["name"], x["country"], x["coordinates"], x["continent"]), data["city"])

asia = tuple(filter(lambda q: q[3] == "Asia", cities)) # cities in Asia
print(asia)

west = None

west = reduce(lambda x, y: x if x < y else y, asia) # western-most country in Asia
print(west)
