from collections import deque

n, m = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(m)]
used = [[0 for _ in range(n)] for _ in range(m)]
my_q = deque()

class Coord():
    def __init__(self, y, x):
        self.y = y
        self.x = x

dirty = [-1, 0, 1, 0]
dirtx = [0, 1, 0, -1]


def bfs(my_day):
    
    while my_q:
        my_day += 1
        now = my_q.pop()

        for i in range(4):
            newy = now.y + dirty[i]
            newx = now.x + dirtx[i]

            if newy > m-1 or newy < 0 or newx > n-1 or newx < 0:
                continue
            if used[newy][newx] == 1:
                continue
            if my_map[newy][newx] == -1:
                continue

            my_map[newy][newx] = 1
            used[newy][newx] = 1



max_day = 0
my_day = 0
if all(0 not in l for l in my_map):
    print(0)
else:
    for i in range(m):
        for j in range(n):
            if my_map[i][j] == 1:
                starty = i
                startx = j
                my_q.append(Coord(i,j))
                used[i][j] = 1
                bfs()
                my_day += 1    
                if my_day > max_day:
                    max_day = my_day

    if any(0 in k for k in my_map):
        print(-1)
    else:
        print(my_day)






