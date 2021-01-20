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
                else:
                    # 不相同则是取当前的跟当前的前一个 记录以当前结尾的最大值
                    dp[j] = max(dp[j - 1], dp[j])
                # 下一次记录之前的出现的最大的值
                pre = temp
        return dp[-1]
        pass

    def lcsLength(self, x, y):
        m = len(x) + 1
        n = len(y) + 1
        # 存放箭头方向
        b = [[0 for i in range(n)] for j in range(m)]
        # 存放数值
        c = [[0 for i in range(n)] for j in range(m)]
        # 已经全部初始化为 0 了   上↑  左←  左上↖
        for i in range(1, m):
            for j in range(1, n):
                # 数组第一个 元素 下标为 0
                if x[i - 1] == y[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1;
                    b[i][j] = '↖'
                elif c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = '↑'
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = '←'
        return c, b

    def printLcs(self, b, x, i, j):
        if i == 0 or j == 0:
            return
        if b[i][j] == '↖':
            self.printLcs(b, x, i - 1, j - 1)
            print(x[i - 1], end='')
        elif b[i][j] == '↑':
            self.printLcs(b, x, i - 1, j)
        else:
            self.printLcs(b, x, i, j - 1)

# print(Solution().longestCommonSubsequence("abcrtot", "ambcrtotu"))
# print(Solution().longestCommonSubsequence("abcde", "ace"))

x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
y = ['B', 'D', 'C', 'A', 'B', 'A']
sol = Solution()
c,b = sol.lcsLength(x,y)
sol.printLcs(b,x, len(x), len(y))