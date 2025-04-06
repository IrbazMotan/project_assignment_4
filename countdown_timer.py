import time

def  set_Count_downtime(my_time:int):
    for x in range (my_time,0,-1):
         second= x % 60
         minute= int (x /60)%60
         hours= int (x/3600)
         print("Your Count Down time is: hours: " + str(hours) + " minute:" + str(minute) + " second " +str(second))
         time.sleep(1)


my_time:int =int(input("set  count down timer"))
        
set_Count_downtime(my_time)
print("Times up")