import time
timestamp = time.strftime('%H:%M:%S')
print("TIme:",timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)

if (timestamp >= 3 and timestamp < 12):
    print("Its",timestamp,": Good Morning :)")
elif (timestamp >=12 and timestamp <= 16):
    print("Its",timestamp,": Good Afternoon :)") 
elif (timestamp >=16 and timestamp <= 19):
    print("Its",timestamp,": Good Evening :)") 
else:
    print("Its",timestamp,": Good Night :)")

# https://docs.python.org/3/library/time.html#time.strftime