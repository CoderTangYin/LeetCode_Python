
#!/usr/bin/env python3

'''

有序数组的平方

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    	# 定义三个指针 指向头 尾 插入位置
    	l = 0
    	r = len(nums) - 1
        pos = len(nums) - 1
    	res = [0] * len(nums)
    	while l <= r:
    		l_val = nums[l] ** 2
    		r_val = nums[r] ** 2
    		if l_val > r_val:
    			res[pos] = l_val
    			l += 1
			else:
				res[pos] = r_val
				r -= 1
			pos -= 1	
    	return res	


res = Solution().sortedSquares([-4,-1,0,3,10])   
print(res)	
