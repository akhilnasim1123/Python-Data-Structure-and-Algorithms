class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
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
                break

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
        self.remove_helper(data, self.root, None)

    def remove_helper(self, data, current, parent):
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

    def inorder(self):
        self.inorder_helper(self.root)

    def inorder_helper(self, root):
        if root is None:
            return
        self.inorder_helper(root.left)
        print(root.data, end=' ')
        self.inorder_helper(root.right)

    def pre_order(self):
        self.__pre_orderhelper(self.root)

    def __pre_orderhelper(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.__pre_orderhelper(root.left)
        self.__pre_orderhelper(root.right)

    def post_order(self):
        self.__post_orderhelper(self.root)

    def __post_orderhelper(self, root):
        if root is None:
            return
        self.__post_orderhelper(root.left)
        self.__post_orderhelper(root.right)
        print(root.data, end=' ')

    def isComplete_funCaller(self):
        print(self.__is_complete(self.root))

    # def __is_complete(self, root):
    #     if root is None:
    #         return True
    #     queue = []
    #     flag = False
    #     queue.append(root)
    #     while len(queue) != 0:
    #         temp = queue.pop(0)
    #         if temp is None:
    #             flag = True
    #         else:
    #             if flag:
    #                 return False
    #             queue.append(temp.left)
    #             queue.append(temp.right)
    #     return True
    def __is_complete(self,root):
        if root is None:
            return True
        q = []
        flag = False
        q.append(root)
        while len(q)!=0:
            temp = q.pop(0)
            if temp is None:
                flag = True
            else:
                if flag:
                    return False
                q.append(temp.left)
                q.append(temp.right)
        return True

    def array_to_bst(self, array):
        for i in array:
            self.insert(i)


bst = BST()
bst.insert(6)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(10)
# bst.remove(8)
# lst = [1, 8,  10]
# bst.array_to_bst(lst)
print(bst.contains(8))
bst.inorder()

print()

print('-------')
bst.pre_order()
print()
print('-------')
bst.post_order()
print()
print('-------')
bst.isComplete_funCaller()
print(bst.root.data)
