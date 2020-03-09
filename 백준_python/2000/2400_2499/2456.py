import sys

N = int(input())
dic = {1: 0, 2: 0, 0: 0, (1, 3): 0, (2, 3): 0, (0, 3): 0, (1, 2): 0, (2, 2): 0, (0, 2): 0, (0, 1): 0, (1, 1): 0,
       (2, 1): 0}
nameList = sys.stdin.read().splitlines()
for idx in range(N):
    x, y, c = map(int, nameList[idx].split())
    dic[0] += x
    dic[1] += y
    dic[2] += c
    dic[(0, x)] += 1
    dic[(1, y)] += 1
    dic[(2, c)] += 1
m_v = max(dic[0],dic[1],dic[2])
ind =[-1,-1,-1]
for i in range(3):
    if dic[i] == m_v:
        ind[i] = 1
if ind.count(-1) == 2:  # 겹치는게 없는경우
    print(ind.index(1)+1,m_v)
elif ind.count(-1) == 1:  # 2개 겹치는경우
    x = ind.index(1)
    y = ind.index(1,x+1)
    if dic[(x,3)] > dic[(y,3)]:
        print(x+1,m_v)
    elif dic[(x,3)] < dic[(y,3)]:
        print(y+1,m_v)
    else:  # 3갯수도 겹치는경우
        if dic[(x, 2)] > dic[(y, 2)]:
            print(x+1, m_v)
        elif dic[(x, 2)] < dic[(y, 2)]:
            print(y+1, m_v)
        else:  # 후보 결정못하는경우
            print(0,m_v)

else:  #  3개 겹치는경우
    L = [dic[(0,3)],dic[(1,3)],dic[(2,3)]]
    m_t = max(L)
    t = L.count(m_t)
    if t == 1:  # 3의 갯수로 1개나오는 경우
        print(L.index(m_t)+1, m_v)
    elif t == 2: #  3의 갯수로 2개 나오는 경우
        x = L.index(m_t)
        y = L.index(m_t,x+1)
        if dic[(x, 2)] > dic[(y, 2)]:
            print(x + 1, m_v)
        elif dic[(x, 2)] < dic[(y, 2)]:
            print(y + 1, m_v)
        else:  # 후보 결정못하는경우
            print(0, m_v)
    else:  #  t == 3 인경우 2에대해서 위를 반복
        L = L = [dic[(0,2)],dic[(1,2)],dic[(2,2)]]
        m_t = max(L)
        t = L.count(m_t)
        if t == 1:
            print(L.index(m_t) + 1, m_v)
        else:
            print(0,m_v)
