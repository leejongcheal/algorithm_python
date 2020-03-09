L = [sum(map(int,input().split())) for _ in range(5)]
score = max(L)
print(L.index(score)+1, score)