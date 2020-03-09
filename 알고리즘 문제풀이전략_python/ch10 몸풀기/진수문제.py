print("10진수->16진수 변환 프로그램이다")
print("10진수를 16진수로 바꾸려면 [A]키 아니면 [B]키를 누르세요.")
s = input("a 나 b를 누르세요: ")
if s == 'a':
    a = int(input())
    print("%x"%a)
else:
    a = (input())
    print(int(a,16))
