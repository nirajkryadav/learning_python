def print_function():
	print '''this is a function to print string only'''
	pass
print_function()
List=[1,2,3,4]
def change_me(List):
	List.append(8)#append in original list
	List=[2,3,4,5]
	List.append(8)#append in the list indside the function
	List.append(7)
	print List
	pass
change_me(List)
print List

def printinfo(name , age,sex='M'):
	print 'name : ',name
	print 'age : ',age
	print 'sex : ',sex
	pass
printinfo('niraj',18)
printinfo(age=18,name='niraj')
def var_arg(arg1,*a):
	for i in a:
		print i
	pass
	
var_arg( 1,273,13,'bvbb')
sum =lambda agr3, arg2: arg2+agr3#anony fx
print sum(10,23)
import os
print os.getcwd()