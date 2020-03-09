dic = dict()
dic[0] = [1,0]
dic[1] = [0,1]


def fi2(n):
    global dic
    if dic.get(n,0) != 0:
        return dic.get(n)
    else:
        num = [fi2(n-1)[0]+fi2(n-2)[0],fi2(n-1)[1]+fi2(n-2)[1]]
        dic[n] = num
        return num


t = int(input())
for i in range(t):
    a = fi2(int(input()))
    print(a[0],a[1])
