t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    score_map = [list(map(int, input().split())) for _ in range(n)]

    rank_map = []
    for idx, j in enumerate(score_map):
        score = 0.35*j[0] + 0.45*j[1] + 0.2*j[2]

        rank_map.append((score,idx+1))

    rank_map.sort(key = lambda x:-x[0])

    for idx, j in enumerate(rank_map):
        student_rank = idx // (len(rank_map) // 10)
        if j[1] == m:
            if student_rank ==0:
                print(f"#{i+1} A+")
            elif student_rank == 1:
                print(f"#{i+1} A0")
            elif student_rank ==2:
                print(f"#{i+1} A-")
            elif student_rank == 3:
                print(f"#{i+1} B+")
            elif student_rank ==4:
                print(f"#{i+1} B0")
            elif student_rank == 5:
                print(f"#{i+1} B-")
            elif student_rank ==6:
                print(f"#{i+1} C+")
            elif student_rank == 7:
                print(f"#{i+1} C0")
            elif student_rank ==8:
                print(f"#{i+1} C-")
            elif student_rank == 9:
                print(f"#{i+1} D0")