n = int(input())

def check_box(my_arr, i, j):
    box_arr = []
    for k in range(3):
        for l in range(3):
            box_arr.append(my_arr[(i*3)+k][(j*3)+l])
    if len(set(box_arr)) == 9:
        return True
    else:
        return False

def check_row(my_arr, i):
    row_arr = []
    for k in range(9):
        row_arr.append(my_arr[i][k])
    if len(set(row_arr)) == 9:
        return True
    else:
        return False

def check_column(my_arr, i):
    column_arr = []
    for k in range(9):
        column_arr.append(my_arr[k][i])
    if len(set(column_arr))==9:
        return True
    else:
        return False

def check_sudoqu(my_arr):
    ans = True
    for i in range(3):
        for j in range(3):
            if check_box(my_arr, i, j) == False:
                return False
            else:
                continue
    for i in range(9):
        if check_row(my_arr, i) == False:
            return False
        else:
            continue
    for i in range(9):
        if check_column(my_arr, i) == False:
            return False
        else:
            continue
    return ans
 
                
                
for i in range(n):
    my_arr = [list(map(int, input().split())) for _ in range(9)]
    
    if check_sudoqu(my_arr):
        print("#" + str(i+1) + " " + "1")
    else:
        print("#" + str(i+1) + " " + "0")