"""
无序数组排序后的最大相邻差
如：无序数组 2,3,1,4,6，排序后是1,2,3,4,6，最大差值是6-4=2
"""
import array
class Solution:
    # 计数排序思想解法
    def getMaxAdjustDifference(self, arr: array) -> int:
        # 1 求最值
        maxVal = max(arr)
        minVal = min(arr)
        # 2 初始化计数的数组 并统计过每个数字出现的次数
        countArr = [0 for _ in range((maxVal - minVal + 1))]
        for idx, val in enumerate(arr):
            countArr[arr[idx] - minVal] += 1
            pass
        count = maxCount = startIndex = endIndex = 0
        for idx1, val1 in enumerate(countArr):
            # 没有出现的数字 0填充的情况
            if val1 == 0:
                # 第一次出现 并标记它的起始位置是它的
                # 前一位，对出现的次数进行 +1 操作
                if count == 0:
                    startIndex = idx1 - 1
                count += 1
            else:
                count = 0
            #当前出现的次数大于之前出现的次数情况
            if count > maxCount:
                maxCount = count
                endIndex = idx1 + 1
        return endIndex - startIndex
        pass
    pass

    # 桶排序思想解法
    def getMaxSortedDistance(self, arr: array) -> int:
        # 内部桶类
        class Bucket:
            minV = maxV = 0
            pass

        # 1 求最值
        maxVal = max(arr)
        minVal = min(arr)
        dis = maxVal - minVal
        # 如果最大跟最小相等那就是没有 最大差值即为0
        if dis == 0: return 0
        # 2 初始化全部的桶
        buckets = [Bucket() for _ in range(len(arr))]
        for idx in range(len(arr)):
            # 确定该元素所属桶的下标 【这个有点难 不是很理解为什么这么做】
            elementIdx = int(((arr[idx] - minVal) * (len(arr) - 1)) / dis)
            if buckets[elementIdx].minV == 0 or buckets[elementIdx].minV > arr[idx]:
                buckets[elementIdx].minV = arr[idx]
            if buckets[elementIdx].maxV == 0 or buckets[elementIdx].maxV < arr[idx]:
                buckets[elementIdx].maxV = arr[idx]
        # 3
        curMaxVal = buckets[0].maxV
        maxDis = 0
        for idxBucket in range(1, len(buckets)):
            if buckets[idxBucket].minV == 0: continue
            if buckets[idxBucket].minV - curMaxVal > maxDis:
                maxDis = buckets[idxBucket].minV - curMaxVal
            curMaxVal = buckets[idxBucket].maxV
        return maxDis
        pass

# print(Solution().getMaxAdjustDifference([2, 6, 3, 4, 5, 10, 3]))
print(Solution().getMaxSortedDistance([2, 6, 3, 4, 5, 10, 3]))