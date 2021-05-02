# Importing all libaries
import preparing_data
import random
import appointment_classes
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sqlite3
import time
import re
from preparing_data import model2, X, y

conn = sqlite3.connect("databases.db")
cursor = conn.cursor()

class Doctors:
	def __init__(self, firstName, lastName, email, password):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.password = password
	
	def create_doctor_table():
		cursor.execute("""CREATE TABLE IF NOT EXISTS doctors(firstName TEXT, lastName TEXT, email TEXT, password TEXT, DoctorID TEXT)""")
	
	def CreateDoctorID(self):
		randomNumber = random.randint(1,999)
		DoctorID = (f"{self.firstName[0]}{self.lastName}{randomNumber}")
		return DoctorID

	def add_doctors(self):
		setattr(self, "DoctorID", self.CreateDoctorID())
		conn.execute("INSERT INTO doctors VALUES (?, ?, ?, ?, ?)", (self.firstName, self.lastName, self.email, self.password, self.DoctorID))
		conn.commit()
	
	def login_user(DoctorID, password):
		cursor.execute("SELECT * FROM doctors WHERE username = ? AND password = ?", (self.DoctorID, self.password))
		data = cursor.fetchall()
		return 
	
	def view_all_doctors():
		cursor.execute("SELECT * FROM doctors")
		data = cursor.fetchall()
		return data


def login_user(DoctorID, password):
		cursor.execute("SELECT * FROM doctors WHERE DoctorID = ? AND password = ?", (DoctorID, password))
		data = cursor.fetchall()
		return data


# def create_login_table():
# 	cursor.execute("""CREATE TABLE IF NOT EXISTS logintable(username TEXT, password TEXT)""")

# def add_login_data(username, password):
# 	cursor.execute("INSERT INTO logintable(username, password) VALUES (?,?)", (username, password))
# 	conn.commit()

# def login_user(username, password):
# 	cursor.execute("SELECT * FROM logintable WHERE username = ? AND password = ?", (username, password))
# 	data = cursor.fetchall()
# 	return data

# def view_all_logins():
# 	cursor.execute("SELECT * FROM logintable")
# 	data = cursor.fetchall()
# 	return data

def create_patients_table():
	cursor.execute("""CREATE TABLE IF NOT EXISTS patients(firstName TEXT, lastName TEXT, email TEXT)""")

def add_patient(firstName, lastName, email):
	conn.execute("INSERT INTO patients VALUES (?, ?, ?)", (firstName, lastName, email))
	conn.commit()

def view_all_patients():
	cursor.execute("SELECT * FROM patients")
	data = cursor.fetchall()
	return data



