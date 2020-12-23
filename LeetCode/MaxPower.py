
"""
最长的连续字符

示例 1：

输入：s = "leetcode"
输出：2
解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
示例 2：

输入：s = "abbcccddddeeeeedcba"
输出：5
解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/consecutive-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:
    def maxPower(self, s: str) -> (int, str):
        # 假设当前的字符就是最大的出现次数为1次
        maxCount = curCount = 1
        # 假设第一个是出现的最大次数的字符
        element = s[0]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                curCount += 1
                # 如果当前的小于最大的则element保存的是上一次最大次数
                # 的字符 大于的情况下才需要更新
                if curCount > maxCount:
                    element = s[i+1]
                maxCount = max(curCount, maxCount)
                pass
            else:
                curCount = 1
        return (maxCount, element)
        pass
print(Solution().maxPower("leetcode"))

