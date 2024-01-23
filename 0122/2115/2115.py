import sys

sys.stdin = input(input.txt)


def check_honey(my_map, n, m, start_y, start_x, c, used):
    my_max = 0
    honey_sum = 0
    honey = []
    max_honey = []
    for i in range(m):
        if start_x + i > n-1 :
            continue
        if used[start_y][start_x+1] == 1:
            continue
        honey_sum += my_map[start_y][start_x+i]
        honey.append(my_map[start_y][start_x+i])
    if my_max < honey_sum:
        my_max = honey_sum
        max_honey.extend(honey)
    return my_max
t = int(input())
for i in range(t):
    n, m, c = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range()]
    used = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for k in range(n):
            for l in range(2):
                result = check_honey(my_map, n, m, j, k, c, used)

