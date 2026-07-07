class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4


def print_ll(head):
    curr = head
    while curr != None:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("Null")


def insert_at_head(val, head):
    new_node = Node(val)
    new_node.next = head
    return new_node


def insert_at_end(val, head):
    new_node = Node(val)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = new_node


def search(val, head):
    pass


print_ll(node_1)

new_head = insert_at_head(0, node_1)
insert_at_end(5, new_head)
insert_at_end(6, new_head)
insert_at_end(7, new_head)

print_ll(new_head)
