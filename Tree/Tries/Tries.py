class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.end = False


class Tries:
    def __init__(self):
        self.root = TrieNode("")

    # def insert(self, string):
    #     node = self.root
    #     for char in string:
    #         if char in node.children:
    #             node = node.children[char]
    #         else:
    #             newNode = TrieNode(char)
    #             node.children[char] = newNode
    #             node = newNode
    #     node.end = True
    #
    # def dfs(self, node, pre):
    #
    #     if node.end:
    #         self.output.append((pre + node.char))
    #
    #     for child in node.children.values():
    #         self.dfs(child, pre + node.char)
    #
    # def search(self, x):
    #     node = self.root
    #     for char in x:
    #         if char in node.children:
    #             node = node.children[char]
    #         else:
    #             return []
    #     self.output = []
    #     self.__dfs(node, x[:-1])
    #
    # def __dfs(self, node, pre):
    #     if node.end:
    #         self.output.append((pre + node.char))
    #     for child in node.children.values():
    #         self.dfs(child, pre + node.char)
    #
    # def search(self, x):
    #
    #     node = self.root
    #
    #     for char in x:
    #         if char in node.children:
    #             node = node.children[char]
    #         else:
    #
    #             return []
    #
    #     self.output = []
    #     self.dfs(node, x[:-1])
    #
    #     return self.output

    def insert(self, string):
        node = self.root
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode(char)
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
        self.__dfs(node, x[:-1])
        return self.output

    def __dfs(self, node, pre):
        if node.end:
            self.output.append((pre + node.char))
        for char in node.children.values():
            self.__dfs(char, pre + node.char)


trie = Tries()
trie.insert('hello')
trie.insert('lo')
trie.insert('he')
trie.insert('hell')
print(trie.search('he'))
var = 'hello'