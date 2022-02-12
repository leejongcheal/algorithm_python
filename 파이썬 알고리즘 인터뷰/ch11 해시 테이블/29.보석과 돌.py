from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freq = Counter(S)
        count = 0
        for char in J:
            count += freq[char]
        return count

print(Solution().numJewelsInStones("aAc", "aAAbbbb"))