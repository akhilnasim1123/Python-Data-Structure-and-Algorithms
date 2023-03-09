class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            return self.inserthelper(data, self.root)

    def inserthelper(self, data, current):
        if data <= current.data:
            if current.left is None:
                current.left = Node(data)
                return
            else:
                self.inserthelper(data, current.left)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
                return
            else:
                self.inserthelper(data, current.right)

    def search(self, data):
        if self.root.data == data:
            print(True)
        else:
            self.searchhelper(data, self.root)

    def searchhelper(self, data, root):
        if data < root.data:
            if root.left:
                self.searchhelper(data, root.left)
        elif data > root.data:
            if root.right:
                self.searchhelper(data, root.right)
        else:
            print(True)
            return

    def inorder(self):
        return self.inorderhelper(self.root)

    def inorderhelper(self, root):
        if root:
            self.inorderhelper(root.left)
            print(root.data)
            self.inorderhelper(root.right)


a = BST()
a.insert(10)
a.insert(11)
a.insert(1)
a.insert(2)
a.inorder()
a.search(177)
