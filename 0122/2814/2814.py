t = int(input())

def dfs(start_node, my_arr, used, length):

    used[start_node] = 1

    for i in my_arr[start_node]:
        if used[i] == 1:
            continue
        
        length = dfs(i, my_arr, used, length+1)

    return length

for i in range(t):
    n, m = map(int, input().split())

    my_arr = [[] for _ in range(n)]

    for j in range(m):
        start, end = map(int, input().split())
        my_arr[start-1].append(end-1)
        my_arr[end-1].append(start-1)

    my_max = 0

    for j in range(n):
        length = 1
        used = [0 for _ in range(n)]
        result = dfs(j, my_arr, used, length)
        if result > my_max:
            my_max = result
    
    print(f"#{i+1} {my_max}")