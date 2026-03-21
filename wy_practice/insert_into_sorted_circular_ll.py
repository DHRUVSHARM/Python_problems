# Definition for a Node.
class Node:
  def __init__(self, val=None, next=None):
       self.val = val
       self.next = next


"""
head=[1,3,5]
insertVal=0

"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal , head)
            return head
        
        if head.next == head:
            new_node = Node(insertVal , head)
            head.next = new_node
            return head
        
        # atleast 2 nodes
        # non decreasing ----- keep going up then from behind down
        prev, curr , all_equal = head , head.next , True 
        while curr != head:
            
            if prev.val <= insertVal <= curr.val:
                # insert and break
                all_equal = True
                break

            if prev.val > curr.val:
                # drop at this point 
                if insertVal >= prev.val or insertVal <= curr.val:
                    all_equal = True
                    break
            
            prev = curr
            curr = curr.next
        
        new_node = Node(insertVal)
        prev.next = new_node
        new_node.next = curr

        return head
            
        

        
        
