def insertionsort(numbers):
    n = len(numbers)

    for i in range(1, n):
        curr = numbers[i]
        prev = i - 1

        while prev >= 0 and numbers[prev] > curr:
            numbers[prev + 1] = numbers[prev]
            prev = prev - 1

        numbers[prev + 1] = curr

    print(numbers)


numbers = [5,4,1,3,2]
insertionsort(numbers)