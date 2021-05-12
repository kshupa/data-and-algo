class My_array():
    def __init__(self):
        self.length = 0
        self.data = {}


    def __str__(self):
        return str(self.__dict__)


    def get(self, index):
        return self.data[index]


    def push(self, item):
        self.length += 1
        self.data[self.length - 1] = item


    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item


my_list = My_array()
my_list.push(1)
my_list.push('hi')
my_list.pop()
print(my_list)
