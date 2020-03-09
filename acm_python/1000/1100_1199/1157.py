s = input().upper()
dic = dict()
for i in range(len(s)):
    dic[s[i]] = dic.get(s[i],0)+1
n = 0
m = 0
for i in dic.keys():
        if n == 0:
            m = i
            n = 1
        elif dic[i] > dic[m]:
            m = i
            n = 1
        elif dic[i] == dic[m]:
            n += 1
if n == 1:
    print(m)
else:
    print("?")
