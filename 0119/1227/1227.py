import sys
from collections import deque

sys.stdin = open("input.txt")


dirty = [-1, 1, 0, 0]
dirtx = [0, 0, -1, 1]

class Coord():
    def __init__(self, y, x):
        self.y =y 
        self.x =x


def bfs(my_map, visited, my_q, start_y, start_x, end_y, end_x):

    visited[start_y][start_x] = 1
    my_q.append(Coord(start_y, start_x))
    my_flag = False

    if start_y == end_y and start_x == end_x:
        return True
    
    while my_q:
        now = my_q.popleft()

        for i in range(4):
            newy = now.y + dirty[i]
            newx = now.x + dirtx[i]

            if newy < 0 or newy > 99 or newx < 0 or newy > 99:
                continue
            if my_map[newy][newx] == 1:
                continue
            if visited[newy][newx] != 0:
                continue
            if my_map[newy][newx] == 3:
                my_flag = True
                break

            my_q.append(Coord(newy, newx))
            visited[newy][newx] = 1

    return my_flag

for i in range(10):
    test_case = int(input())
    my_q = deque()
    my_map = [list(map(int, input())) for _ in range(100)]
    visited = [[0 for _ in range(100)] for _ in range(100)]
    for j in range(100):
        for k in range(100):
            if my_map[j][k] == 2:
                start_y, start_x = j, k
            elif my_map[j][k] == 3:
                end_y, end_x = j, k
    
    if bfs(my_map, visited, my_q, start_y, start_x, end_y, end_x):
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
        
