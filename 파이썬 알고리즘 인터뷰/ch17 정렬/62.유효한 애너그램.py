class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = "aab"
t = "baa"
print(Solution().isAnagram(s, t))