n = int(input())
x = input()
y = input()
if n%2 == 0:
    if x == y:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
else:
    for i in range(len(x)):
        if x[i] == y[i]:
            print("Deletion failed")
            exit()
    print("Deletion succeeded")
