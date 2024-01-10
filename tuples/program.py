# tuples are immutable

fname = ("Kinza",)
lname = ("Qamar" , "Zaman")

print(fname.count("Qamar"))
print(lname.index("Qamar"))

# If you want to change a tuple first convert it into a list

list1 = list(fname)
print("The type of list is : ",type(list1))
print("List 1 : ",list1)

list1.extend(list(lname))
print("List after extend : ",list1)

fname = tuple(list1)
print("Tuple fname : ",fname)

#Different ways to input to tuple

tup = tuple(input("Enter the items to the tuple : "))
print(tup)

tup = tuple(input('Enter the items to the tuple : ').split())
print(tup)

inp = input('Enter the items to the tuple : ')
tup = tuple(int(item) for item in inp)
print(tup)