class Graph:
    def __init__(self):
        self.dict = {}

    def insert(self,vertex,edges,is_bidirectional):
        if vertex  not in self.dict:
            self.add_vertex(vertex)
        if edges not in self.dict:
            self.add_vertex(edges)
        self.dict.get(vertex).append(edges)
        if is_bidirectional:
            self.dict.get(edges).append(vertex)
    def add_vertex(self, vertex):
        self.dict.update({vertex: []})
    def display(self):
        print(self.dict)

    def degree(self,node):
        degree = len(self.dict.get(node))
        return degree

graph = Graph()
graph.insert(3,5,True)
graph.insert(3,4,True)
graph.insert(5,6,False)
graph.insert(5,4,True)
graph.display()
print(graph.degree(6))