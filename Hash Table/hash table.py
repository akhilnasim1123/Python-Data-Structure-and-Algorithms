class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def add(self, key, value):
        i = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[i]):
            if len(element) == 2 and element[0] == key:
                self.arr[i][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[i].append((key, value))
        self.arr[i] = value

    def get(self, key):

        i = self.get_hash(key)
        if i:
            return self.arr[i]
        else:
            message = 'There is no Data, Please Check What You asked....'
            return message
    def delete(self,key):
        i = self.get_hash(key)
        for idx, element in enumerate(self.arr[i]):
            if element[0]==key:
                del self.arr[i][idx]


hash = HashTable()
hash.add('my birth day', 'Feb 9')
print('You Can Ask Me :')
print(hash.get(input()))
