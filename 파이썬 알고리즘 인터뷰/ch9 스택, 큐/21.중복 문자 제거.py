from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 내 원래풀이보다 훨씬 깔끔함
        # 대신 fix and temp을 쓰지않고 stack으로 그냥 풀어버림
        counter = Counter(s)
        stack = []
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        return "".join(stack)


        # 화려한 재귀방법 -> 발상자체는 훌룡한데 이 발상을 내머리로는 절대못해
        # if not s:
        #     return ""
        # for char in sorted(set(s)):
        #     index = s.index(char)
        #     suffix = s[index:]
        #     if set(suffix) == set(s):
        #         return char + self.removeDuplicateLetters(suffix.replace(char,""))


# "cbacdcbc" "acdb"
# "bddbccd" "bcd"
# "bbcaac" "bac"
# "cdadabcc" "adbc"
s = "cbacdcbc"
print(Solution().removeDuplicateLetters(s))