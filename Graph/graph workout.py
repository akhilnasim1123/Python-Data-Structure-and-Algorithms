class graph:
    def __init__(self):
        self.dict = {}

    def insert(self, vertex, edges, is_bidirectional):
        if vertex not in self.dict:
            self.add_vertex(vertex)
        if edges not in self.dict:
            self.add_vertex(edges)
        self.dict.get(vertex).append(edges)
        if is_bidirectional:
            self.dict.get(edges).append(vertex)

    def add_vertex(self, value):
        self.dict.update({value: []})

    def display(self):
        print(self.dict)

    def degree(self, vertex):
        if vertex in self.dict:
            return len(self.dict[vertex])

    def dfs_caller(self, value):
        visited = set()
        for node in self.dict:
            self.__dfs(visited, node, value)

    def __dfs(self, visited, node, value):
        if node not in visited:
            visited.add(node)
            count = 0
            for edges in self.dict[node]:
                count += 1
                if edges == value:
                    print('Vertex is : ', node, ' |  ', count, 'nth Element')
                    return
                else:
                    self.__dfs(visited, edges, value)

    def bfs_caller(self):
        visited = []
        queue = []
        count = 0
        for node in self.dict:
            count +=self.__bfs(visited, queue, node, 5)

    def __bfs(self, visited, queue, node, value):
        visited.append(node)
        queue.append(node)
        count = 0
        while queue:
            s = queue.pop(0)
            for edge in self.dict[s]:
                if edge == value:
                    print('node is :', s, ' edge is :', edge)
                    count += 1
                else:
                    if edge not in visited:
                        visited.append(edge)
                        queue.append(edge)
        return count

graph = graph()
graph.insert(3, 5, True)
graph.insert(3, 4, True)
graph.insert(5, 6, False)
graph.insert(5, 4, True)
graph.display()
# graph.dfs_caller(4)
graph.bfs_caller()
