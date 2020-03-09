import sys
N = int(input())
inputList = list(map(int, sys.stdin.read().splitlines()))
print(sum(inputList) - N + 1)
