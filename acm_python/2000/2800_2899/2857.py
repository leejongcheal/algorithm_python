res =[]
for i in range(1,6):
    if input().find("FBI") != -1:
        res.append(i)
if len(res) == 0:
    print('HE GOT AWAY!')
else:
    print(" ".join(map(str,res)))
