import time
print "no of ticks since: 12 am , 1 jan ,1970 :" ,time.time()
print time.localtime(time.time())#gives u time tuple ,calc tuple using sec rom 1jan 1970 12 am
print time.asctime(time.localtime(time.time())) #for getting formated time , it takes ardument as time tuple
import  calendar
print calendar.month(2016,7)
print time.altzone#no idea what it is giving
a= time.time()
b=time.clock()
#time.sleep(1.5)
print time.clock()-b  #gives process time
print time.time()-a#gives total time
print time.ctime()
print time.gmtime() #provides time structure
print time.mktime(time.localtime(time.time()))#convert the time tuple in secs
#print time.strftime( %b%d %Y %H %M %S, time.gmtime(time.time())) check errors
print calendar.calendar(1,w=2,l=1,c=6)