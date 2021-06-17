class Solution:
	# 递归
	def reverseList(self, head: ListNode) -> ListNode:
		# 传入的节点为空 传入结点下一个为空 说明是最后一个了
		if head == None or head.next == None: return head
		newHead =  self.reverseList(head.next)
		head.next.next = head
		head.next = None
		return newHead

	# 迭代	
	def reverseList(self, head: ListNode) -> ListNode:
		# 传入的节点为空 传入结点下一个为空 说明是最后一个了
		if head == None or head.next == None: return head
		newHead = None
		while head != None:
			temp = head.next
			head.next = newHead
			newHead = head
			head = temp
			pass
		return newHead	
			
	pass