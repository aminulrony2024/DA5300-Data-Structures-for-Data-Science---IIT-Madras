class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def delete_node(self,key):
        if key == self.head.data:
            temp = self.head
            self.head = temp.next
            temp = None
            return
        prev = None
        temp = self.head
        while temp and temp.data is not key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("The element is not found")
            return
        prev.next = temp.next
        temp = None

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


ll = LinkedList()

x = int(input("Enter the initial size of the linked list: "))
 
print("Enter the node's :  ")
for i in range(x):
    x = int(input())
    ll.append(x)

print("The element's of the linked list are : ")

ll.print_ll()

print("\nNow, append an element in front of the linked list : ")

print("Enter the element : ")
x = int(input())

ll.prepend(x)

print("Linked list after adding the element in front of the linked list : ")

ll.print_ll()

print("\nEnter a node to delete from the linked list : ")
key = int(input())
ll.delete_node(key)

print("Linked list after deleteing a partiulcar node : ")
ll.print_ll()