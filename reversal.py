from collections import deque

def reverse(q):
    stack = []

    # queue → stack
    while len(q) > 0:
        stack.append(q.popleft())

    # stack → queue
    while len(stack) > 0:
        q.append(stack.pop())


# main part
q = deque()

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

# reverse call
reverse(q)

# print queue
while len(q) > 0:
    print(q.popleft(), end=" ")