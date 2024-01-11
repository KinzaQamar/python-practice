def factorial(n):
    '''
    ** Calculates the factorial of a number
    ** Only calculates factorial of natural number
    ** Factorial of 0 is 1
    '''
    fact = 1
    if( n == 0 ) :
        return 1
    else :
        for i in range(n, 1, -1):
            fact *= i
        return fact
    
num = int(input("Enter the number : "))
print(f"The factorial of {num} is",factorial(num))
# print(factorial.__doc__)