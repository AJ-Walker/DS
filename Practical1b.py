# Write a program to perform the Matrix addition, Multiplication, and 
# Transpose Operation
a=str(input("Enter the  * for Multiplication Operation , + Adding Operation ,T for Transpose Operation :"))
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

if a== '+' :
    print("Adding Operation")
    def Adding_Matrix(X,Y):
        for i in range(len(X)):
            for j in range(len(X[0])):
                result[i][j] = X[i][j] + Y[i][j]
                
        for r in result:
            print(r)
            
    Adding_Matrix(X,Y)
    
elif a == '*':
    print(" Multiplication Operation")
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
                
    for r in result:
        print(r)
        
elif a == "t" or a == "T":
    print(" Transpose Operation")
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
            
    for r in result:
        print(r)
        
else:
    print("Enter valid input:")
