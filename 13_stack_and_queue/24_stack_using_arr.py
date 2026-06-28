class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        return self.stack.append(x)

    def pop(self):
        last_el = self.stack[-1]
        self.stack = self.stack[:-1]
        return last_el

        
    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

        return False
       
    
arraystack = ArrayStack()
arraystack.push(5)
print(arraystack.stack)
arraystack.push(10)
print(arraystack.stack)
print(arraystack.top())
print(arraystack.pop())
print(arraystack.stack)