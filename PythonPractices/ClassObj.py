
class Person:
	def __init__(self,initialAge):
		self.age = initialAge
		if(initialAge<0):
			print("Age is invalid, setting age to 0")
			print("\a")
			self.age = 0
			
	
	def yearPasses(self):
		self.age =+1
		
	def amIOld(self):
		if self.age<13:
			print("You are young..")
			
		elif(self.age>=13 and self.age<18):
			print("You are teenager..")
			
		else:
			print("You are old")
			
			
agee = int(input("Age : "))
obj = Person(agee)
obj.amIOld()
obj.yearPasses()