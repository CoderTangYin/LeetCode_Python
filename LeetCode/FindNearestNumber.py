
"""
输入12345，返回12354

输入12354，返回12435

输入12435，返回12453

"""
import array
import copy
class Solution:
    def findNearestNum(self, arr: array) -> array:
        idx = self.__findTransferPoint(arr)
        if idx == 0: return None
        arrCopy = copy.copy(arr)
        self.__exchangeHead(arrCopy, idx)
        self.__reverse(arrCopy, idx)
        return arrCopy
        pass

    # ①寻找逆序区域 返回逆序区域的前一位 作为数组交换的边界
    def __findTransferPoint(self, arr: array) -> array:
        i = len(arr)-1
        while i>0:
            if arr[i] > arr[i-1]:
                return i
            i -= 1
        return 0
        pass
    # ②对①中index对应的数跟刚好比他大的数进行交换 如果 12354 执行后的结果为12453（但这个结果不是仅仅比他大的
    # 整数12435）
    def __exchangeHead(self, arr: array, idx: int) -> array:
        head = arr[idx-1]
        i = len(arr) - 1
        while i > 0:
            if head < arr[i]:
                arr[idx-1] = arr[i]
                arr[i] = head
                break
            i -= 1
            return arr
        pass

    # 把逆序的区域转换成正序的顺序
    def __reverse(self, arr: array, idx: int) -> array:
        i = idx
        j = len(arr)-1
        while i<j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        return arr

        pass
    pass


print(Solution().findNearestNum([1, 2, 3, 4, 5]))