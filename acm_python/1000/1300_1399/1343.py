S = input()
L = S.split(".")
# print(L)
temp = []
t = 0
for i in range(len(L)):
    if L[i] == "":
        continue
    if len(L[i]) % 2 != 0:
        print(-1)
        exit()
    else:
        if len(L[i]) % 4 == 0:
            temp.append("A"*(len(L[i])))
        else:
            s = "A"*(len(L[i])-2)
            s += "BB"
            temp.append(s)
result = ""
X = []
for i in range(len(S)):
    if S[i] == ".":
        X.append(i)
c = 0
idx = 0
for i in range(len(S)):
    if i in X:
        result += "."
        c = 0
    elif i not in X:
        if c == 0:
            result += temp[idx]
            idx += 1
            c = 1
        else:
            continue
print(result)

