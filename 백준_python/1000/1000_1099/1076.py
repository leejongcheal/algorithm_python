dic = {"black":[0,1],"brown":[1,10], "red":[2,100]
       ,"yellow":[4,10000],"orange":[3,1000],"green":[5,100000],
       "blue":[6,1000000],"violet":[7,10000000],"grey":[8,100000000],
       "white":[9,1000000000]}
a = input()
b = input()
c = input()
n = dic[a][0]*10
n += dic[b][0]
n *= dic[c][1]
print(n)
