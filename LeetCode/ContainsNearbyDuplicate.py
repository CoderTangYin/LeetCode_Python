from typing import List

"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入: nums = [1,2,3,1], k = 3
输出: true

"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
         判断是存在num[i]==num[j]，存在的情况下才判断|i-j|<=k
        :param nums:
        :param k:
        :return:
        """
        if len(nums) <= 1:
            return False
        temp = {}
        for idx in range(len(nums)):
            if nums[idx] in temp:
                if idx - temp[nums[idx]] <= k:
                    return True
            temp[nums[idx]] = idx
        return False
        pass
print(Solution().containsNearbyDuplicate([1, 2, 3, 1], k=3))