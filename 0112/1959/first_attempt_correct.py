test_case = int(input())

for i in range(test_case):
    n, m = map(int, input().split())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    max_size = max(n,m)
    min_size = min(n,m)

    while len(arr1) != max_size :
        arr1.append(0)
        temp_arr  = 1
    while len(arr2) != max_size:
        arr2.append(0)
        temp_arr = 2

    my_max = 0
    for j in range((max_size-min_size)+1):
        arr3 = []
        for k in range(max_size):
            arr3.append(arr1[k]*arr2[k])
        my_max2 = sum(arr3)

        if my_max < my_max2:
            my_max = my_max2
        
        if temp_arr == 1:
            arr1.pop(-1)
            arr1.insert(0, 0)
        else:
            arr2.pop(-1)
            arr2.insert(0,0)

        
    print("#" + str(i+1) + " " + str(my_max))
