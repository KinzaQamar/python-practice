def sum(*numbers):
    sum = 0
    print("The numbers are :")
    for i in numbers:
        sum = sum+i
        print(i)
        if (i == len(numbers)):
            break
        else:
            print(",")

    return sum

sum = sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
 
print ("\nThe sum = ",sum)
