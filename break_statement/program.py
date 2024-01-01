#Print the table of an integer till a specific limit

num = int(input('Enter an integer : '))
limit = int(input('Enter the limit : '))
i = 0

while True:
    if ( i == 10):
        break
    print(num, "*", i+1,"=",num*(i+1))
    i = i+1