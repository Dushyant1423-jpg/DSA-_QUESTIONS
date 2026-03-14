def selectionsort(numbers):
    n = len(numbers)

    for i in range(n):
        minpos = i

        for j in range(i+1, n):
            if numbers[minpos] > numbers[j]:
                minpos = j

        temp = numbers[i]
        numbers[i] = numbers[minpos]
        numbers[minpos] = temp

    print(numbers)


numbers = [5,4,1,3,2]
selectionsort(numbers)