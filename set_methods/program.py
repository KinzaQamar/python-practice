name = {"Kinza"}
sibs = {"Shez","Maaz","Eishal"}

# Union method
print("The union of the sets :",sibs.union(name))

# Update method
sibs.update(name)
print("Siblings :",sibs)

# Intersection methods
print("The intersection of the sets :",sibs.intersection(name))

# Intersection update methods
sibs.intersection_update(name)
print("The sibs set after intersection update :",sibs)

# Symmetric Difference method
sibs = {"Shez","Maaz","Eishal","Kinza"}
print("The symmetric difference of the sets :",sibs.symmetric_difference(name))

# Symmetric Difference update method
sibs.symmetric_difference_update(name)
print("The sibs set after symmetric difference update :",sibs)

# add method
sibs.add("Kinza")
print("Set sibs after add :",sibs)

# pop method
s = sibs.pop()
print(f"The sets : {s} and {sibs}")

# add method
sibs.add("Kinza")
print("Set sibs after add :",sibs)

# del method deletes the set
del name

# clear method clears the set
sibs.clear()
print("The set after clear method :",sibs)
