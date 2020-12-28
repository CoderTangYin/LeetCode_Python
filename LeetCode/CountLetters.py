
"""
给你一个字符串 S，返回只含 单一字母 的子串个数。

示例 1：

输入： “aaaba”
输出： 8
解释：
只含单一字母的子串分别是 “aaa”， “aa”， “a”， “b”。
“aaa” 出现 1 次。
“aa” 出现 2 次。
“a” 出现 4 次。
“b” 出现 1 次。
所以答案是 1 + 2 + 4 + 1 = 8。
示例 2:

输入： “aaaaaaaaaa”
输出： 55

"""
class Solution:
    def countLetters(self, S: str) -> int:
        totalCount = 0
        # 连续出现的次数
        continuityCount = 1
        S = S + "#"
        for idx in range(1, len(S)):
            if S[idx] == S[idx - 1]:
                continuityCount += 1
            else:
                print(continuityCount)
                # aaaba  1 + 2 + 3 + 1 + 1 本质是计算以某个下标结尾连续字符出现的次数 自己出现的情况连续为1
                # 1 + 2 + 3 可以看做是公差为1的等差数列 1 + 1可以看做是公差为0的等差数列
                # 比如求前三项和其实就是套公式（等差数列前N项和公式 sn = na1 + n(n-1)*d/2 ）
                # 3*1 + 3(3-1) * 1 / 2
                # 通过s3推导公式 套公式进行推导 n为3
                # s3 = n + n(n-1)/2 = (2n + n(n-1))/2 = (n(2+n-1))/2 = n(n+1)/2 进而得到下边的
                # 连续长度为n的相同元素的单个字符子串个数为：n(n + 1) / 2
                totalCount += continuityCount*(continuityCount + 1) >> 1
                continuityCount = 1
            pass
        return totalCount
        pass
print(Solution().countLetters("aaaba"))