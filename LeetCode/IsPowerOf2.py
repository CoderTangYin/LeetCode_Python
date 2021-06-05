
"""
判断一个数是否是2的整数次幂
"""
class Solution:
    """
    0和1按位与运算的结果是0，所以凡是2的整数次幂和它本身减1的结果进行与运算，
    结果都必定是0。反之，如果一个整数不是2的整数次幂，结果一定不是0！
    """
    def isPowerOf2(self, num: int) -> bool:
        return (num & num-1) == 0
        pass
    pass


print(Solution().isPowerOf2(8)) # true
print(Solution().isPowerOf2(100)) # false