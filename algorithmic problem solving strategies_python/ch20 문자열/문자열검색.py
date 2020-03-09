# H,N 문자열을 받아서 H에 N이 있으면 그수만큼 위치 반환
H = input()
N = input()
c = 0
if H.count(N) > 0:
    for i in range(H.count(N)):
        c = H.find(N, c) + 1
        print(c - 1)
