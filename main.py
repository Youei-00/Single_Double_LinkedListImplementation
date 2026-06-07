# Exercise 1: Singly Linked List Implementation

# REAL-TIME USAGES OF LINKED LISTS:
# 1. Implementing undo/redo operations in text editors.
# 2. Managing browser history in web browsers.
# 3. Handling playlists in music players where new songs can be inserted or deleted dynamically.


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def StartInsert(self, data):
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode

    def EndInsert(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.nextNode:
            temp = temp.nextNode
        temp.nextNode = newNode

    def NodeInsert(self, item, data):
        temp = self.head
        while temp and temp.data != item:
            temp = temp.nextNode
        if not temp:
            print("Item not found.")
            return
        newNode = Node(data)
        newNode.nextNode = temp.nextNode
        temp.nextNode = newNode

    def Delete(self, data):
        temp = self.head

        if temp and temp.data == data:
            self.head = temp.nextNode
            return

        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.nextNode

        if not temp:
            print("Item not found.")
            return

        prev.nextNode = temp.nextNode

    def Traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.nextNode
        print("NULL")

    def Reverse(self):
        prev = None
        curr = self.head

        while curr:
            nextNode = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = nextNode

        self.head = prev

def main():
    print("\n=== Testing Singly Linked List (main) ===")

    slist = SinglyLinkedList()

    print("\nInserting at start: 10, 5")
    slist.StartInsert(10)
    slist.StartInsert(5)
    slist.Traverse()

    print("\nInserting at end: 20")
    slist.EndInsert(20)
    slist.Traverse()

    print("\nInserting 15 after 10")
    slist.NodeInsert(10, 15)
    slist.Traverse()

    print("\nDeleting 10")
    slist.Delete(10)
    slist.Traverse()

    print("\nReversing List")
    slist.Reverse()
    slist.Traverse()

if __name__ == "__main__":
    main()
