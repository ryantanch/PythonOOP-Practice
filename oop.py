##################################################
#	Python OOP tutorials by Corey Schafer 
#	Source: Youtube - Corey Schafer
#	Practice Done by RyanTanCH 2019
#	Ver Python 3.6
##################################################

class Employee: 

	#Class Variable
	No_of_emps  = 0;
	raise_amount = 1.04

	#constructor 1 
	def __init__(self,first,last,pay):
		self.first = first;
		self.last = last;
		self.pay= pay;
		Employee.No_of_emps += 1 ;

	#Alternative Constructor 2
	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)

	#regular methods
	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first,self.last)

	#setter
	@fullname.setter
	def fullname(self,name): 
		first,last = name.split(' ')
		self.first = first
		self.last = last


	#Magic Methods
	def __repr__(self):
		return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

	def __str__(self):
		return '{} - {}'.format(self.fullname(),self.email)

	def __add__(self,other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname)

	#class methods

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount = amount

	#static methods
	@staticmethod
	def is_weekday(day):
		if day.weekday() == 5 or  day.weekday() == 6:
			return False
		return True

#Sublcass Inheritance
class Developer(Employee):
	raise_amount = 1.10

	#Subclass Constructur 
	def __init__(self,first,last,pay,language):
		#superclass 
		Employee.__init__(self,first,last,pay)
		self.language = language

class Manager(Employee):

	def __init__(self,first,last,pay,employees = None):
		#superclass 
		Employee.__init__(self,first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees  = employees

	def add_employee(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_employee(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)


	def print_employee(self):
		for emp in self.employees:
			print("-->",emp.fullname())


#How to use isInstance()
mgr_1 = Manager('Carol','Lee',51200,'Java')
print(isinstance(mgr_1,Manager))

#How to use isSubClass()

dev_1 = Developer('Richard','Lee',45440,'Python')
print(issubclass(Developer,Employee))

#Magic Method __add__

emp_1 = Employee('Corey','Schafer',50222)
emp_2 = Employee('Sally','Schafer',60355)
print(emp_1 + emp_2)

#Magic Method __len__

print(len(emp_1))


 












 



 