Dict={'age ':'18','year':'1','name':'Niraj'}
print Dict
Dict['year']='2'
print Dict
for x in Dict.keys():
	print x+'\t:\t'+Dict[x]
	pass
del Dict['name']#delete element with key name, del Dict will delete entire dictionary
print Dict
Dict['name']='niraj'#add a element with key name 
Dict.clear()#clear the dictionary
print Dict
Dict={'age ':'18','year':'2','name':'Niraj'}
print str(Dict)
Dict1=Dict.copy()#copy the entire dictionary
print Dict1
seq=('name','age ','year')
Dict1 =Dict1.fromkeys(seq,10)#form a new dict from seq with default value none 
print Dict1
print Dict1.get('sex','please try again') #default value none
print Dict1.has_key('sex')#returns true of false
print Dict1.items()#return list of tuples with key value pair
print Dict1.setdefault('sex','M')#set default value of the key #default is none
print Dict1
Dict=Dict.update(Dict1)#update dict from dicct1
print Dict
