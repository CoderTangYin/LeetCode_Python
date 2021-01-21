from typing import List

"""
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        for num in nums:
            arr += [val + [num] for val in arr]
        return arr
        pass

print(Solution().subsets([1, 2, 3]))