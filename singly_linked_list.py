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

# traverseAndPrint(node1)

# Finding the lowest value in a singly linked list
def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

# print("Lowest value in the linked list: ", findLowestValue(node1))

# deleting a specific node
def deleteSpecificNode(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next
    
    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:    
        currentNode = currentNode.next

    if currentNode.next is None:
        return head
    
    currentNode.next = currentNode.next.next

    return head

node1 = deleteSpecificNode(node1, node4)

# print('Linked list after deletion')
# traverseAndPrint(node1)

# inserting a node
def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
    
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

newNode = Node(92)
node1 = insertNodeAtPosition(node1, newNode, 2)

traverseAndPrint(node1)