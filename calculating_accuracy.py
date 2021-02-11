from preparing_data import X_train, y_train, model1, model2, model3, X_test, y_test, X, y
from sklearn.metrics import confusion_matrix

# I can try use oop here

def accuracy(model):
	cm = confusion_matrix(y_test, model.predict(X_test))

	trueNegative = cm[0][0]
	truePositive = cm[1][1]
	falseNegative = cm[1][0]
	falsePositive = cm[0][1]

	accuracy_rating = (truePositive + trueNegative)/(truePositive+trueNegative+falseNegative+falsePositive)

	return accuracy_rating

print("Random Forest classifier accuracy = ",round(accuracy(model3),2))
print("K nearest neighbour accuracy = ",round(accuracy(model2),2))
print("Decision Tree classifier accuracy = ",round(accuracy(model1),2))




def classifier(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak):

	model2.fit(X, y)

	print(model2.predict([age, sex, cp, tres, chol, fbs, restecg, thalach, exang, oldpeak]))

age = int(input("How old are you?"))
sex = int(input("Are you male (1) or female (0)?"))
cp = int(input("What kind of chest pain are you having?"))
trestbps = int(input("Whats your trestbps innit"))
chol = int(input("Whats your cholestoral level"))
fbs = int(input("Whats your fbs"))
restecg = int(input("Whats your restecg"))
thalach = int(input("Whats your thalach"))
exang = int(input("Whats your exang"))
oldpeak = float(input("Whats your oldpeak"))

classifier(age,sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak)

class knn:
	def __init__