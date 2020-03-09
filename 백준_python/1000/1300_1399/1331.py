def check_night(s,s1):
    m = ord(s[0]) - ord("A") + 1
    n = int(s[1])
    m1 = ord(s1[0]) - ord("A") + 1
    n1 = int(s1[1])
    if abs(m - m1) == 2 and abs(n - n1) == 1:
        return 1
    elif abs(m - m1) == 1 and abs(n - n1) == 2:
        return 1
    else:
        return 0


dic = {}
for i in range(36):
    s = input()
    if i == 0:
        start = s
        s1 = s
        dic[s] = 1
        continue
    b = check_night(s,s1)
    if b == 0 or dic.get(s,0) != 0:
        print("Invalid")
        exit()
    else:
        s1 = s
        dic[s] = 1
if check_night(s,start) == 0:
    print("Invalid")
else:
    print("Valid")