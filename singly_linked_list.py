class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=' -> ')
    currentNode = currentNode.next

print('null')


# Transving a singly linked list
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data)
        currentNode = currentNode.next
    print('null')

traverseAndPrint(node1)