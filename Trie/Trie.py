class TrieNode:
    def __init__(self,data):
        self.char = data
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self,string):

        node = self.root
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode(char)
                node.children[char]=newNode
                node = newNode
        node.end = True


    def search(self,x):
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.output = []
        self.__starts_with(node,x[:-1])
        return self.output
    def __starts_with(self,node,pre):
        if node.end:
            self.output.append(pre+node.char)
        for edge in node.children.values():
            self.__starts_with(edge,pre+node.char)

trie = Trie()
trie.insert('hello')
trie.insert('he')
trie.insert('hell')
trie.insert('llo')
print(trie.search('lgfgfgf'))