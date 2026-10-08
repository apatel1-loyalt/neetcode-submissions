class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.first = Node(-1)
        self.last = Node(-1)

        # Point First Node to Last
        self.first.next = self.last

        # Point Last Node to First
        self.last.prev = self.first

    def isEmpty(self) -> bool:
        return self.first.next == self.last

    def append(self, value: int) -> None:
        # Add Node the end of the queue
        new_node = Node(value)

        # Point New Node to last one
        new_node.next = self.last

        old_last_pre = self.last.prev
        new_node.prev = old_last_pre
        old_last_pre.next = new_node
        
        self.last.prev = new_node

        
    def appendleft(self, value: int) -> None:
        # Add node the start of the queue
        new_node = Node(value)

        # Point new node pre to the first node
        new_node.prev = self.first

        old_first_next = self.first.next
        self.first.next = new_node

        new_node.next = old_first_next
        old_first_next.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1 
        
        last_node = self.last.prev
        prev_node = last_node.prev
        value = last_node.val

        self.last.prev = prev_node
        prev_node.next = self.last

        return value


    def popleft(self) -> int:
        if (self.first.next != self.last):
            tmp = self.first.next
            self.first.next = tmp.next
            tmp.next.prev = self.first
            return tmp.val
        return -1
        
