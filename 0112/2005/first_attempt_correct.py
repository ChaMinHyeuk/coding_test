t = int(input())

for i in range(t):
    n = int(input())
    my_arr = [[0 for _ in range(n)] for _ in range(n)]
    
    for j in range(n):
        my_arr[j][0] = 1

    for j in range(1, n):
        for k in range(1, n):
            my_arr[j][k] = my_arr[j-1][k-1] + my_arr[j-1][k]
    
    print(f"#{i+1}")         
    for j in range(n):
        for k in range(n):
            if my_arr[j][k] != 0:
                print(my_arr[j][k], end=" ")
        print(" ")