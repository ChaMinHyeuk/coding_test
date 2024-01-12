t = int(input())

cross_dirty = [-1, 0, 1, 0]
cross_dirtx = [0, 1, 0, -1]

x_dirty = [-1, 1, -1, 1]
x_dirtx = [-1, 1, 1, -1]


def check_plus(my_arr, starty, startx, n, m):

    my_sum = my_arr[starty][startx]

    for i in range(1, m):
        for j in range(4):
            if starty+ (cross_dirty[j]*i) > n-1 or starty + (cross_dirty[j]*i) <0 or startx + cross_dirtx[j] * i > n-1 or startx + cross_dirtx[j] * i <0:
                continue
            else:
                my_sum += my_arr[starty + cross_dirty[j]*i][startx+cross_dirtx[j]*i]
    
    return my_sum


def check_x(my_arr, starty, startx, n, m):
    my_sum = my_arr[starty][startx]

    for i in range(1, m):
        for j in range(4):
            if starty+ x_dirty[j] *i > n-1 or starty + x_dirty[j] *i <0 or startx + x_dirtx[j] * i > n-1 or startx + x_dirtx[j] *i <0:
                continue
            else:
                my_sum += my_arr[starty + x_dirty[j]*i][startx+x_dirtx[j]*i]
    
    return my_sum

for i in range(t):
    n, m = map(int, input().split())
    my_arr = [list(map(int, input().split())) for _ in range(n)]
    
    my_max = 0
    for j in range(n):
        for k in range(n):
            plus_max = check_plus(my_arr, j, k, n, m)
            x_max = check_x(my_arr, j, k, n, m)
            one_max = max(plus_max, x_max)
            if one_max > my_max:
                my_max = one_max
    
    print("#" + str(i+1) + " " + str(my_max))


