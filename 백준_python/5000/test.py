cases = []
# 입력 받아서 저장
while True:
    line = input()
    if line == '0 0 0':
        break
    else:
        cases.append(list(map(int, line.split())))

for i in range(len(cases)):
    case = cases[i]
    print('Triangle #%d' % (i+1))
    x = case.index(-1)
    xname = chr(x + 97) # 0a 1b 2c
    if x == 2:
        ans = (case[0]**2 + case[1]**2) ** 0.5 #
    else:
        # 빗변이 나머지 한 변보다 작다면 Impossible
        if max(case[0], case[1]) >= case[2]:
            print('Impossible.\n')
            continue
        ans = (case[2]**2 - case[1-x]**2) ** 0.5 #
    print('%s = %.3f\n' % (xname, ans))
