from typing import List

"""
全排列：
给一个数组[1, 2, 3] 返回一个
[
 [1, 2, 3],
 [1, 3, 2],
 [2, 1, 3],
 [2, 3, 1],
 [3, 2, 1],
 [3, 1, 2],
]
"""
class Solution:
    resultList = []
    sumCount = 0
    def permList(self, list: List[int]) -> List[List[int]]:
        self.permutation(list, 0, len(list)-1)
        return self.resultList
        pass

    def permutation(self, list, left, right):
        if left == right:
            resArr = []
            for idx in range(len(list)):
                resArr.append(list[idx])
            self.resultList.append(resArr)
        else:
            idx = left
            while idx <= right:
                self.swap(list, left, idx)
                self.permutation(list, left + 1, right)
                self.swap(list, left, idx)
                idx += 1
        pass

    def swap(self,  list: List[int], i, j):
        if list[i] != list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp


print(Solution().permList([1, 2, 3]))
