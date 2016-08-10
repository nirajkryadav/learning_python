try:
	fo=open('file','w')
	fo.write('yeeeh i can handle exceptions!!')
	fo.read() #gives an error reading in write mode
except IOError:
	print "the file u r trying to access is currently unavialable\nplaese try again after rechecking ur shitty code"
else:
	print "ur message has been written sucessfully"
	fo.close()
#the above one is not a good programming practice cos it catches all the exceptions in one except we may have diff kind of errors also use multiple excepions
try:
	fo=open('file','w')
	fo.write('yeeeh i can handle exceptions!!')
	fo.read() #gives an error reading in write mode
except IOError:
	print "the file u r trying to access is currently unavialable\nplaese try again after rechecking ur shitty code"
finally:				#this will run either error comes or not
	print "ur message has been written sucessfully"
	fo.close()

try:
	fh = open("testfile", "w")
	try:
		fh.write("This is my test file for exception handling!!")
	finally:
		print "Going to close the file"
		fh.close()
except IOError:
	print "Error: can\'t find file or read data"
def convert_var(var):
	try:
		return int(var)
	except ValueError, e:
		print "r u idiot argument must contain number",e
		pass
convert_var('xyzb')




