"""
求2个数的最大公约数 效率最高的解法
"""
class Solution:
    def getGreatestCommonDivisor(self, a: int, b: int) -> int:
        if a == b: return a
        if a&1==0 and b&1==0:
            """
            a b 都是偶数 2 X (getGreatestCommonDivisor(a/2, b/2))
            2倍的递归函数 a/2 b/2
            """
            return self.getGreatestCommonDivisor(a>>1, b>>1)<<1
        elif a&1==0 and b&1!=0:
            """
            a偶 b奇 getGreatestCommonDivisor(a/2, b)
            谁是偶数谁就取一半 在跟奇数递归比较
            """
            return self.getGreatestCommonDivisor(a>>1, b)
        elif a&1!=0 and b&1==0:
            """
            a奇 b偶 getGreatestCommonDivisor(a, b/2)
            """
            return self.getGreatestCommonDivisor(a, b>>1)
        else:
            """
            都是奇数 先用更相减损术 getGreatestCommonDivisor(big-small, small)
            此时 big-small 一定是偶数
            """
            big = a if a>b else b
            small = b if a>b else a
            return self.getGreatestCommonDivisor(big-small, small)
        pass
    pass


print(Solution().getGreatestCommonDivisor(27, 14))
print(Solution().getGreatestCommonDivisor(20, 10))