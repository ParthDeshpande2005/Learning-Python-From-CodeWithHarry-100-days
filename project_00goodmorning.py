#%%
import time
timestamp=time.strftime('%H:%M:%S')
hour=time.strftime('%H')
if(int(hour)>=12 and int(hour)<17):
    print("good afternoon")
elif(int(hour)>=21):
    print("good Night")
elif(21>int(hour)>=17):
    print("good evening")
else:
    print("good morning")