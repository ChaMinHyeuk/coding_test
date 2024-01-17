import sys

sys.stdin = open('./input.txt')

t = int(input())

for i in range(t):
    p, q, r, s, w = map(int, input().split())

    result_a = p*w
    result_b = 0
    
    if w > r:
        result_b += r*q
        result_b += s*(w-r)
    else:
        result_b = w*q
    print(f"#{i+1} {min(result_a, result_b)}")
    