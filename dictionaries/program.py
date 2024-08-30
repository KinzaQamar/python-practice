# Kinza Qamar Zaman
# 30-Aug-2024

# Dictionary is a combination of key-value pairs. It is a ordered collection of data items.

# Declaration of Dictionary
student = {
           "Name" : "Kinza",
           "Father's Name" : "Qamar Zaman",
           "Roll Number": "18B-058-CE",
           "Major" : "Computer Systems Engineering",
           "CGPA" : 3.0
           }

# Ways to print values from a dictionary
print(student,"\n")  # Prints all the members of the dictionary in same order. 
                     # Note that dictionaries below 3.7 are unordered 

print(student["Name"]) # Prints the value corresponds to key Name. 
print(student.get("Name"),"\n") # Prints the value corresponds to key Name. Except it does 
                                # not throws error if key does not exist in the dictionary.

print(student.get("age"),"\n") # Prints None
# print(student["age"]) # Throw error

print(student.keys()) # Prints all keys 
print(student.values(),"\n") # Prints all values

# Using for loop to print values of the dictionary
for key in student.keys():
    print(f"The value correspond to key {key} is {student[key]}")

print("\n")
print(student.items(),"\n") # Prints all the key-value pairs from the dictionary

# Another way to print the values of the dictionary along with their keys
for keys,values in student.items():
    print(f"The value correspond to key {keys} is {values}")