# Exercise 2: Doubly Linked List Implementation

# REAL-TIME USAGES OF DOUBLY LINKED LISTS:
# 1. Navigating next/previous elements in image viewers.
# 2. Implementing LRU cache in operating systems.
# 3. Forward/backward navigation in applications.


class DNode:
    def __init__(self, data):
        self.data = data
        self.prevNode = None
        self.nextNode = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def StartInsert(self, data):
        newNode = DNode(data)
        newNode.nextNode = self.head
        if self.head:
            self.head.prevNode = newNode
        self.head = newNode

    def EndInsert(self, data):
        newNode = DNode(data)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.nextNode:
            temp = temp.nextNode
        temp.nextNode = newNode
        newNode.prevNode = temp

    def MiddleInsert(self, item, data):
        temp = self.head
        while temp and temp.data != item:
            temp = temp.nextNode
        if not temp:
            print("Item not found.")
            return

        newNode = DNode(data)
        newNode.nextNode = temp.nextNode
        newNode.prevNode = temp

        if temp.nextNode:
            temp.nextNode.prevNode = newNode

        temp.nextNode = newNode

    def Delete(self, data):
        temp = self.head

        if not temp:
            return

        if temp.data == data:
            self.head = temp.nextNode
            if self.head:
                self.head.prevNode = None
            return

        while temp and temp.data != data:
            temp = temp.nextNode

        if not temp:
            print("Item not found.")
            return

        if temp.prevNode:
            temp.prevNode.nextNode = temp.nextNode
        if temp.nextNode:
            temp.nextNode.prevNode = temp.prevNode

    def Traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.nextNode
        print("NULL")

    def Reverse(self):
        temp = self.head
        prevTemp = None

        while temp:
            prevTemp = temp.prevNode
            temp.prevNode = temp.nextNode
            temp.nextNode = prevTemp
            temp = temp.prevNode

        if prevTemp:
            self.head = prevTemp.prevNode


def main():
    print("\n=== Testing Doubly Linked List (main) ===")

    dlist = DoublyLinkedList()

    print("\nInserting at start: 10, 5")
    dlist.StartInsert(10)
    dlist.StartInsert(5)
    dlist.Traverse()

    print("\nInserting at end: 20")
    dlist.EndInsert(20)
    dlist.Traverse()

    print("\nInserting 15 after 10")
    dlist.MiddleInsert(10, 15)
    dlist.Traverse()

    print("\nDeleting 10")
    dlist.Delete(10)
    dlist.Traverse()

    print("\nReversing List")
    dlist.Reverse()
    dlist.Traverse()

if __name__ == "__main__":
    main()
