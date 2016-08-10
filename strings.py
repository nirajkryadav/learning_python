var ='python'
print var
print var[::-1]
print var + var[::-1]
print "sfsdf\vsdfsdfv"#vertical tab
print 'h' in var
print 'h' not in var 
print r'sddg\nfgfg\tsfd\vdfd\dfg'#supress  the meaning of \ in the string
print "my name is %s and i am %d years old this is %s"%('niraj',18,'awesome')
print """this is for printing paragraphs 
everything in output will appear same as it
is in the print statement \nnew line characher will also work here
as well as \\t and other \ characters"""
print u'u for the uniode string it is a 16 bit which includes special chars from most of languages of the world'
#string build-in meathods
print var
print var.capitalize()#capitalize first letter
#print string.center('20',var) error check
print var.find('thon',0,len(var))#on which place it is found is returned -1 if not found
print var.isalpha()
print var.isdigit()
print 'fhfggfg'.isdigit()
print '1231212'.isdigit()
print 'a'.join(var)#concatinate string in a seq 
print len(var)
print var.lower()
print var.upper()
var="  python"
print var
var = var.lstrip() #remove all leading whitespaces
print var
print max(var)
print min(var)
print var.replace('p','P')#replace all p with P
var = 'python    '
print var+"whitespaces"
print var.rstrip()+"whitespaces" #remove all whitespaces from the back
print var.strip('p')#strip p from both back and front
print var.swapcase()
var='py\thon'
print var.center(40,'*')
print var.count('o',0,len(var)-1)#count no of o in the sting
print var
print var.encode('base64','strict')
print 'i m awesome'.encode('base64')
print var.expandtabs(16)
print var.ljust(50,'*')
print var
var = 'i am awesome, i love programming'
print var
import string
from string import maketrans
print var.translate(maketrans("aeiou","12345"),)#need to import function maketrans
print var.replace("i","I",1)#1 for how many words to replace
print var.title()#make the line as a title


















