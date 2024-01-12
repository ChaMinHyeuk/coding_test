t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(n)]
    my_max = 0
    
    for j in range(n):
        for k in range(n):
            my_sum = 0
            my_sum += my_map[j][k]
            for l in range(1,m):
                if j-l <0 or k-l < 0 or j+l >n-1 or k+l > n-1:
                    continue
                else:
                    my_sum += my_map[j-l][k]
                    my_sum += my_map[j+l][k]
                    my_sum += my_map[j][k-l]
                    my_sum += my_map[j][k+l]
            if my_sum > my_max:
                my_max = my_sum
            my_sum = 0
            my_sum += my_map[j][k]
            for l in range(1, m):
                if (j-l <0 or k-l < 0) or (j+l >n-1 or k+l > n-1) or (j+l > n-1 or k-l < 0) or (j-l < 0 or k+l > n-1):
                    continue
                else:
                    my_sum += my_map[j-l][k+l]
                    my_sum += my_map[j-l][k-l]
                    my_sum += my_map[j+l][k+l]
                    my_sum += my_map[j+l][k-l]
            if my_sum > my_max:
                my_max = my_sum
    print("#" + str(i+1) + " " + str(my_max))