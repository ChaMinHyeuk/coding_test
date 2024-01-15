t = int(input())

for i in range(t):
    my_list = list(map(int, input().split()))

    my_list.sort()

    my_sum = 0
    for j in range(1, len(my_list)-1):
        my_sum += my_list[j]
    
    print(f"#{i+1} {int(round((my_sum/(len(my_list)-2))))}")