from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left, right = [1]*N, [1]*N
        for i in range(1,N):
            left[i] = left[i-1] * nums[i - 1]
            right[N-1-i] = right[N - i] * nums[N - i]
        res = []
        for i in range(N):
            res.append(left[i] * right[i])
        return res

print(Solution().productExceptSelf([1,2,3,4]))