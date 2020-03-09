h, m, s = map(int, input().split())
d = int(input())
h += d // 3600
d = d % 3600
m += d // 60
s += d % 60
if s >= 60:
    temp = s
    s = s - (s // 60) * 60
    m += temp // 60
while m >= 60:
    temp = m
    m = m - (m // 60) * 60
    h += temp // 60
while h >= 24:
    h = h - (h // 24) * 24
print(h, m, s)
