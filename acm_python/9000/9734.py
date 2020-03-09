import sys,math
L = sys.stdin.read().splitlines()
res =[]
for idx in range(len(L)):
    all = ""
    nore = ""
    re = -1
    m = -1
    for i in range(len(L[idx])):
        if "0" <= L[idx][i] <= "9":
            if i == 0 and L[idx][i] == "0":
                continue
            all += L[idx][i]
            if re == -1:
                    nore += L[idx][i]
            if re != -1:
                re += 1
            if m != -1:
                m += 1
        elif L[idx][i] == ".":
            m += 1
        elif L[idx][i] =="(":
            re += 1
    if re != -1:
        if nore != "":
            a = int(all) - int(nore)
        else:
            a = int(all)
        b = int("9"*re+"0"*(m-re))
        c = math.gcd(a,b)
        a //= c
        b //= c
    else: # 순환소수 아닌경우
        a = int(all)
        b = 10**m
        c = math.gcd(a,b)
        a //= c
        b //= c
    res.append("{} = {} / {}".format(L[idx],a,b))

print("\n".join(res))




