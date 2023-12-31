num = int(input("Enter any number : "))

match num:
    case _ if(num%2 == 0):
        print(num, "is an even number")
    case _ :
        print(num, "is an odd number")