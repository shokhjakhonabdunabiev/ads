'''
Linked List consist of nodes where each node had value and pointer to next value.
LinkedList has the following functionalities:
    - push
    - delete
    - pop
    - popfront
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":
    print("yo")