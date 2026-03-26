from typing import List

"""
Design a Binary Search Tree class.

You will design a Tree Map, 

which maps an integer key to an integer value. 

Your Tree class should support the following operations:

need bstnode
left, right, val (none defaults and val req )

TreeMap() will initialize an binary search tree map.
empty bst just the root 


void insert(int key, int val) will map the key to the value and insert it into the tree. - done

int get(int key) will return the value mapped with the key. If the key is not present in the tree, return -1.

int getMin() will return the value mapped to the smallest key in the tree. If the tree is empty, return -1.

int getMax() will return the value mapped to the largest key in the tree. If the tree is empty, return -1.

void remove(int key) will remove the key-value pair with the given key from the tree.

int[] getInorderKeys() will return an array of the keys in the tree in ascending order.




            10
     -1            20

null    1
            3
                4
                    6



"""

class BSTNode:

    def __init__(self , key , val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None
        
    def insert_helper(self, node , k , v):
        if node == None:
            return BSTNode(k , v) # insertion since this implies the node was not inserted 

        # we need to find the correct location 
        if k < node.key:
            # move to the left and connect the tree
            node.left = self.insert_helper(node.left , k , v)
        elif k > node.key:
            # move to right and connect the tree
            node.right = self.insert_helper(node.right , k , v)
        else:
            # the key already exists so we just update 
            node.val = v

        return node

    def search_helper(self, node , k):
        # try to find the key if found return value else -1
        if node == None:
            # not found
            return -1
        
        if k < node.key:
            return self.search_helper(node.left , k)
        elif k > node.key:
            return self.search_helper(node.right , k)
        else:
            return node.val
    
    def inorder_traversal(self, node , acc):
        if not node:
            return 
        self.inorder_traversal(node.left, acc)
        acc.append(node.val)
        self.inorder_traversal(node.right , acc)

    def get_min_helper(self, node):
        # find minimal key value, can get by getting the leftmost key of the tree
        curr = node
        while curr and curr.left:
            # while tree is not empty and we can stil move left
            curr = curr.left
        # return reference if empty tree then return None        
        return curr

    def get_max_helper(self, node):
        # can find the maximal key value by looking into the rightmost key of the tree
        curr = node
        while curr and curr.right:
            # tree is not empty and we can still move right 
            curr = curr.right
        return curr

    def delete_helper(self, node, k):
        # will find and delete the node with the correct key k if it exists 
        # we return the root of the tree with root node, and deleting k, if that k was found  
        if not node:
            return None 
        
        if k < node.key:
            node.left = self.delete_helper(node.left, k)
        elif k > node.key:
            node.right = self.delete_helper(node.right , k)
        else:
            # we have found the node
            # print("found : " , node.val , " to delete") 
            if not node.left and not node.right:
                return None
            elif node.left and node.right:
                # we will replace the val with the max node in the left part 
                # output will be some node and not -1 since we have checked that the left tree is not empty
                left_max = self.get_max_helper(node.left)
                node.val = left_max.val # change val
                node.key = left_max.key # change key as well
                node.left = self.delete_helper(node.left , node.key)
            elif node.left:
                return node.left
            else:
                return node.right
        
        return node

    def insert(self, key: int, val: int) -> None:
        # use the helper
        self.root = self.insert_helper(self.root , key , val)

    def get(self, key: int) -> int:
        # use the helper
        return self.search_helper(self.root , key)

    def getMin(self) -> int:
        min_node = self.get_min_helper(self.root)
        return -1 if min_node is None else min_node.val 

    def getMax(self) -> int:
        max_node = self.get_max_helper(self.root)
        return -1 if max_node is None else max_node.val

    def remove(self, key: int) -> None:
        # one approach could be to mark as -1 the key and then lazily push out or delete it ?
        # we will follow the more traditional recursive approach 
        self.root = self.delete_helper(self.root , key)


    def getInorderKeys(self) -> List[int]:
        # [] if empty , ie; the root is None 
        acc = []
        self.inorder_traversal(self.root , acc)
        return acc