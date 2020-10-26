# Perform Queues operations using Circular Array implementation.

class CircularQueue():
    def __init__(self,size):
        self.size = size
        self.data = [None for i in range(size)]
        self.front = -1
        self.rear = -1
  
    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.data[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = data

    def dequeue(self):
        if (self.front == -1):
            print ("Queue is Empty")
        elif (self.front == self.rear):
            temp=self.data[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.data[self.front]
            self.front = (self.front + 1) % self.size
            return temp
  
    def display(self):
        if(self.front == -1):
            print ("Queue is Empty")
        elif (self.rear >= self.front):
            print("Elements in the circular queue are:",end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.data[i], end = " ")
        else:
            print ("Elements in Circular Queue are:",end=" ")
            for i in range(self.front, self.data):
                print(self.data[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.data[i], end = " ")

        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")

cq = CircularQueue(5)
cq.enqueue(23)
cq.enqueue(34)
cq.enqueue(12)
cq.enqueue(12)
cq.enqueue(67)
cq.enqueue(78)
cq.display()
cq.dequeue()
cq.display()