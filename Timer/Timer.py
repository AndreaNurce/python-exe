import time
sec = int(input("Type how many seconds woy want to wait "))
times = sec
hrs = 0
min = 0
if sec > 59:
    while sec > 59 and sec > 0 :
        sec -= 60
        min += 1
if min > 59 :
    while min > 59 and min > 0 :
        min -= 60
        hrs += 1

cr_hrs = hrs
cr_min = min
cr_sec = sec

check = True
while check :
    if sec > 0 :
        #do this
        sec -= 1
        time.sleep(1)
        print(cr_hrs -hrs,"Hours ",cr_min - min ,"Minutes",cr_sec - sec,"Seconds" , "Have passed")
    if sec == 0 and min >= 1 :
        #do this
        min -= 1
        sec += 60
    if sec == 0 and min == 0 and hrs >= 1:
        #do this
        hrs -=1
        min += 60
    if sec == 0 and min == 0 and hrs == 0:
        check = False
        print("")
        print("")
        print("Time is up!!!")