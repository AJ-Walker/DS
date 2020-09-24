# Implement the following for Stack:
# WAP to calculate factorial and to compute the factors of a given no. 
# (i) using recursion, (ii) using iteration.

def factorial_num(num):
    fact = 1
    while (num>0):
        fact = fact * num
        num = num - 1
    return fact

def factorial_num_recursion(num):
    if num == 1:
        return num
    else :
        return num*factorial_num_recursion(num-1)


def factors_num(num):
    for i in range(1,num+1):
        if (num%i)==0:
            print(i, end =" ")

def factors_num_recursion(num,x):
    if x <= num:
        if (num % x == 0):
            print(x, end =" ")
        factors_num_recursion(num, x + 1)
        

num = 6
print(f"Factorial of {num} : {factorial_num(num)}")
print(f"Factorial of {num} using recursion : {factorial_num_recursion(num)}")
print(f"Factors of {num} : ")
factors_num(num)
print(f"\nFactors of {num} using recursion : ")
print(factors_num_recursion(num,1))