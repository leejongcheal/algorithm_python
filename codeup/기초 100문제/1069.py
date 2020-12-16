import sys
a = sys.stdin.readline().rstrip()
if a == "A":
    s = "best!!!"
elif a == "B":
    s = "good!!"
elif a == "C":
    s = "run!"
elif a == "D":
    s = "slowly~"
else:
    s = "what?"
print(s)