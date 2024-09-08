# Update on 3-sep-2024
# Kinza Qamar Zaman

Firstname = "Kinza"
Lastname = " Qamar Zaman"
Intro = """Hi, I am Kinza from Pakistan
and I am a graduated student from UITU, Karachi"""
print(Firstname+Lastname)
print(Intro)

# Strings are immutable. Therefore, assigning to an indexed position in the string results in an error:
# Firstname[0] = "p"  # Throws error

print("let's try through loop")
for i in Intro:
    print(i)

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 * 'un' + 'ium')