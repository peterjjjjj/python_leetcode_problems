class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        #basecase when reached the tail
        if not head or not head.next:
            return head

        #new_head is the tail
        new_head = self.reverseList(head.next)
        #head is the node before tail, tail.next is now pointing towards the head before it
        head.next.next = head

        head.next = None
        return new_head

