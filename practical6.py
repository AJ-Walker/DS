#WAP to sort a list of elements. Give user the option to perform sorting using Insertion sort, Bubble sort or Selection sort.
def insertion_sort(array):

    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item

    return array


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False
        if already_sorted:
            break

    return array

def selection_sort(array):
    for i in range(len(array)):
        minimum = i
        
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]
            
    return array

array = [45,89,23,98,5,78,32]
print("The list is : ",array)
#array = list(input("Enter your list : "))
print("Select 'I' for Insertion sort, 'B' for Bubble sort, 'S' for selection sort")
yourChoice = str(input("Your choice : "))

if yourChoice == "I":
    print("Insertion sort : ",insertion_sort(array))
elif yourChoice == "B":
    print("Bubble sort : ",bubble_sort(array))
else :
    print("Selection sort : ",selection_sort(array))