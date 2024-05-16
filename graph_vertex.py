class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex):
    print("Adding edge to {}".format(vertex))
    self.edges[vertex] = True

  def get_edges(self):
    return list(self.edges.keys())
  
grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')

print(grand_central.get_edges())

grand_central.add_edge(forty_second_street.value)

print(grand_central.get_edges())
