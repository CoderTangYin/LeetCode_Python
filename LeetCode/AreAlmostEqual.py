'''
**
 * 仅执行一次字符串交换能否使两个字符串相等
 *
 * 示例 1：
 *
 * 输入：s1 = "bank", s2 = "kanb"
 * 输出：true
 * 解释：例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"
 * 示例 2：
 *
 * 输入：s1 = "attack", s2 = "defend"
 * 输出：false
 * 解
'''

class AreAlmostEqual:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        if not s1 or not s2: return False
        difCount = 0
        difS1 = difS2 = ""
        for index in range(len(s1)):
            if difCount > 2: return False
            if s1[index] != s2[index]:
                difCount += 1
                difS1 += s1[index]
                difS2 += s2[index]
        return difS1 == difS2[::-1]
        pass


print(AreAlmostEqual().areAlmostEqual("bank", "kanb"))