# 비교만 할꺼면 루트를 쓰기보단 d를 제곱하는게 더 시간적으로 좋다!
import sys, math


def calDir(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2
read =sys.stdin.readline
for _ in range(int(read())):
