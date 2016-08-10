import sys
print "no_of_args:",len(sys.argv),"args"
print "argument_list",str(sys.argv),"\n\n"

"""print "first_arg",sys.argv[1]
print "fifth_arg",sys.argv[5]
#print "fifth_arg",sys.argv(5)  ////error list items are not callable
add=int(sys.argv[1])+int(sys.argv[2])
print "add:",add"""

i=1
add_=0
while i<len(sys.argv): #i=1 cos Ist argumenrt is the filename.py itself
	
	add_=add_+int(sys.argv[i])
	i+=1
print "addition fo args:",add_
raw_input("\n\npress_enter_to_exit")
