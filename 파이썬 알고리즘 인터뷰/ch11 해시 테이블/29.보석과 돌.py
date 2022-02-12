from collections import defaultdict
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freq = defaultdict(int)
        count = 0
        for char in S:
            freq[char] = freq[char] + 1
        for char in J:
            count += freq[char]
        return count


print(Solution().numJewelsInStones("aA", "aAAbbbb"))