d = "CAMBRIDGE"
s = input()
i = 0
ans = ""
for i in s:
    if i not in d:
        ans += i
print(ans)
