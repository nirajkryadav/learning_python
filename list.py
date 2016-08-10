List1=['python','c++','java']
List2=['swift','c','ruby']

print List1
print List2[0]
List2[0]='python'#updating value at 0
print List2
del List2[0] #deleting value at 0
print List2
print len(List1)
print List1+List2
List1+=List2 #concatinating 2 strings
print List1
for x in List1:
	print x
print 'python' in List1
print List1[-1]#accessing elements from end
print cmp(List1,List2)
print max(List1)
print min(List1)
print List1.append('swift')#takes one arguments
print List1
print List1.count('python')
List1.extend(('python','c','c++'))#takes a tuple or more arguments
print List1
print List1.index('c')#index of element
List1.insert(3,'python')
print List1
print List1.pop()#removes last item or place thre index of the element
print List1.remove('python')#remove first 'python' found
print List1
List1.reverse()
print List1.sort()
print List1


