#Print the table for any number for its even multiples
num = int(input("Enter an integer : "))
limit = int(input("Enter limit : "))

i = 1
    
while (i <= limit):
    if ( i%2==0):
        i = i+1
        continue
    print(num, "*", i,"=",num*i)
    i = i+1
        