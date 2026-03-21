
# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)
def cycleStart(head):
    if head is None:
        return None
    
    # first we can check if we have cycle 
    slow , fast = head , head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break

    if not fast or not fast.next:
        # cycle not found, we found end of list 
        return None
    
    # found intersection point 
    slow_new = head
    while slow_new != slow:
        slow_new = slow_new.next
        slow = slow.next
    
    return slow_new