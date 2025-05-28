class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    passed_nodes = set()
    #set current to the starting node
    current = head

    while current is not None:
        if current in passed_nodes:
            return True
        passed_nodes.add(current)
        current = current.next
    return False