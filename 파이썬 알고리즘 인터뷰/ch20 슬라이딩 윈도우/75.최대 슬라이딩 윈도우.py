from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        now_max = -int(1e10)
        res = []
        left, right = 0, k - 1
        for _ in range(len(nums) - k + 1):
            # 계속 max해서 구하기보단 최근에 빠진값이 now_max였다면 해당 구간의 최댓값을 구하는식으로 시간효율
            # left가 0 인경우에도 nums[-1] 마지값은 어쩄든 최솟값보다 크니깐 인덱스범위 오류없이 잘들어감
            # 의도된 값은 아니니 틀렸다고 보겠음, 그렇다고 left > 0 을 넣어주면 처음에 구간최댓값구하는걸 못함
            if now_max <= nums[left - 1]:
                now_max = max(nums[left:right+1])
            else:
                now_max = max(nums[right],now_max)
            left += 1
            right += 1
            res.append(now_max)
        return res

L = [1,3,-1,-3,5,3,6,7]
print(Solution().maxSlidingWindow([1,2],1))