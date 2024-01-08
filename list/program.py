#Declaration and ways to print a list
marks = [100,50,78,90,45]
print("Marks : ",marks)
print("Marks[:] : ",marks[:])

#List can have entities of multiple data types
student = [ "Name : Kinza", 60, "Roll No : 18B-058-CE"]
print("\nStudent : ",student)
print("Student[:] : ",student[:])

#Indexing in lists
print(student[-1])
print(student[-2])
print(student[-3])
# print(student[-4]) Gives an error as list index out of range
print("\nmarks[::1] : ",marks[::1]) 

#Check if item is present in list
if 900 in marks:
    print("\n90 is present in the marks list")
else:
    print("\n90 is not present in the marks list")

high = 0
for i in marks:
    if (i > high):
        high = i

print("\nThe highest marks from list are:",high)

