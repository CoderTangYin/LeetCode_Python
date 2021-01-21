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

    def maxSubArray1(self, nums: List[int]) -> int:
        if not nums: return -1
        max_val = tem_max = pre = nums[0]
        for index in range(1, len(nums)):
            if pre <= 0:
                tem_max = pre = nums[index]
            else:
                pre += nums[index]
                tem_max += nums[index]
            if tem_max > max_val: max_val = tem_max
        return max_val
        pass

    def maxSubArray2(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return -1
        # 保存以某个索引结束的最大值 默认每个都是0
        dp = [0 for _ in range(len(nums))]
        # 假设以第一个结尾的就是最大的值
        dp[0] = nums[0]
        maxVal = dp[0]
        for index in range(1, len(nums)):
            # 如果前面的小于0 以当前结尾的最大值只能
            # 是自己
            if dp[index-1] <= 0:
                dp[index] = nums[index]
            else:
                # 前面的大于0 自己+前面=以自己结尾的最大的
                dp[index] = dp[index-1] + nums[index]
            maxVal = max(dp[index], maxVal)
            print(dp)
        return maxVal
        pass

print(Solution().maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



