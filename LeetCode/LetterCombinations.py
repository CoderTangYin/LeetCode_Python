from typing import List

"""
组合出现次数问题
电话按键 2对应的英文字母a b c 3对应的英文字母d e f
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        [a,b,c]单个跟[d,e,f]匹配
        :param digits:
        :return:
        """
        dig_map = self.dig_letter_map()
        resultArr = [""]
        for num in digits:
            tempArr = []
            for char in dig_map[int(num)]:
                for val in resultArr:
                    tempArr.append(val + char)
                # ['a']
                # ['a', 'b']
                # ['a', 'b', 'c']
                # ['ad', 'bd', 'cd']
                # ['ad', 'bd', 'cd', 'ae', 'be', 'ce']
                # ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
                # ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
                # print(tempArr)
            resultArr = tempArr
        return resultArr
    def dig_letter_map(self):
        return {
            0:"0",
            1:"1",
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }

    def letterCombinations1(self, digits: str) -> List[str]:
        """
        队列解法
        :param digits:
        :return:
        """
        if not digits: return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit) - 50]:  # 这里我们不使用 int() 转换字符串，使用ASCII码
                    queue.append(tmp + letter)
        return queue



print(Solution().letterCombinations1("23"))