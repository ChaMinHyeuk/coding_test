import sys

sys.stdin = open('./input.txt')

t = int(input())

for i in range(t):
    n = int(input())

    my_lst = list(map(int, input().split()))
    my_min  = 21e8
    cnt = 0
    for j in my_lst:
        result = abs(j) - 0
        if result == my_min:
            cnt+=1
        if result < my_min:
            cnt = 1
            my_min = result
    
    print(f"#{i+1} {my_min} {cnt}")

