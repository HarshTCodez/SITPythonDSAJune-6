class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("Null")

    def insert_at_end(self, val):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)

    def __contains__(self, target):
        curr = self.head
        while curr is not None:
            if curr.data == target:
                return True
            curr = curr.next
        return False


ll = LinkedList()
ll.insert_at_head(5)
ll.insert_at_head(4)
ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_end(10)
ll.print()


print(1 in ll)
print(2 in ll)
print(3 in ll)