def main():
	st.title("Fortismere Surgery")

	menu = ["Predictor", "Doctor Login"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Doctor Login":
		st.subheader("Doctor Login")

		st.image("doctor.png", width=100)

		DoctorID = st.text_input("Doctor ID: ")
		password = st.text_input("Password: ", type="password")
		
		# try change this to button
		if st.checkbox("Click to Login"):
			Doctors.create_doctor_table()
			result = Doctors.login_user(DoctorID, password)

			if result:
				st.success(f"Logged in as {DoctorID}")

				admin_tools = st.sidebar.selectbox("Admin Tools",["Check appointments","View prediction analytics","Add doctor","View doctors"])

				if admin_tools == "Check appointments":
					create_patients_table()
					st.subheader("Check appointments")
					clean_db = pd.DataFrame(view_all_patients(), columns = ["firstName", "lastName", "email"])
					st.dataframe(clean_db)

				# class Queue:
				# 	def __init__(self):
				# 		pass

				elif admin_tools == "View prediction analytics":
					st.header("Prediction analytics")

					st.subheader("Shape of Dataset: ")
					st.write(preparing_data.dataSet.shape)

					st.subheader("Dataset as a whole: ")
					st.write(preparing_data.dataSet)

					st.subheader("Statistics of the dataset: ")
					st.write(preparing_data.dataSet.describe())

					st.subheader("View individual column")
					individual_column = st.selectbox(" ",["age","sex","chest pain type","resting blood pressure","cholestoral level","fasting blood sugar","resting electrocardiographic","maximum heart rate achieved","excercise induced angina","oldpeak","target"])
					if individual_column == "age":
						attribute = "age"
						if st.checkbox ("Change View"):
							st.bar_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
						else:
							st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					elif individual_column == "sex":
						attribute = "sex"
						if st.checkbox ("Change View"):
							st.bar_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
						else:
							st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					elif individual_column == "chest pain type":
							attribute = "cp"
							if st.checkbox ("Change View"):
								st.bar_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
							else:
								st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					elif individual_column == "resting blood pressure":
						attribute = "trestbps"
						if st.checkbox ("Change View"):
							st.bar_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
						else:
							st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					elif individual_column == "cholestoral level":
							attribute = "chol"
							st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 0, width= 400)	

					elif individual_column == "fasting blood sugar":
							attribute = "fbs"
							if st.checkbox ("Change View"):
								st.bar_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
							else:
								st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					elif individual_column == "resting electrocardiographic":
							attribute = "restecg"
							if st.checkbox ("Change View"):
								st.bar_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
							else:
								st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					elif individual_column == "maximum heart rate achieved":
							attribute = "thalach"
							if st.checkbox ("Change View"):
								st.line_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
							else:
								st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					elif individual_column == "excercise induced angina":
							attribute = "exang"
							if st.checkbox ("Change View"):
								st.bar_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
							else:
								st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					elif individual_column == "oldpeak":
							attribute = "oldpeak"
							if st.checkbox ("Change View"):
								st.line_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
							else:
								st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					elif individual_column == "target":
							attribute = "target"
							if st.checkbox ("Change View"):
								st.bar_chart(data = preparing_data.dataSet[attribute].value_counts(), use_container_width=1, height = 250)
							else:
								st.dataframe(preparing_data.dataSet[attribute].value_counts(), height = 250, width= 400)

					st.subheader("Cases of cardiovascular disease at each age")
					plt.figure(figsize=(16,7.5))
					st.write(sns.countplot(x = preparing_data.dataSet["age"], hue = preparing_data.dataSet["target"]))
					st.pyplot()

					st.subheader("Correlations of all features on each other")
					if st.checkbox ("See Graph"):
						plt.figure(figsize = (10,10))
						st.write(sns.heatmap(preparing_data.dataSet.corr(), annot=True, fmt =".0%"))
						st.pyplot()
					else:
						st.dataframe(preparing_data.dataSet.corr(), height = 250)

				elif admin_tools == "Add doctor":
					st.subheader("Add doctor")
					new_doctor_firstName = st.text_input("Enter the doctors first name")
					new_doctor_lastName = st.text_input("Enter the doctors name")
					new_doctor_email = st.text_input("Enter the doctors email")
					new_doctor_password = st.text_input("Enter the doctors new password", type = "password")

					email_check = re.search("[a-zA-Z0-9]+@[Fortismere]+.[surgery]", new_doctor_email)

					while email_check == None:
						st.warning("Incorrect Email Input, only email domain is '@fortismere.com'")
						new_doctor_email = st.text_input("Re enter the doctors email")
					
					if st.button("Add Doctor"):
						Doctors.create_doctor_table()
						new_doctor = Doctors(new_doctor_firstName, new_doctor_lastName, new_doctor_email, new_doctor_password)

						Doctors.add_doctors(new_doctor)
						st.success(f"You have successfully added a new doctor under the id: {new_doctor.DoctorID}")
						st.info("The new doctor can login in the menu section and access the admin tools")

				elif admin_tools == "View doctors":
					st.subheader("View doctors")
					login_results = Doctors.view_all_doctors()
					clean_db = pd.DataFrame(login_results, columns = ["First Name", "Last Name", "Email", "Password", "Doctor ID"])
					st.dataframe(clean_db)

			else:
				st.warning("Incorrect login. If you are a doctor ask an admin to create a login for you")

	if choice == "Predictor":
		st.subheader("Predictor")

		column1, column2 = st.beta_columns(2)

		def predictor():
			age = st.number_input("How old are you?", min_value = 1)
	
			sex_selectbox = st.selectbox("What gender are you?", ("Male", "Female"))

			if sex_selectbox == "Male":
				sex = 1
			else:
				sex = 0

			cp_selectbox = st.selectbox("What kind of chest pain are you having?", ("Asymptomatic", "Atypical angina", "Non-anginal pain", "Typical angina"))

			if cp_selectbox == "Asymptomatic":
			 	cp = 0
			elif cp_selectbox == "Atypical agina":
				cp = 1
			elif cp_selectbox == "Non-anginal":
				cp = 2
			elif cp_selectbox == "Typical angina":
				cp = 3

			trestbps = st.number_input("What is your resting blood pressure (mm Hg)", min_value = 60, max_value = 250)

			chol = st.number_input("Cholestoral level (mg/dl)", min_value=90, max_value=400)

			fbs_selectbox = st.selectbox("Is your fasting blood sugar over 120 mg/dl?", ("Yes", "No"))

			if fbs_selectbox == "Yes":
				fbs = 1
			else:
				fbs = 0

			restecg_selectbox = st.selectbox("What were the results of your resting electrocardiogram?", ("Normal", "Signs of ST-T wave abnormality", "Showed probably or definite left ventricular hypertrophy by Estes' criteria"))

			if restecg_selectbox == "Normal":
				restecg = 0
			elif restecg_selectbox == "Signs of ST-T wave abnormality":
				restecg = 1
			else:
				restecg = 2

			thalach = st.number_input("What the maximum heart rate that you've achieved", min_value=60, max_value= 230)

			exang_selectbox = st.selectbox("Do you suffer from excercise induced angina?", ("Yes", "No"))

			if exang_selectbox == "Yes":
				exang = 1
			else:
				exang = 0

			oldpeak = st.number_input("ST depression induced by exercise", min_value=0.0, max_value= 10.0, step = 0.1)

			characteristics = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]]
	
			model2.fit(X, y)
	
			prediction = model2.predict(characteristics)
			
			if st.checkbox("Predict"):
				if prediction == 1:
					st.info("You have a cardiovascular disease")
					st.info("[Check the NHS website for more information](https://www.nhs.uk/conditions/cardiovascular-disease/)")
					time.sleep(1)
	
					if st.checkbox("Do you want an appointment?"):
						create_patients_table()
						firstName = st.text_input("Enter your first name")
						lastName = st.text_input("Enter your last name")
						email = st.text_input("Enter your email")
						# appointmentDate = st.date_input(str("Select a date for your appointment"))
						# appointmentTime = st.time_input(str("Select a time for your appointment"))

						if st.button("Book appointment"):
							add_patient(firstName, lastName, email)
							st.success(f"You will be contacted by a Doctor soon")
				else:
					st.info("You do not have a cardiovascular disease")

		predictor()

if __name__ == "__main__":
	main()