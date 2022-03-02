from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        c = Counter()
        res = 0
        for right, val in enumerate(s):
            c[val] += 1
            while right - left + 1 - c.most_common(1)[0][1] > k:
                c[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

s = "AAABCBCAABBBBCCC"
# print(Solution().characterReplacement("A",0))
print(Solution().characterReplacement(s,2))

