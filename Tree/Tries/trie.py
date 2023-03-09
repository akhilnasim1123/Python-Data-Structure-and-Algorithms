class Tries:
    def __init__(self, data):
        self.char = data
        self.children = {}
        self.end = False


class trie:
    def __init__(self):
        self.root = Tries("")

    def insert(self, string):
        node = self.root
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = Tries(char)
                node.children[char] = newNode
                node = newNode
        node.end = True

    def search(self, x):
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.output = []
        self.dfs(node, x[:-1])
        return self.output

    def dfs(self, node, pre):
        if node.end:
            self.output.append(pre + node.char)
        for char in node.children.values():
            self.dfs(char, pre + node.char)
tries = trie()
tries.insert('hello')
tries.insert('he')
tries.insert('hell')
print(tries.search('h'))
