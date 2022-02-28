from typing import List


# [3,3] 6인 경우 이렇게 풀면 복잡하게 연산이 있어야함
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i,val in enumerate(nums):
            dic[val] = i
        nums.sort()
        start, end = 0, len(nums) - 1
        while start < end:
            now = nums[start] + nums[end]
            if now == target:
                if dic[nums[start]] != dic[nums[end]]:
                    a = min(dic[nums[start]],dic[nums[end]])
                    b = max(dic[nums[start]],dic[nums[end]])
                    return [a, b]
            elif now < target:
                start += 1
            elif now > target:
                end -= 1

L = [3,2,4]
print(Solution().twoSum(L,6))