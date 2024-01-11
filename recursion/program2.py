def fibonacci (limit) :
    '''
    ** Print the fibonacci sequence to the given limit
    '''
    
    if ((limit == 0) | (limit == 1)) :
        return limit
    else :
        return fibonacci(limit-2) + fibonacci(limit-1)
    
seq = int(input("Enter the number of sequence you want to see from fibonacci series : "))

for i in range(seq) :
    print(fibonacci(i))