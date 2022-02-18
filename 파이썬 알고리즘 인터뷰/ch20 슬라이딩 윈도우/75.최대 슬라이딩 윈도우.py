from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        now_max = -int(1e10)
        res = []
        left, right = 0, k - 1
        for _ in range(len(nums) - k + 1):
            # 계속 max해서 구하기보단 최근에 빠진값이 now_max였다면 해당 구간의 최댓값을 구하는식으로 시간효율
            if now_max <= nums[left - 1]:
                now_max = max(nums[left:right+1])
            else:
                now_max = max(nums[right],now_max)
            left += 1
            right += 1
            res.append(now_max)
        return res

L = [1,3,-1,-3,5,3,6,7]
print(Solution().maxSlidingWindow(L,3))