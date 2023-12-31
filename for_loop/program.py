#Print the alphabets
name = input("Enter name : ")

for i in name:
    print(i, end = " , ")

#Print the table for any number till the given range

num = int(input("\n\nEnter an integer:"))
limit = int(input("Enter limit:"))

for i in range(limit):
    print(num, "*", i+1,"=",num*(i+1))

#Print the table for any number for its even/odd multiples
num = int(input("\nEnter an integer:"))
limit = int(input("Enter limit:"))

if (limit%2 == 0):
    print("Entered limit is even, so start should be 0")
    start = 0
else:
    print("Entered limit is odd, so start should be 1")
    start = 1
    
for i in range(start, limit, 2):
    print(num, "*", i,"=",num*i)