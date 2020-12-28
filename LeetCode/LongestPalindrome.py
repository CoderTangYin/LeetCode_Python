"""
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

"""
class Solution:
    """
    按回文情况是基数跟偶数的情况去处理
    """
    def longestPalindrome(self, s: str) -> str:
        palindrom = ""
        for idx in range(len(s)):
           #  基数个数
           temp = self.longestPalindromeIndex(s, idx, idx)
           if len(palindrom) < len(temp):
               palindrom = temp
           #   偶数个数
           temp1 = self.longestPalindromeIndex(s, idx, idx + 1)
           if len(palindrom) < len(temp1):
               palindrom = temp1
        return palindrom
        pass

    def longestPalindromeIndex(self, s: str, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
        pass


print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("babad"))
