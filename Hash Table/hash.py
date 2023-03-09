class Hash:
    def __init__(self):
        self.max = 100
        self.array = [[] for i in range(self.max)]
    def get_hash(self,key):
        i = 0
        for char in key:
            i+=ord(char)
        return  i% self.max
    def add(self,key,value):
        i=self.get_hash(key)
        self.array[i]= value

