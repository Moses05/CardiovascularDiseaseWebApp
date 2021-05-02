import random

class Patient:
	def __init__(self, firstName, lastName, email):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		
	def PatientID(self):
		randomNumber = random.randint(1,999)
		PatientID = (f"{self.firstName[0]}{self.lastName}{randomNumber}")
		return PatientID

class Doctor:
	def __init__(self, firstName, lastName, email, password):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.password = password

	def DoctorID(self):
		randomNumber = random.randint(1,999)
		self.DoctorID = (f"{self.firstName[0]}{self.lastName}{randomNumber}")
		return self.DoctorID

	def add(self):
		setattr(self, "DoctorID", self.DoctorID())
		all = vars(self)
		return all.keys()

moses = Doctor("Moses", "Makola", "mmakola67@gmail.com", "Test")

# moses.DoctorID()

# print(moses.DoctorID())
print(moses.add())