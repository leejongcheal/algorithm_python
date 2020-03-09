A, B = map(int, input().split())
C, D = map(int, input().split())
L = [A/C + B/D,C/D + A/B,D/B+C/A,B/A+D/C]
m = max(L)
print(L.index(m))
