class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def empty(self):
        return len(self.queue1) == 0

    def add(self, data):   # push
        # q1 → q2
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))

        # new element
        self.queue1.append(data)

        # q2 → q1
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))

    def remove(self):   # pop
        if self.empty():
            print("Stack is empty")
            return None
        return self.queue1.pop(0)

    def peek(self):
        if self.empty():
            print("Stack is empty")
            return None
        return self.queue1[0]


# test
s = Stack()
s.add(1)
s.add(2)
s.add(3)

while not s.empty():
    print(s.peek())
    s.remove()
                                