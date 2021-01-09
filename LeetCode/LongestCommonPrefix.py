from typing import List

"""
输入：strs = ["flower","flow","flight"]
输出："fl"

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for temp in zip(*strs):
            # ('f', 'f', 'f')
            # ('l', 'l', 'l')
            # ('o', 'o', 'i')
            # ('w', 'w', 'g')
            if len(set(temp)) == 1:
                res += temp[0]
            else:
                break
            print(temp)
        pass

    """
    计算sub子串在在str字符串中出现的次数
    python中的count()函数，从字面上可以
    str.count(sub, start= 0,end=len(string))
    参数
        sub -- 搜索的子字符串
        start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
        end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

    """
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        res = ""
        min_str = min(strs, key=len)
        for idx_min in range(len(min_str)):
            idx_s = ""
            # 取出数组每个索引对应的字符
            for s in strs:
                idx_s += s[idx_min]
            # 计算字符s[idx_min]在 idx_s中出现的的次数
            idx_s_c = idx_s.count(s[idx_min])
            if idx_s_c == len(strs):
                res += s[idx_min]
            else:
                break
        return res
        pass


print(Solution().longestCommonPrefix1(["flower", "flow", "flight"]))