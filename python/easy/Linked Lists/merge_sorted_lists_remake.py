class ListNode:
    def __init__(self, val):
        self.x = val
        self.next = None

#Iteration, recursion

def iteration(list1: ListNode, list2: ListNode) -> ListNode:
    #Placeholder for the head of the list
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.x <= list2.x:
            current.next = list1
            list1 = list1.next

        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1

    if list2:
        current.next = list2

    return dummy.next

def recursion(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1 or not list2:
        return list1 or list2

    if list1.x <= list2.x:
        list1.next = recursion(list1.next, list2)
        return list1

    else:
        list2.next = recursion(list2.next, list1)
        return list2

if __name__ == '__main__':
    testcase1 = ListNode(1)
    testcase1.next = ListNode(2)
    testcase1.next.next = ListNode(4)
    testcase2 = ListNode(1)
    testcase2.next = ListNode(3)
    testcase2.next.next = ListNode(4)
    #print(iteration(testcase1, testcase2))
    print(recursion(testcase1, testcase2))
    print()