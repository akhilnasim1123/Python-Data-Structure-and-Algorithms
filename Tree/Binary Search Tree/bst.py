class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Bst:
    def __init__(self):
        self.root = None

    def insert(self, data):
        current = self.root
        node = Node(data)
        if self.root is None:
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
                print('this node is already exist')
                return

    def remove(self, data):
        self.removehelper(data, self.root, None)

    def removehelper(self, data, current, parent):
        while True:
            if data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right
            else:
                if current.left and current.right:
                    current.data = self.get_min(current.right)
                    self.removehelper(current.data, current.right, current)
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
                            if current.right is None:
                                parent.right = current.left
                            else:
                                parent.right = current.right
                break

    def get_min(self, current):
        if current.left is None:
            return current.data
        else:
            self.get_min(current.left)
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

bst = Bst()
bst.insert(6)
bst.insert(2)
bst.insert(4)
bst.remove(4)
print(bst.contains(4))

