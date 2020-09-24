# Implement the following for Stack:
# Perform Stack operations using Array implementation.
class Stack:
    def __init__(self,data=[]):
        self.data = []

    def is_empty(self):
        self.len_data = len(self.data)
        return self.len_data

    def push(self,elememt):
        self.data.append(elememt)

    def pop(self):
        if self.is_empty():
            print("Array is empty")
        else:
            self.data.pop()

    def top_element(self):
        print("Top element of stack : ",self.data[-1])

    def display(self):
        print(self.data)
        print(self.is_empty())

stackOperation = Stack()
stackOperation.display()
stackOperation.push(23)
stackOperation.push(45)
stackOperation.push(12)
stackOperation.display()
stackOperation.top_element()
stackOperation.pop()
stackOperation.display()
stackOperation.pop()
stackOperation.pop()
stackOperation.display()
stackOperation.pop()



