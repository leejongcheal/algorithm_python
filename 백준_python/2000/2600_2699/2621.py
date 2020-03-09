L = [input() for _ in range(5)]  # 5개 0,3만 이용
# 1
a = [int(L[i][2]) for i in range(5)]
if L[0][0] == L[1][0] == L[2][0] == L[3][0] == L[4][0]:
    a.sort()
    if a[1] - a[0] == a[2] - a[1] == a[3] - a[2] == a[4] - a[3]:
        print(900+a[4])
        exit()
    else:  # 4
        print(600 + a[4])
        exit()
else:
    a.sort()
    # 5
    if a[1] - a[0] == a[2] - a[1] == a[3] - a[2] == a[4] - a[3]:
        print(500 + a[4])
        exit()
c_4 = 0
c_3 = 0
c_2 = 0
same_3 = -1
same_2 = []
same_4 = -1
for i in a:
    if a.count(i) == 4:
        same_4 = i
        c_4 = 1
    if a.count(i) == 3:
        c_3 = 1
        same_3 = i
    if a.count(i) == 2:
        c_2 += 1
        same_2.append(i)
# 2
if c_4 == 1 and same_4 != -1:
        print(800+same_4)
        exit()
# 3
if c_3 == 1 and c_2 != 0:
    print(10*same_3+same_2[0]+700)
    exit()
# 6
if c_3 == 1 and c_2 == 0:
    print(400+same_3)
    exit()
# 7
if c_2 >= 3:
    same_2 = set(same_2)
    same_2 = list(same_2)
    same_2.sort()
    print(10*same_2[1]+same_2[0]+300)
    exit()
# 8
if c_2 != 0 and c_2 < 3:
    print(200 + same_2[0])
    exit()
# 9
print(a[4]+100)
