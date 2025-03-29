from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()

train_data, test_data, train_labels, test_labels = train_test_split(iris.data, iris.target, train_size=0.7, random_state=13)

clf = MLPClassifier(solver='lbfgs', 
                    alpha=1e-5,
                    hidden_layer_sizes=(3, 3), 
                    random_state=1)

clf.fit(train_data, train_labels)

predictions = clf.predict(test_data)
accuracy = accuracy_score(test_labels, predictions)
cm = confusion_matrix(test_labels, predictions)

print(accuracy)
print(cm)

"""
hidden_layer_sizes = (2) oraz (3) daje dokładność 26.7%


hidden_layer_sizes = (3, 3) daje dokładność 97.8%
[[14  0  0]
 [ 0 12  0]
 [ 0  1 18]]
"""