def check_groupnum(s):
    dic ={}
    l = len(s)
    for i in range(l):
        if i == 0:
            dic[s[i]] = 1
            continue
        if s[i] == s[i-1]:
            continue
        else:  # 새로운 단어인경우
            ch = dic.get(s[i], 0)
            if ch != 0:
                return -1
            else:
                dic[s[i]] = 1
    return 1
N = int(input())
result = 0
for i in range(N):
    S = input()
    a = check_groupnum(S)
    if a == 1:
        result += 1
print(result)