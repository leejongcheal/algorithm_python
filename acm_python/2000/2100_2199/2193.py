N = int(input())
dic ={1:1,0:0}
for i in range(1,N):
    temp = dic[1]
    dic[1] = dic[0]
    dic[0] = temp + dic[0]
print(dic[0]+dic[1])
