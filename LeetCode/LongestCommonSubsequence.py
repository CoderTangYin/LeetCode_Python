"""
最长公共子序列
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。

"""
class Solution:
    x = set()
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = self.lcs(text1, len(text1), text2, len(text2))
        print(self.x)
        return res
        pass

    def lcs(self, text1: str, i, text2: str, j) -> int:
        """
        :param text1: 第一个字符串
        :param i: 第一个字符对应的索引
        :param text: 第二个字符串
        :param j: 第二个字符对应的索引
        :return: 当前相等字符出现的次数
        """
        if i == 0 or j == 0: return 0
        if text1[i-1] == text2[j-1]:
            self.x.add(text1[i-1])
            # 在当前自己的基础上 +1  返回所有相等的值 +1
            return self.lcs(text1, i-1, text2, j-1) + 1
        return max(self.lcs(text1, i-1, text2, j),
                   self.lcs(text1, i, text2, j-1))
        pass


print(Solution().longestCommonSubsequence("abcde", "ace"))


