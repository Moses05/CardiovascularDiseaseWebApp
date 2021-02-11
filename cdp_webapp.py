import preparing_data
import streamlit as st
import matplotlib.pyplot as plt
# import seaborn as sns
import sqlite3
import pandas as pd
from preparing_data import model2, X, y
# import hashlib

conn = sqlite3.connect("doctor_logins.db")
cursor = conn.cursor()

def create_usertable():
	cursor.execute("CREATE TABLE IF NOT EXISTS usertable(username TEXT, password TEXT)")

def add_user_data(username, password):
	cursor.execute("INSERT INTO usertable(username, password) VALUES (?,?)", (username, password))
	conn.commit()

def login_user(username, password):
	cursor.execute("SELECT * FROM usertable WHERE username = ? AND password = ?", (username, password))
	data = cursor.fetchall()
	return data

def view_all_users():
	cursor.execute("SELECT * FROM usertable")
	data = cursor.fetchall()
	return data

# def create_connection(d)


def main():
	st.title("Fortismere Surgery")

	menu = ["Predictor", "Doctor Login"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Doctor Login":
		st.subheader("Doctor Login")

		st.image("doctor.png", width=100)

		username = st.text_input("Username: ")
		password = st.text_input("Password: ", type="password")

		# try change this to button
		if st.checkbox("Click to Login"):
			create_usertable()
			result = login_user(username, password)
			if result:
				st.success(f"Logged in as {username}")

				admin_tools = st.sidebar.selectbox("Admin Tools",["Check appointments","View prediction analytics","Add doctor","View doctors"])

				if admin_tools == "Check appointments":
					st.subheader("Check appointments")
		
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
					new_doctor = st.text_input("Username")
					new_password = st.text_input("Password", type = "password")
					
					if st.button("Add Doctor"):
						create_usertable()
						add_user_data(new_doctor, new_password)
						st.success("You have successfully added a new doctor")
						st.info("The new doctor can login in the menu section and access the admin tools")


				elif admin_tools == "View doctors":
					st.subheader("View doctors")
					user_results = view_all_users()
					clean_db = pd.DataFrame(user_results, columns = ["Username", "Password"])
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

			characteristics = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, 	exang, oldpeak]]
	
			model2.fit(X, y)
	
			prediction = model2.predict(characteristics)
	
			if prediction == 1:
				st.write("You have a cardiovascular disease g. Get some help")
			else:
				st.write("Yh ur gd still")

		predictor()

if __name__ == "__main__":
	main()
