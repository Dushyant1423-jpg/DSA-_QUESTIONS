def staircasesearch(matrix, key):

    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:

        if matrix[row][col] == key:
            print("Found key at (", row, ",", col, ")")
            return True

        elif key < matrix[row][col]:
            col -= 1
        else:
            row += 1

    print("Key not found")
    return False


matrix = [
    [10,20,30,40],
    [15,25,35,45],
    [27,29,37,48],
    [32,33,39,50]
]

key = 33
staircasesearch(matrix, key)