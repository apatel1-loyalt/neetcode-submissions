class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.start_node = Node(0)
        self.count = 0
    
    def get(self, index: int) -> int:
        tmp = self.start_node.next

        for i in range(index):
            if tmp.next:
                tmp = tmp.next
            else:
                return -1

        if tmp:
            return tmp.val
        else:
            return -1
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        if self.start_node.next:
            tmp = self.start_node.next
            new_node.next = tmp
        
        self.start_node.next = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        tmp = self.start_node

        while tmp.next:
            tmp = tmp.next

        tmp.next = new_node

    def remove(self, index: int) -> bool:
        tmp = self.start_node.next
        pre = self.start_node

        if not tmp:
            return False

        for i in range(index):
            if tmp and tmp.next:
                pre = tmp
                tmp = tmp.next
            else:
                return False

        if tmp and not tmp.next:
            pre.next = None
            return True
        else:
            pre.next = tmp.next
            return True

        return False
        

    def getValues(self) -> List[int]:
        tmp = self.start_node.next
        ans = []

        while tmp:

            ans.append(tmp.val)

            tmp = tmp.next

        return ans