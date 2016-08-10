Tuple1=(1,2,3,4,5,6,7,8,9)
Tuple2=('python','c','c++','java')
print Tuple1[0]
print Tuple2[3]
#Tuple2[0]='python' tuple cannot be updated
del Tuple2 #delete all aelements from the Tuple2
#print Tuple2
print len(Tuple1)
for x in Tuple1:
	print x
List=['python','c','c++','java']
Tuple2=tuple(List)
print Tuple2
#hence tuples non-changable they r ststic