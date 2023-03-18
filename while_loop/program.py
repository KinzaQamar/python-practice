#Print the table for any number till the given range

num = int(input("\nEnter an integer:"))
limit = int(input("Enter limit:"))
i = 0

while (i < limit):
    print(num, "*", i+1,"=",num*(i+1))
    i = i+1

#Print the table for any number for its even/odd multiples
num = int(input("\nEnter an integer:"))
limit = int(input("Enter limit:"))

if (limit%2 == 0):
    print("Entered limit is even, so start should increment by 2")
    start = 0
else:
    print("Entered limit is odd, so start should increment by 1")
    start = 1
    
while (start <= limit):
    print(num, "*", start,"=",num*start)
    start = start+2
