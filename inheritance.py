class parent:
	parattr = 100
	def _init_(self):
		print ("calling parent constructor")
	def parent_meathod(self):
		print ("calling parent meathod")
	def setarrt(self,attr):
		parattr = attr
	def getattr(self):
		print ("prent attr:", parent.parattr)

class child(parent):
	def _init_(self):
		print ("calling child constructor")
	def child_meathot(self):
		print ("calling child meathod")
c = child() 
c.child_meathot()
c.parent_meathod()
c.setarrt(100)
c.getattr()

print (issubclass(child,parent))
print (isinstance(c,child))

