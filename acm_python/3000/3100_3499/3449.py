import sys
t = int(input())
name = sys.stdin.read().splitlines()
res = ""
for idx in range(0,2*t,2):
    b = str(int(name[idx]) + int(name[idx+1]))
    res += "Hamming distance is {}.\n".format(b.count("1"))
print(res)



