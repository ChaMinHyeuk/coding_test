
t = int(input())

for i in range(t):

    num = int(input())
    
    my_dic = {
        0 : [],
        1 : [],
        2 : []
    }

    for j in range(num):
        input_string = list(input())
        my_lst = []
        for str_idx, my_str in enumerate(input_string):
            if my_str == "*":
                my_lst.append(str_idx)
        if 0 in my_lst:
            for k in range(len(my_lst)):
                input_string.remove("*")
            if my_dic[0]:
                if sum(list(map(int,input_string))) > sum(list(map(int, my_dic[0]))):
                    my_dic[0] = list(map(int, input_string))
            else:
                my_dic[0] = list(map(int, input_string))
        elif len(input_string)-1 in my_lst:
            for k in range(len(my_lst)):
                input_string.remove("*")
            if my_dic[2]:
                if sum(list(map(int, input_string))) > sum(list(map(int, my_dic[2]))):
                    my_dic[2] = list(map(int, input_string))
            else:
                my_dic[2] = list(map(int, input_string))
        elif not my_lst:
            my_dic[1].append(int(''.join(input_string)))
    
    my_sum = 0
    for j in my_dic:
        if j != 1:
            for k in my_dic[j]:
                my_sum += int(k)
        else:
            for k in my_dic[j]:
                my_num = list(str(k))
                for l in my_num:
                    my_sum += int(l)
    print(f"{i+1} {my_sum}")
            
