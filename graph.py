from graph_vertex import Vertex

class Graph():
  def __init__(self, directed = False):
    self.directed = directed
    self.graph_dict = {}

  def add_vertex(self, vertex):
    print("Adding {}".format(vertex.value))
    self.graph_dict[vertex.value] = vertex

grand_central = Vertex("Grand Central Station")

railway = Graph()

print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)
