class Hamiltonian:
  def __init__(self, vertices, adjacency_matrix, starting_vertex):
    self.vertices = vertices
    self.adj_matrix = adjacency_matrix
    self.start = starting_vertex
    
    self.path = []
    self.visited_vertices = [0 for x in range(len(self.vertices))]

    self.hpaths = []
    self.cycles = []
    self.num_vertices = len(self.vertices)

  def traverse(self):
    self.path.append(self.start)
    self.search(self.start)

  def search(self, vertex):
    all_visited = True
    
    for i in range(1, len(self.visited_vertices)):
      if self.visited_vertices[i] == 0:
        all_visited = False
        break

    if all_visited and len(self.path) == len(set(self.path)):
      self.hpaths.append(list(self.path))

    if vertex == self.start and len(self.path) == self.num_vertices + 1:
      self.cycles.append(list(self.path))
      return

    for neighbor in range(len(vertices)):

      if self.adj_matrix[vertex][neighbor] == 1 and self.visited_vertices[neighbor] == 0:
        self.visited_vertices[neighbor] = 1
        self.path.append(neighbor)
        self.search(neighbor)
        self.visited_vertices[ neighbor ]=0
        self.path.pop()

vertices = ['School', 'Sanjay', 'Marquis', 'Marisol', 'Lisa']
adjacency_matrix = [
                    [0, 1, 0, 0, 1],
                    [1, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0]
                  ]
ham = Hamiltonian(vertices, adjacency_matrix, 0)
ham.traverse()

print("Hamiltonian paths:" + str(ham.hpaths))
print("Hamiltonian cycles:" + str(ham.cycles))
