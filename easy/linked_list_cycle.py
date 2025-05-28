class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    passed_nodes = set()
    if not head:
        return False
    while head.next is not None:
        if head.val not in passed_nodes:
            passed_nodes.add(head.val)
            head = head.next
            continue
        return True
    return False