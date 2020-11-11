class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast != None:
            fast = fast.next
            if (fast != None):
                fast = fast.next
            slow = slow.next
        
        prev = None
        curr = slow 
        while curr != None:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next 
        
        while prev != None:
            if (head.val != prev.val):
                return False
            prev = prev.next
            head = head.next
        return True
        
