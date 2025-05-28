class LinkNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_nth_from_end(head, n):
    index = 0
    current = head
    while current is not None:
        index += 1
        current = current.next
    target = index - n
    if target == 0:
        return head.next

    index = 0
    #iterate to the node before the target node
    while index != target - 1:
        head = head.next
        index += 1

    head.next = head.next.next
    return head

