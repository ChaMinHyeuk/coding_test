from collections import Counter

test_case = int(input())

for j in range(test_case):
    current_case = int(input())

    my_dic = Counter(list(map(int, input().split())))
    
    my_max = 0
    for i in my_dic:
        if my_max <my_dic[i]:
            my_max = my_dic[i]
            ans = i
    print("#" + str(j+1) + " " + str(ans))