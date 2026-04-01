class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def empty(self):
        return len(self.stack1) == 0

    def add(self, data):

        # stack1 → stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # add element
        self.stack1.append(data)

        # stack2 → stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def remove(self):
        if self.empty():
            print("Queue is empty")
        else:
            return self.stack1.pop()

    def peek(self):
        if self.empty():
            print("Queue is empty")
        else:
            return self.stack1[-1]


# test
q = Queue()
q.add(1)
q.add(2)
q.add(3)

while not q.empty():
    print(q.peek())
    q.remove()
