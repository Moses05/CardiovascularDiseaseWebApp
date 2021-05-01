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

	def login(self):
		randomNumber = random.randint(1,999)
		DoctorID = (f"{self.firstName[0]}{self.lastName}{randomNumber}")
		return DoctorID

sam = Patient("Sam", "Makola", "mmsdkfosfksd@sdfsfds.com")

print(sam.PatientID())
Doctor1 = Doctor("Moses", "Peter", "sdfkjnsfkjsd@Sdfsdfsd", "jdsfnjskdf")

print(Doctor1.login())