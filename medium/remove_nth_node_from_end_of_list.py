class LinkNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_nth_from_end(head, n):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next

    if n == length:
        return head.next

    target = length - 1 - n
    #iterate to the node before the target node
    for _ in range(length):
        head = head.next
    head.next = head.next.next

    return head