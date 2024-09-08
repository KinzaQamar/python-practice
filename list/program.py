# Modified on 4th september 2024
# Kinza Qamar Zaman

# List is a collection of items of same or different data types
print(list)

# Declaration and ways to print a list
marks = [100,50,78,90,45]
print("Marks : ", marks)
print("Marks[:] : ", marks[:])

# List can have entities of multiple data types
student = [ "Name : Kinza", 60, "Roll No : 18B-058-CE"]
print("\nStudent : ", student)
print("Student[:] : ", student[:])
print("\nlen(student) : ", len(student))

# List can be indexed and sliced
print("\nstudent[-1] : ", student[-1]) # student[len(student)-1]
print("student[-2] : ", student[-2])   # student[len(student)-2]
print("student[-3] : ", student[-3])   # student[len(student)-3]
# print(student[-4]) Gives an error as list index out of range
print("\nmarks[::1] : ", marks[::1]) 
print("marks[::2] : ", marks[::2])
print("marks[::3] : ", marks[::3])
print("marks[::4] : ", marks[::4])
print("marks[1::1] : ", marks[1::1])
print("marks[1::2] : ", marks[1::2])
print("marks[0::2] : ", marks[0::2])

print("\nStudent + Marks : ", student + marks)

# List are mutable, Their content can be change after the declaration
marks[0] = 1.45
student[-3] = "Kinza Qamar"
print("Marks : ", marks)
print("Students : ", student)

#Check if item is present in list
if 90 in marks:
    print("\n90 is present in the marks list")
else:
    print("\n90 is not present in the marks list")

high = 0
for i in marks:
    if (i > high):
        high = i

print("\nThe highest marks from list are:",high)

# User input in list
size = int(input("\nEnter the size of the list : "))
list = []

for i in range(size) :
    item = int(input("Enter the value in list at %d index " %i))
    list.append(item)

print("User input list : ",list)

print("\nUser input list in reverse order : ",list[::-1])
print("\nUser input list in reverse order : ",list[::-2])

print("\nList + [A , B , C] : ", list + ["A", "B", "C"])