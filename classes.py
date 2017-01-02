class learn(object):  #classs 
	"example for learning classes"

	count=0			#sared among all instance of the class 
	def __init__(self,name,sal):  #constructor f(x) of the class
		self.name =name	
		self.sal=sal
		learn.count+=1
	def display(self): #f(x)inside the class
		print "total employee %d "  %learn.count
		pass
	def displayemp(self):
			print "name :", self.name,"salary:",self.sal
e1= learn("niraj",3000)#object of the class 
e2= learn("pankaj",3000)
e3= learn("akshit",3000)
e1.displayemp() #f(x) call using object
e2.displayemp()
print hasattr(e1,'salary')
print hasattr(e1,'sal')
print getattr(e1,'sal')
print learn.count





	
