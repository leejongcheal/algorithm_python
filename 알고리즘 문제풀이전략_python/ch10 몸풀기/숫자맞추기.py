import random
a = random.randint(0,9)
i = 0
print("0부터 9까지의 숫자를 입력하세요.")
while True:
    i += 1
    b = int(input("[%d번쨰 도전] : "%i))
    if a == b:
        print("우와! 정확하다. {}번쨰 만에 맞췄군요".format(i))
        break
    elif a > b:
        print("{}보다 큽니다".format(b))
    else:
        print("{}보다 작습니다".format(b))
