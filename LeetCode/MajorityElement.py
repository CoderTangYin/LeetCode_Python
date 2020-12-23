
"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

"""
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        出现的次数超过数组length/2,排完序一定会出现在
        中间位置
        :param nums:
        :return:
        """
        nums.sort()
        return nums[int(len(nums) >> 1)]
        pass


print(Solution().majorityElement([3,2,3]))