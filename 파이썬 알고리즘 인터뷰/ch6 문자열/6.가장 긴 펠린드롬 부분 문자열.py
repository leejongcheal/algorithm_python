def expand(start, end):
    global S
    if end >= len(S):
        return ""
    while start >= 0 and end < len(S) and S[start] == S[end]:
        start -= 1
        end += 1
    return S[start + 1: end]

S = input()
res = ""
for i in range(len(S)):
    res = max(expand(i,i+1), expand(i,i+2), res, key = len)
print(res)

