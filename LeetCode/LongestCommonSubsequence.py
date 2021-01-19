"""
最长公共子序列
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。

"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        if n1 * n2 == 0: return 0
        dp = [0 for _ in range(n2 + 1)]
        res = ""
        for i in range(1, n1 + 1):
            pre = 0
            for j in range(1, n2 + 1):
                # 取出以j结尾的最长长度
                temp = dp[j]
                # 拿第一字符串的第一个字符跟第二字符串的字符一一比对
                # 其实是计算以第二个字符串每个字符结尾出现的公共子序列
                # 最大值
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = pre + 1
                    # 记录相同的子序列 ..
                    # if not res.find(text1[i-1]):
                    #     res += text1[i-1]
                else:
                    # 不相同则是取当前的跟当前的前一个 记录以当前结尾的最大值
                    dp[j] = max(dp[j - 1], dp[j])
                # 下一次记录之前的出现的最大的值
                pre = temp
        print(res)
        return dp[-1]
        pass

print(Solution().longestCommonSubsequence("abcrrt", "abcccc"))
# print(Solution().longestCommonSubsequence("abcde", "ace"))