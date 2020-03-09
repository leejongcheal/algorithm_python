N, P = map(int,input().split())
data = [N]
r = (N*N)%P
while r not in data:
    data.append(r)
    r = (r*N)%P
i = data.index(r)
print(len(data) - i)

