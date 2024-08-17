def sort_it_up(n, arr):
    start = 0
    end = n - 1
    i = 0
    while i <= end:
        if arr[i] == 2:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
    return arr

n = int(input())
arr = list(map(int, input().split()))
output = sort_it_up(n, arr)
print(' '.join(map(str, output)))
