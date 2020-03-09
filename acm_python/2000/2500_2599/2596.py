# C = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
# R = ["A", "B", "C", "D", "E", "F", "G", "H"]
def check(s):
    for c in dic.keys():
        dif = 0
        for i in range(6):
            if s[i] != c[i]:
                dif += 1
        if dif == 1:
            return c
    return -1


dic = {'000000': 'A', '001111': 'B', '010011': 'C', '011100': 'D', '100110': 'E', '101001': "F", '110101': 'G',
       '111010': "H"}
N = int(input())
S = input()
ans = ""
for i in range(0,N*6, 6):
    # print(str(dic.get(S[i:i+6],-1)),S[i:i+6],i)
    if dic.get(S[i:i+6],-1) == -1:
        g = check(S[i:i+6])
        if g == -1:
            print(i//6+1)
            exit()
        else:
            ans += dic[g]
    else:
        ans += dic[S[i:i+6]]
print(ans)

