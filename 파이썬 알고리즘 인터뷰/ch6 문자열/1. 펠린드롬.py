import re
s = input()
s = s.lower()
# 1
# 문자에 대해서 char.isalnum()을 이용해서 숫자 or 문자인지 판별 가능
# 2
s = re.sub('[^a-z0-9]','',s)
# \w 는 숫자 + 알파벳문자를 뜻함 [a-zA-Z0-9]
# s = re.sub("[\W]","",s)
# 3
# L_s = re.findall("[\w]", s)
# s = "".join(L_s)
print(s == s[::-1])