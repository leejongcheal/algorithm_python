def DFS(line):
    global result
    idx = len(line)
    if idx == k+1:
        result.append(line)
        return
    for i in range(10):
        if str(i) not in line:
            if sign[idx-1] == "<" and line[idx-1] < str(i):
                DFS(line+str(i))
            elif sign[idx-1] == ">" and line[idx-1] > str(i):
                DFS(line+str(i))


k = int(input())
sign = list(input().split())
result = []
for i in range(10):
    DFS(str(i))
print(max(result))
print(min(result))
