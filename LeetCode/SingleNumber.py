"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
输入: [2,2,1]
输出: 1

"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        交换律：a ^ b ^ c <=> a ^ c ^ b
        任何数于0异或为任何数 0 ^ n => n
        相同的数异或为0: n ^ n => 0
        :param nums:
        :return:
        """
        a = 0
        for num in nums:
            """
            [2, 1, 2]
             2 = 0 ^ 2
             2 ^ 1 == 0 ^ 2 ^ 1
             2 ^ 1 ^ 2 = 0 ^ 2 ^ 1 ^ 2
             2 ^ 1 ^ 2 = 0 ^ 2 ^ 2 ^ 1
             
             res 1 
            """
            a = a ^ num
        return a
        pass

# 0^2^1^4^6^4^2^6
print(Solution().singleNumber([2, 1, 4, 6, 4, 2, 6]))