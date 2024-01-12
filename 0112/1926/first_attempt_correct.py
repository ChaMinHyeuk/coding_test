n = int(input())

def count_3_6_9(number):
    cnt = 0
    for i in number:
        if i == "3" or i == "6" or i =="9":
            cnt+=1
    
    return cnt

my_arr = []
for i in range(1, n+1):

    number = str(i)
    cnt = count_3_6_9(number)

    if cnt == 0 :
        my_arr.append(number)
    elif cnt == 1:
        my_arr.append("-")
    elif cnt == 2:
        my_arr.append("--")
    else:
        my_arr.append("---")
    
print(' '.join(my_arr))

    
#재귀로도 풀어보자... 동적으로 할 수 있는 방법이 뭐가 있을까?