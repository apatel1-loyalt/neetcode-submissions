class Node:
    """ Double Linked List """
    
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache =  {} # Hash Map to store value
        
        # Left - LRU(Least used), right - Most Used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # We remove pointers to node
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert(self, node):
        # Add new node to right
        prv, nxt = self.right.prev, self.right
        prv.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prv

    def get(self, key: int) -> int:
        """Get  Member or -1"""

        # find the member
        if key in self.cache:

            # update the use and move to right
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            # Return the member
            return self.cache[key].value

        return -1
        

    def put(self, key: int, value: int) -> None:
        """ Update Cache to add new value or replace Least used member"""

        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if at capacity remove LRU Member 
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        