class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()

print(q.enqueue(9))
print(q.enqueue(1))
print(q.enqueue(5))
print(q.dequeue())
print(q.__class__)