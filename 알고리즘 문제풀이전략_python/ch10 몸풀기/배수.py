sum = 0
cnt = 0
print("1~1000 사이에서 선택한 수의 배수가 몇개이고 배수의 합은?")
a = int(input("수를 입력:"))
for i in range(a, 1001, a):
    cnt += 1
    sum += i
print(cnt, sum)
