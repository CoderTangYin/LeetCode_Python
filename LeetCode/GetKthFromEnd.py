from LeetCode.ListNode import ListNode
'''
链表中倒数第k个节点
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5
'''
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
        利用快慢指针思想
        先让快指针走K步 之后快慢一起走 等快指针的下一节点为none时候 慢指针就是
        从后边倒数要删除的节点头结点
        :param head:
        :param k:
        :return:
        """
        fast = slow = head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        pass

def createNode():
    tail = dummyHead = ListNode(-1)
    for val in range(1, 6):
         node = ListNode(val)
         tail.next = node
         tail = node
    return dummyHead.next

root = Solution().getKthFromEnd(createNode(), 2)
while root:
    print(root.val)
    root = root.next

