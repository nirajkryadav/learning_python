import time  #use for time
a=time.clock()
count =0
while count<10:
	print count
	count+=1
	pass
'''count =0
while count<10:
	print "yeh i killed ur program"
	pass   #infinite loop'''

#using else with loop
count =6
while count>5:
	print "inside the loop"
	count =3
else:
	print "inside the else"

flag = 10
while flag : print "flag has a value";flag =0
while flag : print "flag has a value again"
else : print "flag is null"
flag 


#for loop
j=0
for i in 'python':
	j+=1
	print "the ",j," letter is :",i
for i in range (10):
	print i
i=2
for i in range (10,100):
	for j in range (2,i):
		if i%j is 0:
			#num=i/j
			#print "%d equals %d*%d"%(i,j,num)
			#print "%d number is not prime"%i
			break
	else:
		print "%d number is prime"%i


i=2
while i<100:
	j=2
	while j<=i/j:  #to reduce complexity
		if i%j is 0:  #if not i%j => is the same thing here(if not remainder or remainder is 0)
			#print i%j
			break
		j=j+1
	else :print "%d is prime"%i
	i=i+1



print time.clock()-a #for checking processing time