from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        cnt = Counter()
        for right in range(len(s)):
            cnt[s[right]] += 1
            max_char_n = cnt.most_common(1)[0][1]
            # 만족하지 못한경우
            if right + 1 - left - max_char_n > k:
                cnt[s[left]] -= 1
                left += 1
        return right + 1 - left

s = "AAABBC"
print(Solution().characterReplacement("A",0))

