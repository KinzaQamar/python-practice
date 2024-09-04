# Update on 3-sep-2024
# Kinza Qamar Zaman

name = "Kinza Qamar"
print("The length of name : ",len(name)) 
print("name[0] : ", name[0])
print("name[1] : ", name[1])
print("name[11:0] : ", name[11:0]) # No output
print("name[0:11]", name[0:11])
print("name[0:6] : ", name[0:6])
print("name[-1] : ", name[-1]) # name[len(name)-1]
print("name[7:10] : ", name[7:10])   # starting from index 7 to 2 following characters excluding 10th
print("name[-4:-2] : ", name[-4:-2]) # name[len(name) - 4 : len(name) - 2] -> name[7:9]
print("name[:2] : ", name[:2])       # starting from the beginning to the position 2 (excluded)
print("name[2:] : ", name[2:])       # starting from the position 2 to the end
print("name[-2:] : ", name[-2:])     # starting from the position name[len(name)-2] to the end
print("name[:-2] : ", name[:-2])     # starting from the beginning to the name[len(name)-2]
print("name[:2] + name[2:] : ", name[:2] + name[2:])
print("name[:4] + name[4:] : ", name[:4] + name[4:])

lname = name[6:] + "Zaman"
print("name[6:] + Zaman : ", lname)