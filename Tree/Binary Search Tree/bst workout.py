class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        current = self.root
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
                break

    def remove(self, data):
        self.__remove_helper(data, self.root, None)

    def __remove_helper(self, data, current, parent):
        while True:
            if data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right
            else:
                if current.left and current.right:
                    current.data = self.__get_min(current.right)
                    self.__remove_helper(current.data, current.right, current)
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
                            if parent.right == current:
                                if current.right is None:
                                    parent.right = current.left
                                else:
                                    parent.right = current.right
                    break

    def __get_min(self, current):
        if current.left is None:
            return current.data
        else:
            self.__get_min(current.left)

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

    def inorder(self):
        self.__inorder_helper(self.root)

    def __inorder_helper(self, root):
        if root is None:
            return
        self.__inorder_helper(root.left)
        print(root.data, end=' ')
        self.__inorder_helper(root.right)

    def preorder(self):
        self.__preorder_helper(self.root)

    def __preorder_helper(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.__preorder_helper(root.left)
        self.__preorder_helper(root.right)

    def postorder(self):
        self.__postorder_helper(self.root)

    def __postorder_helper(self, root):
        if root is None:
            return
        self.__postorder_helper(root.left)
        self.__postorder_helper(root.right)
        print(root.data, end=' ')

    def is_complete(self):
        return self.__is_complete_helper(self.root)

    def __is_complete_helper(self, root):
        if root is None:
            return True
        queue = []
        flag = False
        queue.append(root)
        while len(queue) != 0:
            temp = queue.pop(0)
            if temp is None:
                flag = True
            else:
                if flag:
                    return False
                queue.append(temp.left)
                queue.append(temp.right)
        return True


bst = BST()
bst.insert(6)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(10)

bst.inorder()
print(bst.is_complete())
print(bst.root.data)
