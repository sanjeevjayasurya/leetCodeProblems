# Iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None 
        while(curr is not None):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        head = prev
        return head

    
# Recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest