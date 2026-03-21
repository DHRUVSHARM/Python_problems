"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.


capacity = 2
size = 1
hashmap counter (key) -> (freq usage) 

1 : 1

map 
freq -> dll (lru mru)


freq -> {
    map , key : node

} , lru , mru 

node has the value 

                    b        f
lru <-> element - e2    =     e4 - mru
                                            
                                 

// insert logic , connect the element front and back , then connect the front and back to the element 
// front , back : last 2 elements 

element.prev = back
element.next = front
back.next = element
front.prev = element

// delete logic 
// node pointer given back , front = n.prev, n.next 
node.prev = None
node.next = None
back.next = front
front.prev = back 

max_count = 1
lowest count= 1

1 : lru , mru


# get 

# check elese -1
# otherwise get value 
# after getting , delete and move it to the increased frequencey insert (automatically inserts as mru )
# increase the max_count if it increases 

# put
# cap exceed after out, 1


int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
simple cache check , return the value 

void put(int key, int value)
Update the value of the key if present, 
or inserts the key if not already present. 


When the cache reaches its capacity, 
it should invalidate and remove the least frequently used key before inserting a new item.
For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, 
a use counter is maintained for each key in the cache. 
The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

"""

class DLLNode:
    def __init__(self, prev=None , next=None , val=-1 , key=-1):
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 # current size
        self.lower_freq_bound = 0 # lowest key in metadata map
        self.upper_freq_bound = 0 # the highest key in metadata map 

        # we will need usage freq map 
        # key -> usage freq 
        # the initial check of membership will go through this 
        self.freq = {}

        # we also need to map the freq to the metadata (key -> node map , lru, mru to manage the dll)
        self.freq_metadata_map = {}

    # insert , delete functions
    # manage only ops on the dll here
    # manage the metadata, and the membership check outside 
    def insert(self , back , front, node):
        # no need to return the node 
        node.prev = back
        node.next = front
        back.next = node
        front.prev = node

    def delete(self, back , front , node):
        # we will return the removed node 
        node.next = None
        node.prev = None
        back.next = front
        front.prev = back

        return node
    
    def insert_lfu(self , key_freq , node):
        # create entry if not exist 
        if key_freq not in self.freq_metadata_map:
            new_node_map , new_lru , new_mru = {} , DLLNode() , DLLNode()
            new_lru.next = new_mru
            new_mru.prev = new_lru
            self.freq_metadata_map[key_freq] = (
                new_node_map,
                new_lru,
                new_mru
            )
        
        # the node will now be inserted into the new_key_freq
        node_map , lru , mru = self.freq_metadata_map[key_freq]
        node_map[node.key] = node
        self.insert(mru.prev , mru , node)

    def get(self, key: int) -> int:
        if key not in self.freq:
            return -1
        
        # we have the key 
        key_freq = self.freq[key]
        # we access the prev data 
        node_map , lru , mru  = self.freq_metadata_map[key_freq]
        # get the key value first
        node , value = node_map[key] , node_map[key].val
        # process the cache 
        # delete from current place 
        node = self.delete(node.prev , node.next , node)
        # pop from node map
        node_map.pop(key)
        # check if now empty 
        if len(node_map) == 0:
            # current frequency is finished
            self.freq_metadata_map.pop(key_freq)
            # adjust 
            if key_freq == self.lower_freq_bound:
                self.lower_freq_bound += 1
            if key_freq == self.upper_freq_bound:
                self.upper_freq_bound += 1
  
        # [1 , 2 , 4 , 10]
        # 1 empty move to next hole
        # if 10, move to next hole
        # [1 , 1]
        new_key_freq = key_freq + 1
        # now push to the new freq 
        self.freq[key] = new_key_freq
        self.insert_lfu(new_key_freq , node)

        return value        


    def pop_lfu(self):
        """
        pop the lru from the lowest frequency 
        """
        node_map , lru , mru = self.freq_metadata_map[self.lower_freq_bound]
        node = self.delete(lru , lru.next.next , lru.next)
        node_map.pop(node.key)
        self.freq.pop(node.key) # remove from freq map 

        if len(node_map) == 0:
            self.freq_metadata_map.pop(self.lower_freq_bound)


    def put(self, key: int, value: int) -> None:
        
        
        if key in self.freq:
            # update the node and delete it to get the node with new freq 
            key_freq = self.freq[key]
            node_map , lru , mru = self.freq_metadata_map[key_freq]
            node_map[key].val = value # update the value 
            node = node_map[key]
            node = self.delete(node.prev , node.next , node)
            node_map.pop(key) # remove the node from the current map

            # adjust limits
            if len(node_map) == 0:
                # current frequency is finished
                self.freq_metadata_map.pop(key_freq)
                # adjust 
                if key_freq == self.lower_freq_bound:
                    self.lower_freq_bound += 1
                if key_freq == self.upper_freq_bound:
                    self.upper_freq_bound += 1

            # new_key_freq 
            new_key_freq = key_freq + 1
            self.freq[key] = new_key_freq

            # insert the node in the lfu 
            self.insert_lfu(new_key_freq , node)

        else:
            # need to insert, check capacity and adjust if needed 
            if self.size == self.capacity:
                # print("self size , cap : " , self.size , " : " , self.capacity)
                self.pop_lfu()
                self.size -= 1
            
            new_key_freq = 1
            self.freq[key] = new_key_freq

            # only lower cache moves, unless they were same 
            temp = self.lower_freq_bound
            self.lower_freq_bound = 1
            if temp == self.upper_freq_bound:
                self.upper_freq_bound = self.lower_freq_bound

            # create node
            node = DLLNode(val=value,key=key)

            # insert into the lfu 
            self.insert_lfu(new_key_freq , node)

            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)