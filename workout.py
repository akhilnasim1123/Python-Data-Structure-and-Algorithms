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
            if data < current.left:
                if current.left is None:
                    current.left = node
                    break
                else:
                    current = current.left
            elif data > current.right:
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
            if data < current.left:
                current = current.left
            elif data > current.right:
                current = current.right
            else:
                return True
        return False

    def remove(self, data):
        self.__removehelper(data, self.root, None)

    # def __remove(self,data,current,parent):
    #     while current:
    #         if data < current.left:
    #             parent = current
    #             current = current.left
    #         elif data > current.right:
    #             parent = current
    #             current = current.right
    #         else:
    #             if current.left and current.right:
    #                 current.data = self.get_min(current.right)
    #                 self.__remove(data,current.right,current)
    #             else:
    #                 if parent is None:
    #                     if current.right is None:
    #                         self.root = current.left
    #                     else:
    #                         self.root = current.right
    #                 else:
    #                     if parent.left == current:
    #                         if current.right is None:
    #                             parent.left = current.left
    #                         else:
    #                             parent.left = current.right
    #                     else:
    #                         if current.right is None:
    #                             parent.right = current.left
    #                         else:
    #                             parent.right = current.right
    #             break

    def __removehelper(self, data, current, parent):
        while current:
            if data < current.left:
                parent = current
                current = current.left
            elif data > current.right:
                parent = current
                current = current.right
            else:
                if current.left and current.right:
                    current.data = self.get_min(current.right)
                    self.__removehelper(data, current.right, current)
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
                                parent.right = current.right
                        if parent.right == current:
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


class MinHeap:
    def __init__(self, array):
        self.array = array
        self.root = None
        self.__build_heap()

    def __build_heap(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.shiftdown(i)

    def shiftdown(self, current_index):
        endx = len(self.array) - 1
        left = self.__leftindx(current_index)
        while left <= endx:
            rightx = self.__rightx(current_index)
            if rightx <= endx and self.array[rightx] < self.array[left]:
                idx = rightx
            else:
                idx = left
            if self.array[current_index] < self.array[idx]:
                self.__swap(current_index, idx)
                current_index = idx
                left = self.__leftindx(current_index)
            else:
                return

    def shift_up(self, current_idx):
        parent_idx = self.__parent(current_idx)
        while current_idx > 0 and self.array[parent_idx] > self.array[current_idx]:
            self.__swap(parent_idx, current_idx)
            current_idx = parent_idx
            parent = self.__parent(current_idx)

    def remove(self):
        self.__swap(0, len(self.array) - 1)
        self.array.remove(len(self.array) - 1)
        self.shift_up(0)

    def insert(self, data):
        self.array.append(data)
        self.shiftdown(len(self.array - 1))

    def __swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __rightx(self, i):
        return (i * 2) + 2

    def __leftindx(self, i):
        return (i * 2) + 1

    def __parent(self, i):
        value = int(i - 1) / 2
        return value


class heappp:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        current = self.root
        if self.root is None:
            self.root = node
        while True:
            if data < current.left:
                if current.left is None:
                    current.left = node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                else:
                    current = current.right

    def remove(self, data):
        self.removehelper(data, self.root, None)

    def removehelper(self, data, current, parent):
        while True:
            if data < current.left:
                parent = current
                current = current.left
            elif data > current.right:
                parent = current
                current = current.right
            else:
                if current.left and current.right:
                    current.data = self.get_min(current.right)
                    self.removehelper(current.data, current.left, current)
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


class TriesNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = None

    def insert(self, string):
        node = self.root
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TriesNode(char)
                node.children[char] = newNode
                node = newNode
        node.is_end = True

    def dfs(self, node, pre):
        if node.end:
            self.output.append(pre + node.char)
        for child in node.children:
            self.dfs(child, pre + node.char)

    def search(self, x):
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.output = []
        self.dfs(node, x[:-1])
