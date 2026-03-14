
def twice(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] == numbers[j]:
                return True

    return False


numbers = [1,2,3,1]
print(twice(numbers))