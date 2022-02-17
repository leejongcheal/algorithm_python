from typing import List
class Solution:
    @staticmethod
    def to_swap(n1: int, n2 : int):
        return str(n1) + str(n2) > str(n2) + str(n1)
    def largestNumber(self, nums: List[int]) -> str:
        N = len(nums)
        for i in range(1, N):
            j = i
            while j > 0 and self.to_swap(nums[j], nums[j-1]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return str(int("".join(map(str,nums))))

L = [3,30,34,5,9]
ans = Solution().largestNumber(L)
print(ans)