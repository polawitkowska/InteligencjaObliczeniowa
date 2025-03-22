from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB

iris = load_iris()

train_inputs, test_inputs, train_classes, test_classes = train_test_split(
    iris.data, iris.target, train_size=0.7, random_state=13)

# k-NN: k=3 k=5 k=11
for k in [3, 5, 11]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_inputs, train_classes)

    predictions = knn.predict(test_inputs)

    accuracy = accuracy_score(test_classes, predictions)
    conf_matrix = confusion_matrix(test_classes, predictions)

    print(f"k-NN (k={k}): Dokładność: {accuracy}")
    print(conf_matrix)

# Naive Bayes
nb = GaussianNB()
nb.fit(train_inputs, train_classes)

nb_predictions = nb.predict(test_inputs)

nb_accuracy = accuracy_score(test_classes, nb_predictions)
nb_conf_matrix = confusion_matrix(test_classes, nb_predictions)
print(f"NB: Dokładność: {accuracy}")
print(conf_matrix)