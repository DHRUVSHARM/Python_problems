"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


least           most
L                  M


# empty put 
L-M

1

insert op

             back   front
M.PREV   1   3      M

back.next = node
node.prev = back
front.prev = node
node.next = front 


delete op with node reference 

back    front
L - 1 - M

back.next = front
front.prev = back
# remove ref
node.prev = None
node.next = None


keys will be unique 
since if key exist, update
otherwise add  
update, add actions will move to the most side 

map

key : node pointer

"""

class DLLNode:
    def __init__(self, key , val , next=None, prev=None):
        self.key = key # reverse relation to pop out 
        self.val=val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity # fixed overall
        self.size = 0 # current size tracking
        self.least = DLLNode(float("inf") , float("inf")) # point to the least recently used , init to None
        self.most = DLLNode(float("inf") ,  float("inf")) # point to the most recently used , init to None
        self.key_mapping = {} # map the key value to the latest node also has the value (tracked using pointer)
        # initially we will keep L - M
        self.least.next = self.most
        self.most.prev = self.least

    def insert(self, node):
        # add the node to the end (at most)
        back , front = self.most.prev , self.most
        back.next = node
        node.prev = back
        front.prev = node
        node.next = front
        # update the size 
        self.size += 1 

    def remove(self , node):
        # remove the node using the reference 
        back , front = node.prev , node.next
        back.next = front
        front.prev = back
        # remove ref
        node.prev = None
        node.next = None
        # reduce size
        self.size -= 1

        # return the node for further op
        return node

    def get(self, key: int) -> int:
        # if key does not exist, return -1
        if key not in self.key_mapping:
            return -1
        
        # the key exists, and we need to move the accesed value to the most recently used and also return the value in the node
        # here the capacity does not change so no eviction 
        value_node = self.key_mapping[key]
        removed_node = self.remove(value_node)
        self.insert(removed_node)
        return removed_node.val

    def put(self, key: int, value: int) -> None:
        # if key exists , we update the value
        if key in self.key_mapping:
            value_node = self.key_mapping[key]
            # need to update the value in the node
            value_node.val = value # update 
            removed_node = self.remove(value_node)
            self.insert(removed_node)
        else:
            # create the key value pair 
            self.key_mapping[key] = DLLNode(key , value)
            value_node = self.key_mapping[key]
            self.insert(value_node)

            # check exceeds capacity 
            if self.size > self.capacity:
                # evict LRU cache 
                # node to remove will be next to the least 
                node_to_remove = self.least.next
                removed_node = self.remove(node_to_remove) # remove from DLL
                # pop from the hashmap
                self.key_mapping.pop(removed_node.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)