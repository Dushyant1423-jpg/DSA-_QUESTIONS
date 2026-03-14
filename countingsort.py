def countingsort(arr):

    largest = max(arr)

    count = [0] * (largest + 1)

    # counting elements
    for i in range(len(arr)):
        count[arr[i]] += 1

    # sorting
    j = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1

    print(arr)


arr = [4,2,2,8,3,3,1]
countingsort(arr)