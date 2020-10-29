#Implement Linked List. Include options for insertion, deletion, and
#  search of a number,
#  reverse the list and concatenate two linked lists
class Node:
    def __init__(self, data,next = None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head 
        while(temp): 
            print(temp.data,end=" ") 
            temp = temp.next

    def insertion(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node:
            prev.next = current_node.next
            current_node = None
            return
        else:
            return

    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next
            count += 1
        return count

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None):
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev

    def search_list(self, data):
        count = 0
        pointer = self.head
        while pointer:
            if pointer.data == data:
                count += 1
            pointer = pointer.next
        print(f"\nNumber {data} is there in list")
        return count

def mergeLists(List_1, List_2):
        head_ptr = temp_ptr = Node(List_1)
        while List_1 or List_2:
            if List_1 and (not List_2 or List_1.data <= List_2.data):
                temp_ptr.next = Node(List_1.data)
                List_1 = List_1.next
            else:
                temp_ptr.next = Node(List_2.data)
                List_2 = List_2.next
            temp_ptr = temp_ptr.next
        return head_ptr.next

llist = LinkedList()
llist1 = LinkedList()
llist.insertion(56)
llist.insertion(5)
llist.insertion(34)
llist1.insertion(21)
llist1.insertion(78)
llist1.insertion(59)
print("Linked List : ")
llist.printList()
llist.search_list(5)
print("Deleting...")
llist.delete_node(34)
print("After deleting : ")
llist.printList()
print("\nReversing the list : ")
llist.reverse()
llist.printList()
print("\nMerging two linked list : ")
llist2 = LinkedList()
llist2.head = mergeLists(llist.head, llist1.head)
llist2.printList()
