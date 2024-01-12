t = int(input())


def rotate_90(my_arr, n):
    new_arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = str(my_arr[n-1-j][i])
    return new_arr

for i in range(t):
    n = int(input())
    my_arr = [list(map(int, input().split())) for _ in range(n)]

    rotated_90 = rotate_90(my_arr, n)
    rotated_180 = rotate_90(rotated_90, n)
    rotated_270 = rotate_90(rotated_180, n)

    print(f"#{i+1}")
    for j, k, l in zip(rotated_90, rotated_180, rotated_270):
        a = ''.join(j)
        b = ''.join(k)
        c = ''.join(l)
        print(a,b,c)

    