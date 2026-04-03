from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    # add (enqueue)
    def add(self, data):
        self.q.append(data)   # addLast

    # remove (dequeue)
    def remove(self):
        if len(self.q) == 0:
            print("Queue is empty")
            return
        return self.q.popleft()   # removeFirst

    # peek (front element)
    def peek(self):
        if len(self.q) == 0:
            print("Queue is empty")
            return
        return self.q[0]   # getFirst


# main part (same as Java main)
q = Queue()

q.add(1)
q.add(2)
q.add(3)

print("peek =", q.peek())
print(q.remove())
print(q.remove())
print(q.remove())