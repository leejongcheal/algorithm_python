class Solution:
    def lengthOfLongestSubstring(self, S: str) -> int:
        start = max_size = 0
        used = dict()
        for end, char in enumerate(S):
            if char in used.keys() and start <= used[char] < end:
                start = used[char] + 1
            else:
                max_size = max(max_size, end - start + 1)
            used[char] = end
        return max_size


print(Solution().lengthOfLongestSubstring("abcabcaa"))