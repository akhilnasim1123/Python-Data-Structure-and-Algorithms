class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class bst:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        current = self.root
        if current is None:
            self.root = node
            return
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = node
                    break
                else:
                    current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = node
                    break
                else:
                    current = current.right
            else:
                print(current.data, ' : node is already exist')
                return

    def insertionrec(self, data):
        current = self.root
        if current:
            return self.insertionhelper(data, current)
        else:
            self.root = Node(data)

    def insertionhelper(self, data, current):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
                return
            else:
                self.insertionhelper(data, current.left)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
                return
            else:
                self.insertionhelper(data, current.right)
        else:
            print('node is already exist')
            return

    def contains(self, data):
        current = self.root
        while current:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return True
        return False

    def remove(self, data):
        return self.remove_helper(data, self.root, None)

    def remove_helper(self, data, current, parent):
        while current:
            if data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right
            else:
                if current.left and current.right:
                    current.data = self.get_min(current.right)
                    self.remove_helper(current.data, current.right, current)
                else:
                    if parent is None:
                        if current.right is None:
                            self.root = current.left
                        else:
                            self.root = current.right
                    else:
                        if parent.left == current:
                            if current.right is None:
                                parent.left = current.left
                            else:
                                parent.left = current.right
                        else:
                            if current.left is None:
                                parent.right = current.left
                            else:
                                parent.right = current.right
                break

    def get_min(self, current):
        if current.left is None:
            return current.data
        else:
            self.get_min(current.left)

    def inorder(self):
        self.inorderhelper(self.root)

    def inorderhelper(self, root):
        if root:
            self.inorderhelper(root.left)
            print(root.data)
            self.inorderhelper(root.right)

    def preOrder(self):
        self.preOrderhelper(self.root)

    def preOrderhelper(self, root):
        print(root.data)
        self.preOrderhelper(root.left)
        self.preOrderhelper(root.right)

    def postOrder(self):
        self.postOrderhelper(self.root)

    def postOrderhelper(self, root):
        self.postOrderhelper(root.left)
        self.postOrderhelper(root.right)
        print(root.data)

    def current(self):
        return self.root

    def findClosest(self,data):
        pass


bst = bst()
bst.insert(12)
bst.insert(6532)
bst.insert(1)
bst.insert(62)
bst.insert(2)
bst.insert(6)
bst.insert(6)
bst.insertionrec(122)

bst.remove(3)
bst.inorder()
print(bst.contains(3))
