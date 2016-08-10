fo=open('file1.txt','wb')
print fo.name
print fo.closed
print fo.mode
print fo.softspace
fo.closed
fo.write('python is great.\npython is awesome\nas so i')
fo.close()
fo=open('file1.txt','r+')
#fo.truncate()    #remove everything after the file pointer
print fo.tell()
a=fo.read()
print a
count=0
word=''
for i in a:	
	word+=i
	count =count+1
	print i
print count
print word
count=0
for i in word:
	if i is '\n':
		count+=1
print count
print fo.tell()	#tell current position of the pointer
print fo.seek(0,0) #place the file pointer at the begining og the file
print fo.read()
print "check for tty device  " ,fo.isatty()
print fo.fileno()
fo.close()
import os
os.rename('file1.txt','file')
os.getcwd()
os.mkdir('new')
print os.getcwd()
os.chdir('new')
print os.getcwd()
os.chdir('/home/niraj/learn_pyth/')
os.rmdir('new')
print os.getcwd()
