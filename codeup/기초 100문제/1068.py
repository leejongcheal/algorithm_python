import sys
a = int(sys.stdin.readline().rstrip())
if a >= 90:
    s = "A"
elif a >= 70:
    s = "B"
elif a >= 40:
    s = "C"
else:
    s = "D"
print(s)