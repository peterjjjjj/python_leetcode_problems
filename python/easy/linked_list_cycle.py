class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    """
    time complexity: O(n)
    space complexity: O(n)

    :param head:
    :return:
    """
    passed_nodes = set()
    #set current to the starting node
    current = head

    while current is not None:
        if current in passed_nodes:
            return True
        passed_nodes.add(current)
        current = current.next
    return False

def has_cycle_fast_slow(head):
    """
    time complexity: O(n)
    space complexity: O(1)

    :param head:
    :return:
    """
    if not head:
        return False
    slow_pointer = head
    fast_pointer = head.next

    while fast_pointer is not None and fast_pointer.next is not None:
        if slow_pointer == fast_pointer:
            #they meet up, means that it is a circle
            return True
        #movee slow pointer up by 1, fast by 2
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return False