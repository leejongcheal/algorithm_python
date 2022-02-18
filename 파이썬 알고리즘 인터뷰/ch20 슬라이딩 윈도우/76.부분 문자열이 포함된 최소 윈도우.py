from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = 0
        end = -1
        for right, char in enumerate(s):
            ## BB AC인 경우에 BB에서 2번 뺴는 경우를 방지해야함
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                # 위의 경우에선 BBAC가 아닌 BAC까지 오게됨
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if  end == -1 or right - left<= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        if end == -1:
            return ""
        return s[start:end + 1]


# "aa", "a" -> ""// "a", "a" -> "a" 예외처리 ㅋㅋ

s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow("a", "a"))