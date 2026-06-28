class ArrayQueue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        return self.queue.append(x)

    def pop(self):
        first_el = self.queue.pop(0)
        self.queue = self.queue[0:]
        return first_el

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

arrqueue = ArrayQueue()
arrqueue.push(5)
arrqueue.push(10)
print(arrqueue.queue)
print(arrqueue.peek())
print(arrqueue.pop())
print(arrqueue.queue)
print(arrqueue.isEmpty())