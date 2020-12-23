
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
        maxCount = curCount = 1
        element = ''
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                curCount += 1
                maxCount = max(curCount, maxCount)
                element = s[i]
                pass
            else:
                curCount = 1
        return (maxCount, element)
        pass


print(Solution().maxPower("leetcode"))

