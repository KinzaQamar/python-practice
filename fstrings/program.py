#Without fstrings
str = 'Hi, I am {1} from {0}'
name = input("Enter your name : ")
country = input("Enter your country : ")

print("Without fstrings : ",str.format(country, name))

print(f"With fstrings : Hi, I am {name} from {country}")

cgpa = 3.707
txt = f"My CGPA was {cgpa:.2f}"
print(txt)