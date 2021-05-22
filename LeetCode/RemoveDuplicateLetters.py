
'''
给你一个字符串 s ，请你去除字符串中重复的字母，
使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）
示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
'''
class rRemoveDuplicateLetters:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c not in stack:
                # 当前字符比栈顶字符小，并且后面还会出现这个字符，则把它pop之后等后面再append
                while stack and c < stack[-1] and stack[-1] in s[i:]:
                    stack.pop()
                stack.append(c)
        return "".join(stack)
        pass