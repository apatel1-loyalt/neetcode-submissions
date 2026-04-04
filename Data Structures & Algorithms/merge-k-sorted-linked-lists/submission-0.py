# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Edge condition
        if not lists or len(lists) == 0:
            return None
        
        # Loop whole lists has more then 2 members
        while len(lists) > 1:

            mergedLists = []

            # Merge 2 Linked List at a time for the
            for i in range(0, len(lists), 2):

                lst1 = lists[i]
                lst2 = lists[i+1] if i + 1 < len(lists) else None

                # Sort the Merged LinkedList
                mergedLists.append(self.mergeList(lst1, lst2))

            # Add it as a lists
            lists = mergedLists

        return lists[0]


    def mergeList(self, l1, l2):

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Add the remaining list
        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next



