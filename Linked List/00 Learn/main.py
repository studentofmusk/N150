class Node:
    def __init__(self, data:int, next=None) -> None:
        self.data:int = data
        self.next:Node = next

class LinkedList:
    def __init__(self):
        self.head:Node = None

    def append(self, data):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
        
        else:
            self.head = Node(data)
    
    def pop(self) -> int:
        if self.head:
            prev, curr = None, self.head

            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            
            return curr.data
    
    def print(self)->None:
        curr:Node = self.head
        while curr:
            print(curr.data)
            curr = curr.next


l1:LinkedList = LinkedList()
l1.append(4)
l1.append(5)
l1.append(9)
print("After Append:")
l1.print()

print("POP Element:")
print(l1.pop())
print("After POP():")
l1.print()