def distance_2(i,j):
    global L
    return (L[i][0] - L[j][0]) ** 2 + (L[i][1] - L[j][1]) ** 2


def inc(i,j):
    if (L[i][1]-L[j][1]) == 0:
        return "infinete"
    else:
        return abs((L[i][0]-L[j][0])/(L[i][1]-L[j][1]))


L = []
for i in range(3):
    L.append(list(map(int,input().split())))
if inc(0,1) == inc(1,2):
    print("X")
else:
    L = [distance_2(0,1),distance_2(1,2),distance_2(0,2)]
    i = L.index(max(L))
    c = L.pop(i)
    a = L.pop()
    b = L.pop()
    if a == b and b == c and a == c:  # 세변이 같은경우
        print("JungTriangle")
    elif a == b:  # 두 각이 같고 하나가 젤긴경우
        if a+b < c:
            print("Dunkak2Triangle")
        elif a+b == c:
            print("Jikkak2Triangle")
        else:
            print("Yeahkak2Triangle")
    elif a == c:  # 두각이같은데 가장긴변이 2개있는경우
        if a+c < b:
            print("Dunkak2Triangle")
        elif a+c == b:
            print("Jikkak2Triangle")
        else:
            print("Yeahkak2Triangle")
    elif b == c:
        if c+b < a:
            print("Dunkak2Triangle")
        elif c+b == a:
            print("Jikkak2Triangle")
        else:
            print("Yeahkak2Triangle")
    else:
        if a+b < c:
            print("DunkakTriangle")
        elif a+b == c:
            print("JikkakTriangle")
        else:
            print("YeahkakTriangle")
