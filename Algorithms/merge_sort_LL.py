class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeSort(head: ListNode) -> ListNode:
    # Base case: if head is None or there is only one element
    if not head or not head.next:
        return head

    # Step 1: Split the linked list into halves
    middle = getMiddle(head)
    next_to_middle = middle.next
    middle.next = None

    # Step 2: Recursively sort both halves
    left = mergeSort(head)
    right = mergeSort(next_to_middle)

    # Step 3: Merge the sorted halves
    sorted_list = sortedMerge(left, right)
    return sorted_list

def getMiddle(head: ListNode) -> ListNode:
    if not head:
        return head
    
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def sortedMerge(left: ListNode, right: ListNode) -> ListNode:
    if not left:
        return right
    if not right:
        return left

    if left.val <= right.val:
        result = left
        result.next = sortedMerge(left.next, right)
    else:
        result = right
        result.next = sortedMerge(left, right.next)
    
    return result
