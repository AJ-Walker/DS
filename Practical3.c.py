# Implement the following for Stack:
# WAP to scan a polynomial using linked list and add two polynomial. 

class PolyNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

class Polynomial:
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self.polyHead = None
        else:
            self.polyHead = PolyNode(degree, coefficient)
        self.polyTail = self.polyHead

    def degree(self):
        if self.polyHead is None:
            return -1
        else:
            return self.polyHead.degree

    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0
        newPoly = Polynomial()
        nodeA = self.polyHead
        nodeB = rhsPoly.polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                coefficient = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                coefficient = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                coefficient = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next

            newPoly.appendTerm(degree, coefficient)

        while nodeA is not None:
            newPoly.appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB is not None:
            newPoly.appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    def appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = PolyNode(degree, coefficient)
            if self.polyHead is None:
                self.polyHead = newTerm
            else:
                self.polyTail.next = newTerm

            self.polyTail = newTerm

    def printPoly(self):
        currentNode = self.polyHead
        while currentNode is not None:
            if currentNode.next is not None:
                print(f"{currentNode.coefficient}x^{currentNode.degree} + ")
            else:
                print(f"{currentNode.coefficient}x^{currentNode.degree}")
            currentNode = currentNode.next

if __name__ == "__main__":
    poly1 = Polynomial(2, 5) 
    poly1 += Polynomial(1, 3)
    poly1 += Polynomial(0, -10)
    print("First Polynomial : ")
    poly1.printPoly()
    poly2 = Polynomial(3, 2)
    poly2 += Polynomial(2, 4)
    poly2 += Polynomial(0, 3)
    print("Second Polynomial : ")
    poly2.printPoly()
    addPoly = poly1 + poly2
    print("The addition of the two polynomials is:")
    addPoly.printPoly()
