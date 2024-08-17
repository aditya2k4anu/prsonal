def is_valid(arr):
    row = [[0 for _ in range(9)] for _ in range(9)]
    col = [[0 for _ in range(9)] for _ in range(9)]
    box = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if arr[i][j] != -1:
                value = arr[i][j] - 1
                boxno = 3*(i // 3) + (j // 3)
                if row[i][value] == 1 or col[j][value] == 1 or box[boxno][value] == 1:
                    return 0
                row[i][value] = 1
                col[j][value] = 1
                box[boxno][value] = 1

    return 1

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

output = is_valid(arr)
print(output)
