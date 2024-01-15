t = int(input())

for i in range(t):
    input_str = input()
    my_str = []
    for j in input_str:
        my_str.append(j)
    
    if my_str == my_str[::-1]:
        ans = 1
    else:
        ans = 0
    print(f"#{i+1} {ans}")