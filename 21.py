# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstNode = None
        
        if (l1 == None):
            return l2 
        
        elif (l2 == None):
            return l1
            
        else:   
            if (l1.val > l2.val):
                firstNode = l2
                firstNode.next = Solution.mergeTwoLists(self, l1, l2.next)
                
            elif (l1.val <= l2.val): 
                firstNode = l1
                firstNode.next = Solution.mergeTwoLists(self, l1.next, l2)
                
        return firstNode