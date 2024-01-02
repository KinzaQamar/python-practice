import time

def greetings():
    timestamp = time.strftime('%H:%M:%S')
    print("Time is",timestamp)
    timestamp = int(time.strftime('%H'))
    print("Hour :",timestamp)
    
    if (timestamp >= 3 and timestamp < 12):
        print("Its",timestamp,": Good Morning :)")
    elif (timestamp >=12 and timestamp <= 16):
        print("Its",timestamp,": Good Afternoon :)") 
    elif (timestamp >=16 and timestamp <= 19):
        print("Its",timestamp,": Good Evening :)") 
    else:
        print("Its",timestamp,": Good Night :)")

greetings()