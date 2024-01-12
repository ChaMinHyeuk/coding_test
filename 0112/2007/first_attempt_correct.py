t = int(input())

for i in range(t):
    my_string = input()
    cnt = 0
    for j in range(1, len(my_string)+1):
        my_word = my_string[0:j]
        second_word = my_string[j:(j*2)]
        cnt +=1
        if my_word == second_word:
            break
    print(f"#{i+1} {cnt}")

