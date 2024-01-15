t = int(input())

for i in range(t):
    my_50000 = 0
    my_10000 = 0
    my_5000 = 0
    my_1000 = 0
    my_500 = 0
    my_100 = 0
    my_50 = 0 
    my_10 = 0

    ans_list = [0 for _ in range(8)]

    my_money = int(input())

    my_money 

    while my_money != 0 :
        if my_money // 50000 != 0:
            ans_list[0] += my_money // 50000
            my_money -= 50000 * ans_list[0]
        elif my_money // 10000 != 0:
            ans_list[1] += my_money // 10000
            my_money -= 10000 * ans_list[1]
        elif my_money // 5000 != 0:
            ans_list[2] += my_money // 5000
            my_money -= 5000 * ans_list[2]
        elif my_money // 1000 != 0:
            ans_list[3] += my_money // 1000
            my_money -= 1000 * ans_list[3]
        elif my_money // 500 != 0:
            ans_list[4] += my_money // 500
            my_money -= 500 * ans_list[4]
        elif my_money // 100 != 0:
            ans_list[5] += my_money // 100
            my_money -= 100 * ans_list[5]
        elif my_money // 50 != 0:
            ans_list[6] += my_money // 50
            my_money -= 50 * ans_list[6]
        elif my_money // 10 != 0:
            ans_list[7] += my_money // 10
            my_money -= 10 * ans_list[7]
        elif my_money //1 != 0 :
            break
    
    print(f"#{i+1}")
    for j in ans_list:
        print(j, end = " ")
    print("")