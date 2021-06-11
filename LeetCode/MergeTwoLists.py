# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
 合并2个有序链表
 输入：1->2->4, 1->3->4
 输出：1->1->2->3->4->4
'''
class Solution:
	'''
	迭代解法
	'''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    	if l1 == None: return l2
    	if l2 == None: return l1
    	# 使用虚拟头节点把整个链表串联起来
        dummyHead = ListNode(-1)
        tail = dummyHead
        while l1 != None && l2 != None:
        	if l1.val <= l2.val:
        		tail = tail.next = l1
        		l1 = l1.next
    		else:
    			tail = tail.next = l2
    			l2 = l2.next
        	pass
        if l1 == None: tail.next = l2
    	elif l2 == None: tail.next = l1
        	pass
    	pass

	'''
	递归解法
	'''
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
    	if l1 == None: return l2
    	if l2 == None: return l1
    	if l1.val <= l2.val:
    		'''
    		把l1当成一个整体返回 用l1的next去串联l1的next跟l2的链表
    		'''
    		l1.next = self.mergeTwoLists1(l1.next, l2)
    		return l1
    	else:
    		l2.next = self.mergeTwoLists1(l1, l2.next)
    		return l2
    	pass