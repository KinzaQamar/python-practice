#Print the table of an integer till a specific limit

num = int(input('Enter an integer:'))
limit = int(input('Enter the limit:'))
i = 0

while True:
    print(num, "*", i,"=",num*i)
    if ( i == limit):
        break
    i = i+1