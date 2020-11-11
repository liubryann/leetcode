class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while (head != None):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
