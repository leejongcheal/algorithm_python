dic = {}
L = list(map(int,list(input())))
for i in range(len(L)):
    if L[i] == 9:
        dic[6] = dic.get(6, 0) + 1
    else:
        dic[L[i]] = dic.get(L[i],0) + 1
max = 0
for i in dic.keys():
    if i == 6:
        if (dic[6]-1)//2 + 1 > max:
            max = (dic[6]-1)//2 + 1
    elif dic[i] > max:
        max = dic[i]
print(max)
