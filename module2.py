from module1 import fib
import functions
functions.printinfo('niraj',18,'M')
fib(6)
import sys
#print sys.path
money=0
def addmoney():
	global money
	money=10
	print money
	pass
print money
addmoney()
print money
print dir(sys)#all fx in the module sys