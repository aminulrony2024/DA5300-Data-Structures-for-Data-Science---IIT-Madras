class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def Insert(self,data):
        new_node = Node(data)
        if not self.root :
            self.root = new_node
            return
        queue = [self.root]

        while queue :
            temp = queue.pop(0)
            if not temp.lchild:
                temp.lchild = new_node
                return
            else:
                queue.append(temp.lchild)
            if not temp.rchild:
                temp.rchild = new_node
                return
            else:
                queue.append(temp.rchild)
        
    def preOrder(self,node):
        if node:
            print(node.data,end=" ")
            self.preOrder(node.lchild)
            self.preOrder(node.rchild)
    def inOrder(self,node):
        if node:
            self.inOrder(node.lchild)
            print(node.data,end=" ")
            self.inOrder(node.rchild)
    def postOrder(self,node):
        if node:
            self.postOrder(node.lchild)
            self.postOrder(node.rchild)
            print(node.data,end=" ")


bt = BinaryTree()

n = int(input("Enter total nodes of the binary tree : "))
print("Enter the node of the binarty tree : ")

for i in range(n):
    data = int(input())
    bt.Insert(data)

print("Pre Order traversal of the binary tree : ")
bt.preOrder(bt.root)

print("\nIn Order traversal of the binary tree : ")
bt.inOrder(bt.root)

print("\nPost Order traversal of the binary tree:")
bt.postOrder(bt.root)