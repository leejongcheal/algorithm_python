from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        fix = []
        temp = []
        counter = Counter(s)
        for char in s:
            # 이미 fix에 있는 경우는 무시
            if char in fix:
                continue
            # 이미 temp에 있는경우 앞에 있는자리가 강력한 후보자리임
            # aba일때의 경우 temp a,b 이고 a의 갯수가 0이되는경우 체크
            elif char in temp:
                counter[char] -= 1
            # temp가 비거나 char 큰경우 마지막으로
            elif not temp or temp[-1] < char:
                temp.append(char)
                counter[char] -= 1
            # temp가 있을때, temp에 char보다 큰건 빼버리고 char을 넣어줌
            elif temp and temp[-1] > char:
                while temp and temp[-1] > char:
                    temp.pop()
                temp.append(char)
                counter[char] -= 1
            # 일단 갯수가 0이되면 자리를 확정해야함 temp 1,2,3,4 일때 현재 3이고 0의 갯수가 되면
            # 3의 자리를 확정해야하고 사전순을 지키기위해 1,2,3만 fix로 가야함
            if counter[char] == 0:
                index = temp.index(char)
                fix += temp[:index + 1]
                temp = temp[index + 1:]
        # 나머지 자리 확정못한 것들을 가능한 사전순으로 fix에 넣어줌
        fix += temp
        return "".join(fix)

# "cbacdcbc" "acdb"
# "bddbccd" "bcd"
# "bbcaac" "bac"
# "cdadabcc" "adbc"
s = "cbacdcbc"
print(Solution().removeDuplicateLetters(s))