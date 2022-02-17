from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

s = "aab"
t = "baa"
print(Solution().isAnagram(s, t))