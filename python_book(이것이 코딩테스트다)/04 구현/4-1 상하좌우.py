n = int(input())
L = list(input().rstrip().split())
point = [0,0]
for c in L:
    if c =="L":
        if point[1]-1>= 0:
            point[1] -= 1
    elif c =="R":
        if point[1]+1 < n:
            point[1] += 1
    elif c == "U":
        if point[0]-1 >= 0:
            point[0] -= 1
    elif c == "D":
        if point[0]+1 <n:
            point[0] += 1
print(point[0]+1,point[1]+1)