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
    current = head
    for _ in range(target):
        current = current.next
    current.next = current.next.next

    return head

if __name__ == '__main__':
    head = LinkNode(1)
    head.next = LinkNode(2)
    head.next.next = LinkNode(3)
    head.next.next.next = LinkNode(4)
    head.next.next.next.next = LinkNode(5)
    remove_nth_from_end(head, 2)
    print(head.val)