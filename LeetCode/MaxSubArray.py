from typing import List

"""
输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return -1
        dp = [1]*len(nums)
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
            print(dp)
        return res
        pass


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



