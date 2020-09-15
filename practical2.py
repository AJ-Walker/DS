#Implement Linked List. Include options for insertion, deletion, and search of a number,
#  reverse the list and concatenate two linked lists
class Node:

  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None
  
  def insertion(self, data):
    new_Node = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = new_Node
    else:
      self.head = new_Node

  def reverse(self):
      pass

  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

LL = LinkedList()
LL.insertion(3)
LL.insertion(4)
LL.insertion(5)
LL.printLL()