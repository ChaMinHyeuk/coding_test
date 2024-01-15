t = int(input())

def check_flies(my_map, my_sum, j, k, n, m):

    for i in range(m):
        for l in range(m):
            if j+i > n-1 or k+l > n-1:
                continue
            else:
                my_sum += my_map[j+i][k+l]
    return my_sum

for i in range(t):
    n, m = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(n)]
    my_sum = 0
    my_max = 0
    for j in range(n):
        for k in range(n):
            my_sum = check_flies(my_map, 0, j, k, n, m)
            if my_max < my_sum:
                my_max = my_sum
    
    print(f"#{i+1} {my_max}")

        
