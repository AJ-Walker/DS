#Write a program to store the elements in 1-D array and provide an option to perform 
#the operatons like searching, sorting, merge_eling, reversing the elements.

class ArrayOperations:
    def __init__(self, arr):
        self.array = arr
    def search(self, e):
        if e in self.array:
            return True
        return False

    def sort(self):
        for i in range(len(self.array)):
            lowest_index = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[lowest_index]:
                    lowest_index = j
            self.array[i], self.array[lowest_index] = self.array[lowest_index], self.array[i]
        return self.array

    def merge_el(self,l):
        self.array = self.array + l
        return self.array

    def reverse(self):
        return self.array[::-1]

arr = [34,67,12,89,23,90]
array1 = ArrayOperations(arr)
print(array1.sort())
print(array1.search(89))
print(array1.merge_el([56,43,21,87]))
print(array1.reverse())