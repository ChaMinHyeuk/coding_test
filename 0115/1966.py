t = int(input())

for i in range(t):
    n = int(input())

    my_arr = list(map(int, input().split()))

    my_arr.sort()

    str_my_arr = []
    for j in my_arr:
        str_my_arr.append(str(j))

    print(f"#{i+1} {' '.join(str_my_arr)}")