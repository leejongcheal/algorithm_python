h, m = map(int, input().split())
M = int(input())
H = M//60
M = M % 60
m +=M
if m >= 60:
    m -= 60
    h += 1
h += H
if h >=24:
    a = h//24
    h -= 24
print(h,m)
