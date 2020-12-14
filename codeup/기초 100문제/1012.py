import sys
a = float(sys.stdin.readline().rstrip())
print("%f"%a)
# print(a)
# 그냥 a로 출력했을때 소수점 뺴먹어서 틀림
# %f , a 차이 %f는 소수점 6자리까지 출력함