a ,b,c =10 ,6.0 ,0
c = a + b
print "Line 1 - Value of c is ", c
c = a - b
print "Line 2 - Value of c is ", c  #automatic type casting
c = a * b
print "Line 3 - Value of c is ", c
c = a / b
print "Line 4 - Value of c is ", c #float will give decimal answers
c = a % b
print "Line 5 - Value of c is ", c #remainder
a = 2
b = 3
c = a**b
print "Line 6 - Value of c is ", c
a = 10
b = 5
c = a//b
print "Line 7 - Value of c is ", c #floor division
print "\n\n\n\n  bitwise operations"
a=60
b=13
print a&b # AND operation of 60 and 13 in binary
print a|b # OR
print a^b #XOR
print ~b # flipping bites -b in 2's complement
print a<<2 #binary left Shift shifting left digits to the right
print b>>2 #binary right shift shifting right digits to the left
print "\n\n\n logical operators"
print a and b #both conditions are true
print a or b# one condition is true
print not b  and a#reverse the logic state
print "\n\n\n\nmembership operators"
a=12
b=4
List =[1,2,3,4,5,6,7]
print List
if a in List:
	print a
else:
	print "a not present"
if b in List:
	print b
else:
	print "b  not present"

print "\n\n\n identity Operators"
a=10
b=10
print a is b
print a is not b
print "operator precedance"
a = 20
b = 10
c = 15
d = 5
e = 0
e = (a + b) * c / d   #( 30 * 15 ) / 5
print "Value of (a + b) * c / d is ",e
e = ((a + b) * c) / d   # (30 * 15 ) / 5
print "Value of ((a + b) * c) / d is ",e
e = (a + b) * (c / d);   # (30) * (15/5)
print "Value of (a + b) * (c / d) is ",e
e = a + (b * c) / d;  #e=20 + (150/5)
print "Value of a + (b * c) / d is ",e










