"""
Docstring for waymo.lru_cache


int get(int key) 
Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

map :

key | val
1 : 1 (node)
2 :2 (node)

# get operation makes the get node as the recently used node
# put makes default recent, it will increase so we need to check and delete if required 

left    right
    3->4 null


"""


import collections

class Node:
    def __init__(self , key , value , prev=None , next=None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = collections.defaultdict()
        self.left = Node(-1 , -1)
        self.right = Node(-1 , -1)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    
    def swap(self, node , lmu ):

        pnode, nnode , plru , nlru = node.prev , node.next , lmu.prev , lmu.next
        node.next = nlru
        node.prev = plru
        nlru.prev = node
        plru.next = node

        lmu.prev = pnode
        lmu.next = nnode
        pnode.next = lmu
        nnode.prev = lmu

    def get(self, key: int) -> int:
        # return the value mapped if exists else -1
        if key in self.key_node:
            # update the recently used 
            # swap the node with the lmu
            node , lmu = self.key_node[key] , self.right.prev
            # swap
            self.swap(node , lmu)
            return self.key_node[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        # check if already present, no increase in capacity in this case
        if key in self.key_node:
            # overwrite the value, move to the lmu
            self.key_node[key].value = value
            # node, lmu
            node , lmu = self.key_node[key] , self.right.prev
            # swap
            self.swap(node , lmu)
            return
        
        # check if capacity is reached
        print(self.capacity , " : " , self.size)
        print(self.left.next.value)
        print(self.right.prev.value)

        if self.capacity == self.size:
            # evict lru

            self.size -= 1
            lru = self.left.next
        
            self.left.next = lru.next
            lru.next.prev = self.left
            lru.next = None
            lru.prev = None

            # we need to have a mapping from the node back to the to work , or maybe reuse logic can work 
            self.key_node.pop(lru.key)

        # ready to add the new node
        self.size += 1
        # we add to the map
        self.key_node[key] = Node(value , key)
        # put node between lmu and right
        lmu , node = self.right.prev , self.key_node[key]
        lmu.next = node
        self.right.prev = node
        node.prev = lmu
        node.next = self.right



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)