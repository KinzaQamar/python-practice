# Strings are immutable
a = "```Kinza Qamar Zaman```"

print("Length of the string is",len(a))
print("String:",a)
print("String with upper method",a.upper())
print("String with lower method",a.lower())
print("string with rstrip method",a.rstrip("`"))
print(a.replace("Kinza", "Eishal"))
print(a.split(" "))
blogHeading = "introduction tO python"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Kinza"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Mohammad. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you Eid Mubarak\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "              #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "He's name is Mohammad. He is an honest man."
print(str1.title())