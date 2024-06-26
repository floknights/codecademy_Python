import csv
from collections import namedtuple
from functools import reduce

tree = namedtuple("tree", ["index", "width", "height", "volume"])

with open('trees.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  next(reader) # skip the first line in trees.csv that contains the data lablels

  mapper = map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)

  #trees = tuple(mapper)
  #print(trees)

  t = filter(lambda q: q[2] > 75, map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)) # filter trees with a height over 75
  trees = tuple(t)

  widest = reduce(lambda x, y: x if x.width > y.width else y, trees) # widest tree with a height over 75
  print(widest)
