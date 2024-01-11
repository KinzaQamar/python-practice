def factorial(n):
    '''
    ** Calculates the factorial of a number
    ** Only calculates factorial of natural number
    ** Factorial of 0 is 1
    '''
    if( n == 0 ) :
        return 1
    else :
        return n * factorial(n-1)
    
num = int(input("Enter the number : "))

print(factorial.__doc__)
print(f"The factorial of {num} is",factorial(num))
