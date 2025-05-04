class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1

        # Determine the head of the merged list
        if list1.val <= list2.val:
            merged_head = list1
            merged_head.next = self.mergeTwoLists(list1.next, list2)
        else:
            merged_head = list2
            merged_head.next = self.mergeTwoLists(list1, list2.next)

        return merged_head



