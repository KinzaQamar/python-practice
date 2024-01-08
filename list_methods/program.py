fname = ["Kinza"]
lname = ["Qamar", "Zaman"]

#Append Method
fname.append("Qamar")
print("List fname after append : ",fname)

#Concatenate
fname.extend(lname)
print("List fname after extend : ",fname)

#Sort
lname.sort(reverse=True) #sort the list in increasing order
print("List lname after sort : ",lname)

#Reverse the list
fname.reverse()
print("List fname after reverse : ",fname)

#count function 
print("The number of times Qamar exist in fname list is : ",fname.count("Qamar"))

#Copy 
# f = fname // creates reference f to fname 
# f[0] = 0 //changes fname as well
f = fname.copy()
print("List f :",f)

#remove
fname.remove("Qamar")
print("List fname after remove : ",fname)

# num = []
# num.append(1)
# num.append(9)
# print(num)

name = fname + lname 
print("List name after concatenation : ",name)