# stack and queue using deque
from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, data):
        self.q.append(data)

    def pop(self):
        return self.q.pop()

    def peek(self):
        return self.q[-1]


s = Stack()

s.push(1)
s.push(2)
s.push(3)

print("peek:", s.peek())
print("pop:", s.pop())
print("pop:", s.pop())
print("pop:", s.pop())