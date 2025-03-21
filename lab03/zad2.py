from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

iris = load_iris()

train_inputs, test_inputs, train_classes, test_classes = train_test_split(
    iris.data, iris.target, train_size=0.7, random_state=13)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_inputs, train_classes)

# plt.figure(figsize=(15, 10))
# tree.plot_tree(clf,
#                feature_names=iris.feature_names,
#                class_names=iris.target_names,
#                filled=True, rounded=True)

# plt.savefig('iris_decision_tree.png', dpi=100)
# plt.show()

predictions = clf.predict(test_inputs)

def accuracy():
    good_predictions = 0
    length = len(test_classes)

    for i in range(length):
        if predictions[i] == test_classes[i]:
            good_predictions = good_predictions + 1

    print(good_predictions) #43
    print(good_predictions/length*100, "%") #95.6%

accuracy()

cm = confusion_matrix(test_classes, predictions)
print(cm)

"""
[[14  0  0] Setosa
 [ 0 12  0] Versicolour
 [ 0  2 17]] Virginica
 Czyli dwa razy pomylił się przy Virginica.
 AI zgadło 43 razy a ja 41 razy.
"""