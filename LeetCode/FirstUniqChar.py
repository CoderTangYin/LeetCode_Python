
"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

s = "leetcode"
返回 0
s = "loveleetcode"
返回 2

"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        # 统计每个字符出现的次数 直接转成字典
        charCountDict = dict(collections.Counter(s))
        arr = []
        # 从字典中取出字符出现一次的的字符并找出它在字符串的位置返回
        for keyChar in charCountDict:
            if charCountDict[keyChar] == 1:
                arr.append(keyChar)
        for i in range(len(s)):
            if s[i] in arr:
                return i
        return -1
    pass

    def firstUniqChar1(self, s: str) -> int:
        valueIdx = -1
        for idx in range(len(s)):
            val = s[idx]
            idxl = idxr = idx
            lhasRes = False
            rhasRes = False
            while idxl - 1 >= 0:
                idxl -= 1
                if s[idxl] == val:
                    lhasRes = True
                    break
                    pass
            if lhasRes == False:
                while idxr + 1 < len(s):
                     idxr += 1
                     if s[idxr] == val:
                         rhasRes = True
                         break
                     pass
                pass
            if lhasRes == False and rhasRes == False:
                valueIdx = idx
                break
            pass
        return valueIdx
        pass
    pass
# print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar1("loveleetcode"))