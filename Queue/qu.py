class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            print("The queue is empty")
            return None
        self.items.pop(0)
    def peek(self):
        if self.is_empty():
            print("The queue is empty")
            return None
        return self.items[0]


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.peek())
    q.dequeue()
    print(q.peek())