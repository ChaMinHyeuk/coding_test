t = int(input())

dx = [1, 1, 1]
dy = [-1, 0, -1]

for _ in range(t):
    n, m = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    print(0)
    