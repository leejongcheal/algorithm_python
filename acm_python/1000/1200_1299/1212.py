o ="0o"
n =(input())
if int(n) == 0:
    print(0)
    exit()
o = o + n
b = int(o,8)
b = bin(b)
print(str(b)[2:])