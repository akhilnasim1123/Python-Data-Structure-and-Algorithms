class graph:
    def __init__(self, size):
        self.size = size
        self.vertex = []
        self.graph = []

    def add_vertex(self, v):
        if v in self.vertex:
            pass
        else:
            self.vertex.append(v)
            temp = []
            for i in range(self.size):
                temp.append(0)
            self.graph.append(temp)

    def add_edges(self, v1, v2, e):
        l1 = self.vertex.index(v1)
        l2 = self.vertex.index(v2)
        self.graph[l1][l2] = e

    def remove_edges(self, v1, v2):
        l1 = self.vertex.index(v1)
        l2 = self.vertex.index(v2)
        self.graph[l1][l2] = 0
    def degree(self,vertex):
        degree = len(self.vertex)

    def print_graph(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.vertex[i], ' -> ', self.vertex[j], ' wight:', self.graph[i][j])


graph = graph(10)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_edges(1, 3, 6)
graph.add_edges(1, 2, 4)
graph.add_edges(2, 4, 3)
graph.add_edges(6, 2, 5)
graph.add_edges(1, 3, 6)
graph.add_edges(1, 6, 4)

graph.print_graph()