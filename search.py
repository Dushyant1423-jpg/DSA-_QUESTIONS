def search(matrix, key):

    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == key:
                count += 1

    print("Total count of", key, "=", count)
    return count


matrix = [
    [4,7,8],
    [8,8,7]
]

key = 7
search(matrix, key)