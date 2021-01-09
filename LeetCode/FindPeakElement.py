"""
输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < nums[mid +1]:
                left = mid + 1
            else:
                right = mid
        return left
        pass

    def findPeakElement1(self, nums: List[int]) -> int:
        res = {}
        for idx in range(1, len(nums)-1):
            print(idx)
            if nums[idx] > nums[idx-1] and nums[idx] > nums[idx+1]:
                res[nums[idx]] = idx
        print(res)
        pass

print(Solution().findPeakElement1([1, 2, 1, 3, 5, 6, 4]))
