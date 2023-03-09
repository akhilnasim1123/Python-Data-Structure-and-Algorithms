class Graph:
    def __init__(self):
        self.dict = {}

    def insert(self, vertex, edge, is_bidirectional):
        if vertex not in self.dict:
            self.__add_vertex(vertex)
        if edge not in self.dict:
            self.__add_vertex(edge)
        self.dict.get(vertex).append(edge)
        if is_bidirectional:
            self.dict.get(edge).append(vertex)

    def __add_vertex(self, vertex):
        self.dict.update({vertex: []})

    def dfs(self,node):
        visited = set()
        self.__dfs_helper(visited, node)

    def __dfs_helper(self, visited, node):
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for edge in self.dict[node]:
                self.__dfs_helper(visited, edge)
    def bfs(self):
        visited = []
        queue = []
        for node in self.dict:
            self.__bfs_helper(visited,queue,node)
    def __bfs_helper(self,visited,queue,node):
        visited.append(node)
        queue.append(node)
        while queue:
            temp = queue.pop(0)
            print(temp, end=' ')
            for edge in self.dict[temp]:
                if edge not in visited:
                    visited.append(edge)
                    queue.append(edge)
    def show(self):
        print(self.dict)


graph = Graph()
graph.insert(3, 5, True)
graph.insert(3, 4, True)
graph.insert(5, 6, False)
graph.insert(5, 4, True)
graph.dfs(3)
graph.show()
print()
graph.bfs()
