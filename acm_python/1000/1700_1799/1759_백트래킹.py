import sys
sys.setrecursionlimit(10**8)


def DFS(c,string,ja,mo):  # c는 이제 넣을 값을 뜻함 이렇게 해야 깔끔하고 좋음 배울것
    global l
    global N
    global w
    if len(string) == N:
        if ja >= 2 and mo >= 1:
            print(string)
        else:
            return
    for i in range(c,len(l)):
        if l[i] in w:
            DFS(i + 1,string+l[i],ja,mo + 1)
        else:
            DFS(i + 1, string + l[i], ja + 1, mo)


N,C = map(int,input().split())
l =[]
w = "aeiou"
result = []
r1 = []
l = list(input().split())
l.sort()  # 알파벳 순서로 들어가있음
DFS(0,"",0,0)
