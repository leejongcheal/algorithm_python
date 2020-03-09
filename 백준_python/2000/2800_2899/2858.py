r, b = map(int, input().split())
for i in range(1,b+1):
    if b%i == 0:
        if ((b//i)+2)*2 + i*2 == r:
            x = b//i + 2
            y = i+2
            if x < y:
                x ,y = y, x
            print(x,y)
            exit()
