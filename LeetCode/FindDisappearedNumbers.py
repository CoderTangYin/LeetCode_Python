from typing import List

"""
范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字
输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arrLength = len(nums)
        x = set(nums)
        y = set([i for i in range(1, arrLength + 1)])
        return list(y-x)
        pass


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))