from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import pandas as pd

diabetes = pd.read_csv("./lab04/diabetes.csv")

train_set, test_set = train_test_split(diabetes.values, train_size=0.7, random_state=13)

train_inputs = train_set[:, 0:-1]
train_classes = train_set[:, -1]
test_inputs = test_set[:, 0:-1]
test_classes = test_set[:, -1]

scaler = StandardScaler()
train_inputs = scaler.fit_transform(train_inputs)
test_inputs = scaler.transform(test_inputs)

clf = MLPClassifier(hidden_layer_sizes=(6, 3), 
                    activation='relu',
                    max_iter=500)

clf.fit(train_inputs, train_classes)

predictions = clf.predict(test_inputs)
accuracy = accuracy_score(test_classes, predictions)
cm = confusion_matrix(test_classes, predictions)

print(accuracy)
print(cm)

"""
Dokładność 75% :(
"""