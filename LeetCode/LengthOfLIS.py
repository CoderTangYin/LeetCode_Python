from typing import List

"""
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        以某个元素结尾的它前边的最长上升子序列
        :param nums:
        :return:
        """
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    # [1, 2, 1, 1, 1, 1, 1, 1]
                    # [1, 2, 2, 1, 1, 1, 1, 1]
                    # [1, 2, 3, 1, 1, 1, 1, 1]
                    # [1, 2, 3, 2, 1, 1, 1, 1]
                    # [1, 2, 3, 3, 1, 1, 1, 1]
                    # [1, 2, 3, 3, 2, 1, 1, 1]
                    # [1, 2, 3, 3, 3, 1, 1, 1]
                    # [1, 2, 3, 3, 4, 1, 1, 1]
                    # [1, 2, 3, 3, 4, 2, 1, 1]
                    # [1, 2, 3, 3, 4, 3, 1, 1]
                    # [1, 2, 3, 3, 4, 3, 1, 2]
                    # print(dp)
        print(dp)
        return max(dp)
        pass

    def lengthOfLIS1(self, nums: List[int]) -> List[int]:
        """
        以某个元素结尾的它前边的最长上升子序列
        :param nums:
        :return:
        """
        pass

    def lis(self, arr):
        n = len(arr)
        m = [0] * n
        for x in range(n - 2, -1, -1):
            for y in range(n - 1, x, -1):
                if arr[x] < arr[y] and m[x] <= m[y]:
                    m[x] += 1
            # [0, 0, 0, 0, 1, 0]
            # [0, 0, 0, 0, 1, 0]
            # [0, 0, 2, 0, 1, 0]
            # [0, 2, 2, 0, 1, 0]
            # [3, 2, 2, 0, 1, 0]
            print(m)
            max_value = max(m)
            result = []
            for i in range(n):
                if m[i] == max_value:
                    result.append(arr[i])
                    max_value -= 1
        return result

print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# arr = [0,1,0,3,2,3]
# print(Solution().lis(arr))
# print(Solution().lengthOfLIS1([10, 9, 2, 5, 3, 7, 101, 18]))