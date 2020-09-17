#Write a program to search an element from a list. Give user the option to perform
#Linear or Binary search.

def LinearSearch(array, element_l):
    for i in range (len(array)):
        if array[i] == element_l:
            return i
    return -1

def BinarySearch(array, element_l):
    first = 0
    array.sort()
    last = len(array)-1
    done = False
    while (first <= last) and not done:
        mid = (first+last)//2
        if array[mid] == element_l:
            done = True
        else:
            if element_l < array[mid]:
                last = last - 1
            else:
                first = first + 1
    return done


array = [45,78,23,17,453,7]
print(array)
element_l = int(input("Enter the element you want to search : "))
print("Select 'L' for Linear Search and 'B' for Binary Search")
yourChoice = str(input("Enter your choice : "))

if yourChoice == 'L':
    
    result = LinearSearch(array, element_l)
    print(result)
    if result == 1:
        print("Element is present.")
    else :
        print("Element not present.")
else:
    result = BinarySearch(array, element_l)
    print(result)
    if result == -1:
        print("Element not present.")
    else :
        print("Element is present.")