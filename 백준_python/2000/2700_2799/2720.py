for i in range(int(input())):
    n = int(input())
    x = n//25
    y = n % 25
    x1 = y//10
    y = y % 10
    print(x,x1,y//5,y%5)
