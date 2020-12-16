import sys
a = int(sys.stdin.readline().rstrip())

if a >= 0:
    print('plus')
else:
    print('minus')
if a%2 == 0:
    print('even')
else:
    print('odd')