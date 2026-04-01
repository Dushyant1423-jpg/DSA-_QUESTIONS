from collections import deque

class Classroom:
    def __init__(self):
        self.count = {}
        self.queue = deque()

    def insert(self, char):
        self.count[char] = self.count.get(char, 0) + 1
        self.queue.append(char)

    def first_non_repeating(self):
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1


# test
stream = "aabcbd"
c = Classroom()

for char in stream:
    c.insert(char)
    print(c.first_non_repeating(), end=" ")