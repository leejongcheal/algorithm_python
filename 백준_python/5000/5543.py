import sys
name =[int(i) for i in sys.stdin.read().splitlines()]
print(min(name[0:3])+min(name[3:5])-50)
