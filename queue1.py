from collections import deque

class Queue:
    def binary_numbers(self, n):
        for i in range(1, n+1):
            num = i
            binary = ""

            while num > 0:
                binary = str(num % 2) + binary
                num = num // 2

            print(binary, end=" ")
            

q = Queue()
q.binary_numbers(5)