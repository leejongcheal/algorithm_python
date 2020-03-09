import sys
dic = {1: '1', 2: '2', 3: '4', 4: '7', 5: '13', 6: '24', 7: '44', 8: '81', 9: '149', 10: '274'}
n = int(input())
res = [dic[int(i)] for i in sys.stdin.read().splitlines()]
print("\n".join(res))

