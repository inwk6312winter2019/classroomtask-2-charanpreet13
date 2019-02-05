import string
class Cal:
	def __init__(self,ip=[0,0,0,0],nm=[0,0,0,0]):
		self.ip=ip
		self.nm=nm
	def myip(self):
		i = input("enter IP")
		a = i.split('.')
		b = hex(int(a[0])) + hex(int(a[1])) + hex(int(a[2])) + hex(int(a[3]))
		b = b.replace('{:02x}', '')
		b = b.upper()
		print(b)
	def mymask(self):
		print("The mask is",self.nm)
x=Cal( )
x.myip()
x.mymask()

