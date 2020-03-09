N = input()
N = N[::-1]
result = ""
for i in range(1,len(N)+1):
    if i % 3 == 1:
        s = int(N[i-1])
        if i == len(N):
            result = str(s) + result
    elif i % 3 == 2:
        s += int(N[i-1])*2
        if i == len(N):
            result = str(s) + result
    else:
        s += int(N[i-1])*4
        result = str(s) + result
print(result)