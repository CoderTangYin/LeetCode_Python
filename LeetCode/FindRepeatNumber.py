
'''
找出数组中重复的数字
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
'''
from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        return self.method2(nums)
    def method1(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        res = []
        for i in range(1, len(nums)):
            if prev == nums[i]:
                res.append(prev)
            prev = nums[i]
        return res
        pass

    def method2(self, nums: List[int]) -> int:
        x = set()
        res = []
        for i, value in enumerate(nums):
            if value in x:
                res.append(value)
                continue
            x.add(value)
        return res

print(Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))

