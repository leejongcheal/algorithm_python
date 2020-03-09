s = input()
old = s[0]
res = 10
for c in s[1:]:
    if c == old:
        res += 5
    else:
        res += 10
        old = c
print(res)
