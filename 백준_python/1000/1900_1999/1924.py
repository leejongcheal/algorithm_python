dic = {0:"SUN" , 1:"MON",2:"TUE",3:"WED",4:"THU",5:'FRI',6:"SAT"}
s_1 = [1,3,5,7,8,10]
s_0 = [2,4,6,9,11]
x,y = map(int,input().split())
if x == 1:
    print(dic[y % 7])
elif x == 2:
    print(dic[(y+31) % 7])
else:
    for i in range(1,x):
        if i in s_0:
            y += 30
        elif i in s_1:
            y += 31
    y -= 2
    print(dic[y % 7])
