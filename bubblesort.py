def bubblesort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n-1-i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp

    for i in range(n):
        print(numbers[i], end=" ")

numbers = [5,4,1,3,2]
bubblesort(numbers)