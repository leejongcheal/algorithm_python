import sys
N = int(input())
a =sys.stdin.read().splitlines()
dic = {}
for i in range(N):
    c = list(map(int,a[i].split()))
    if dic.get(c[0],0) == 0:
        dic[c[0]] = []
    dic[c[0]].append(c)
for i in dic.keys():
    dic[i].sort(reverse=True)
i = 0
result = 0
current_m = -1  # 실행중인 회의의 끝나는 시간 후에 이보다 빨리 끝나는게 잇다면 변경할것
idx = max(dic)
while idx >= i:
    if i == current_m:  # 끝남
        current_m = -1
    while dic.get(i,0) != 0 and dic.get(i,0) != []:
        c = dic[i].pop()
        if current_m == -1:  # 실행중인 회의를 넣어줘야함
            current_m = c[1]
            result += 1
        else:  #실행중인 회의 가있을떄
            if current_m > c[1]:
                current_m = c[1]
        if i == current_m:  # i,i 인경우 다시 넣어줘야하니
            current_m = -1
    i += 1
print(result)
