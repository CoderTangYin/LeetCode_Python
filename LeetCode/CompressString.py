
"""
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
"""
class Solution:
    def compressString(self, S: str) -> str:
        prevStr = S[0:1]
        # 每个字符至少出现了一次
        count = 1
        temp = ""
        for index in range(1, len(S)+1):
            curS = S[index: index+1]
            if prevStr == curS:
                count += 1
            else:
                temp = temp + prevStr + str(count)
                count = 1
                prevStr = curS
        return temp
        pass


print(Solution().compressString("abbccd"))
