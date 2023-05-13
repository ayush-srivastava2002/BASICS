import time
realtime=time.strftime("%H:%M:%S")
print(realtime)
realhour=time.strftime("%H")
print(realhour)
realminute=time.strftime("%M")
print(realminute)
realsecond=time.strftime("%S")
print(realsecond)

if(realtime>="5:0:0"):
    if(realtime<"12:0:0"):
        print("GOOD MORNING")
elif(realtime>="12:0:0"):
    if(realtime<"17:0:0"):
        print("GOOD AFTERNOON")
elif(realtime>="17:0:0"):
    if(realtime<"21:0:0"):
        print("GOOD EVENING")
else:
    print("GOOD NIGHT")                        