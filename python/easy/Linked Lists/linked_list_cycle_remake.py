class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#2 solutions, hash, two pointer

def hashset(head: ListNode) -> bool:
    seen = set()
    #Set curr to first node
    current = head

    while current:
        #Cycle found
        if current in seen:
            return True

        seen.add(current)
        current = current.next

    return False

def two_pointer(head: ListNode) -> bool:
    #The idea is that fast moves 2 nodes a time,
    #as slow loops through first cycle fast finishes 2 and they overlap
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False