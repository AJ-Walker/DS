# Write a program for inorder, postorder and preorder traversal of tree.

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else :
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else :
                    self.right.insert(data)
            else:
                pass
        else:
            self.data = data

    def preorder(self):
        print("preorder : ", self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


    def inorder(self):
        if self.left:
            self.left.inorder()
        print("inorder : ",self.data)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print("postorder : ",self.data)

    def PrintTree(self):
        print(self.data)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

tree = Node(25)
tree.insert(23)
tree.insert(45)
tree.insert(8)
tree.insert(29)
tree.insert(46)
tree.PrintTree()
tree.preorder()
tree.inorder()
tree.postorder()