class LinkNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_nth_from_end(head, n):
    """
    time complexity: O(2n)
    space complexity: O(1)
    :param head:
    :param n:
    :return:
    """
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

def remove_nth_from_end_slow_fast(head, n):
    """
    time complexity: O(L(size of list) - n(index from the end))
    space complexity: O(1)
    :param head:
    :param n:
    :return:
    """
    #set a dummy that is before the head
    dummy = LinkNode(-1000)
    dummy.next = head
    #initialize slow and fast
    slow = dummy
    fast = dummy
    #move fast to n places ahead of dummy
    for _ in range(n):
        fast = fast.next
    #interate fast to the end of the list, slow now points toward the node to remove
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    #dummy.next is the head
    return dummy.next

if __name__ == '__main__':
    head = LinkNode(1)
    head.next = LinkNode(2)
    remove_nth_from_end_slow_fast(head, 2)
    print(remove_nth_from_end_slow_fast(head, 2))