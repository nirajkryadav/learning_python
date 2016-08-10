import math
import random
x=123.34
print abs(x)#absolute value of x
print math.ceil(x)#smallest integer not less than x
print cmp(x,10) #1 if x>10
print cmp(x,125)#-1 ifx x<125
print cmp(x,123.34)#0 if x=123.34
print math.exp(x) #expontional of x
print math.fabs(x)#absolute value of x
print math.floor (x)#largest integer not greater than x
print math.log(x)#log of x
print math.log10(x)#log of x with base 10
print max(x,12,134,123)
print min(x,23,234,12,2)
print math.modf(x)#seprate integer and decimal part in a tuple with 2 values
print math.pow(x,2) #gives x power2
#print round(x[,1]) error ??
print math.sqrt(x)#square root of x
string = 'python'
print random.choice(string)
print random.randrange(1,10,3)#ans from only 1 4 7 (1 to 10 in steps 0f 3)
print random.random()#a random float btw 0and 1
#print random.speed(12) error??
List=list(string)
print random.shuffle(List)#shuffles the list elements
print random.uniform(12,17)#float point btw 12 and 17

#trignometric functions
print math.acos(1)#gives radian value of the function
print math.pi
print math.e**2
print math.asin(.5)
print math.atan(12)
print math.atan2(12,1) #atan value of 12/1
print math.cos(12)
print math.hypot(3,4)#return the third triplet or eucliden norm
print math.sin(12)
print math.tan(123)
print math.degrees(math.pi)
print math.radians(180)
