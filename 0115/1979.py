t = int(input())


def check_row(my_map, start_row, n, m):
    check = 0 
    for i in range(n):
        if my_map[start_row][i] == 0:
            return False
        else:
            check += 1
    if check == m:
        return True
    else:
        return False

def check_col(my_map, start_col, n, m):
    check = 0

    for i in range(n):
        if my_map[i][start_col] == 0:
            return False
        else:
            check += 1
    if check == m:
        return True
    else:
        return False

for i in range(t):
    n, m = map(int, input().split())

    my_map = [list(map(int, input().split())) for _ in range(n)]

    my_sum = 0

    for j in range(n):
        for k in range(n):
            if check_row(my_map, j, n, m):
                my_sum +=1
    
    for j in range(n):
        for k in range(n):
            if check_col(my_map, j, n, m):
                my_sum +=1
    
    print(f"#{i+1} {my_sum}")