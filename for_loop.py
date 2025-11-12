# FOR LOOP: EXECUTE A BLOCK OF CODE FOR A FIXED NUMBER OF TIIMES.
# YOU CAN ITERATE OVER A RANGE,STRING,SEQUENCE..,ETC.
'''
for x  in range (10,20):
    print(x)

for y in reversed(range(0,10)):
    print(y)

credits_card = "8645-8565-5653-4622-5466"
 
for x in credits_card:
    print(x,end="")

for x in range(11,21):
    if x == 15:
        break
    else:
        print(x,end="")
        print("\n")

for y in range(0,10):
    if y == 3:
        continue
    else:
        print(y,end=" ")


# TIME FUNCTIONS

import time
time.sleep(3)
print("TIME'S UP")

my_time = int(input("ENTER YOUR TIME FOR SLEEPING:"))
for x in range(0,my_time):
    print(x)


time.sleep(1)
print("TIME'S UP") 

import time
my_time = int(input("ENTER YOUR TIME FOR SLEEPING:"))
#for x in range(my_time,0,-1):
for x in reversed(range(0,my_time)):
    print(x)


time.sleep(1)
print("TIME'S UP") 
'''
import time
my_time = int(input("ENTER YOUR TIME FOR SLEEPING:"))


for x in reversed(range(0,my_time)):
    sec = x % 60
    min = (x//100) % 60
    hour = (x//3600) % 12
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep

print("it's time")