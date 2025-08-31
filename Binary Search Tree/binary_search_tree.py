class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class binarySearchTree:
    def __init__(self):
        self.root = None
    def Insert(self,node,data):
        if not node:
            return Node(data)
        else:
            if data < node.data:
                node.lchild = self.Insert(node.lchild,data)
            elif data > node.data:
                node.rchild = self.Insert(node.rchild,data)
            return node
    def preOrderTrav(self,node):
        if node:
            print(node.data,end=" ")
            self.preOrderTrav(node.lchild)
            self.preOrderTrav(node.rchild)
    def inOrderTrav(self,node):
        if node:
            self.inOrderTrav(node.lchild)
            print(node.data,end=" ")
            self.inOrderTrav(node.rchild)
    def postOrderTrav(self,node):
        if node:
            self.postOrderTrav(node.lchild)
            self.postOrderTrav(node.rchild)
            print(node.data,end=" ")


x = int(input("Enter the number of elements in the binary search treee : "))
bt = binarySearchTree()
for i in range(x):
    data = int(input("\nEnter the value of the node : "))
    bt.root = bt.Insert(bt.root,data)

print("Pre Order Traversal of the binary tree : ")
bt.preOrderTrav(bt.root)

print("\nIn Order Traversal of the binary tree : ")
bt.inOrderTrav(bt.root)

print("\nPost Order Traversal of the binary tree : ")
bt.postOrderTrav(bt.root)