class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            print('The stack is empty')
            return None
        return self.items[-1]


if __name__ == "__main__" :
    stack = Stack()
    print(stack.peek())
    stack.push(10)
    stack.push(14)
    print(stack.peek())