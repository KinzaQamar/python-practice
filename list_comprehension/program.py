list1 = [i for i in range(50) if (i%2==0)]

print("List 1 :",list1)

#Making list from another list
list2 = [i for i in list1 if i > 10]
print("List 2 :",list2)
